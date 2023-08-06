import yaml
import logging
import os
import typing
from datetime import datetime

from remotemanager.connection.url import URL
from remotemanager.storage.database import Database
from remotemanager.storage.function import Function
from remotemanager.dataset.runner import Runner
import remotemanager.transport as tp
import remotemanager.serialisation as serial
from remotemanager.storage.sendablemixin import SendableMixin
from remotemanager.utils.uuid import generate_uuid
from remotemanager.logging.utils import format_iterable

_logger = logging.getLogger(__name__)


class Dataset(SendableMixin):
    """
    Bulk holder for remote runs. The Dataset class handles anything regarding
    the runs as a group. Running, retrieving results, sending to remote, etc.

    Args:
        function (Callable):
            function to run
        url (URL):
            connection to remote (optional)
        transport (tp.transport.Transport):
            transport system to use, if a specific is required. Defaults to
            transport.rsync
        dbfile (str):
            filename for the database file to be associated with this dataset
        script (str):
            callscript required to run the jobs in this dataset
        submitter (str):
            command to exec any scripts with. Defaults to "bash"
        name (str):
            optional name for this dataset. Will be used for runscripts
        global_run_args:
            any further (unchanging) arguments to be passed to the runner(s)
    """

    # DEV NOTE: arguments must be None for computer-url override to function
    def __init__(self,
                 function: typing.Callable,
                 url: URL = None,
                 transport: tp.transport.Transport = None,
                 serialiser=None,
                 dbfile: str = None,
                 script: str = None,
                 submitter: str = None,
                 name: str = None,
                 skip: bool = None,
                 **global_run_args):

        self._logger = logging.getLogger(__name__ + '.Dataset')
        self._logger.info('initialising Database')
        try:
            self._function = Function(function)
        except TypeError:
            _logger.info('dummy call detected, exiting early')
            return

        self._global_run_args = global_run_args

        # dataset uuid is equal to Function uuid for now
        self._name = name if name is not None else 'dataset'
        self._uuid = generate_uuid(self._function.uuid + 'Dataset' + self.name)

        self._defaultfile = f'dataset-file-{self.short_uuid}.yaml'
        if dbfile is None:
            dbfile = os.path.join(os.getcwd(), self._defaultfile)

        self._dbfile = dbfile
        self._script = script if script is not None else '#!/bin/bash'
        self._submitter = submitter if submitter is not None else 'bash'
        self._scriptfile = f'run-{self.name}.sh'
        self.skip = skip if skip is not None else False

        self._url = None
        self._transport = None
        self.url = url
        self.transport = transport
        self.serialiser = serialiser

        if os.path.isfile(self._dbfile):
            self._logger.info(f'unpacking database from {self._dbfile}')

            # create a "temporary" database from the found file
            self._database = Database(self._dbfile)
            # update it with any new values
            self.database.update(self.pack())
            # unpack from here to retrieve
            payload = self.database._storage[self.uuid]
            self.inject_payload(payload)

        else:
            self._runs = {}
            self._results = []

        # database property creates the database if it does not exist
        self.database.update(self.pack())

    @classmethod
    def recreate(cls,
                 dbfile: str,
                 function = None,
                 uuid: str = None):
        """
        Re-create the dataset from a function or uuid

        Args:
            function (Callable):
                If a dataset exists for this function, re-create it
            uuid (str):
                search the database for a uuid, and re-create the object

        Returns:
            Dataset
        """
        if function is None and uuid is None:
            raise ValueError('please provide a function or uuid to search for')

        if not os.path.isfile(dbfile):
            raise FileNotFoundError(f'could not find file {dbfile}')

        database = Database(file=dbfile)

        if uuid is None:
            # create a uuid if not otherwise found
            uuid = generate_uuid(Function(function).uuid)

        reinit = database.find(uuid)

        return cls.unpack(reinit)

    def __getattribute__(self, item):
        """
        Redirect Dataset.attribute calls to _global_run_args if possible.
        Allows for run global_run_args to be kept seperate
        Args:
            item:
                attribute to fetch
        """
        # TODO: keep an eye on this, it's hacky and liable to break
        if item != '_global_run_args' \
                and hasattr(self, '_global_run_args') \
                and item in self._global_run_args:
            return self._global_run_args.get(item)
        return object.__getattribute__(self, item)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError(f'Cannot compare Dataset against type '
                             f'{type(other)}')
        return self.uuid == other.uuid

    @property
    def database(self):
        """
        Access to the stored database object.
        Creates a connection if none exist.

        Returns:
            Database
        """
        if not hasattr(self, '_database'):
            self._database = Database(file=self._dbfile)
        return self._database
    
    def pack(self, **kwargs):
        if len(kwargs) == 0:
            self._logger.info('Dataset override pack called')
        else:
            self._logger.info('Data override pack called with kwargs')
            self._logger.info(f'{format_iterable(kwargs)}')
        return super().pack(uuid=self._uuid, **kwargs)

    def set_run_option(self, key, val):
        """
        Update a glopal run option `key` with value `val`
        Args:
            key (str):
                option to be updated
            val:
                value to set

        """
        self._global_run_args[key] = val

    def append_run(self,
                   args = None,
                   arguments = None,
                   **run_args):
        """
        Serialise arguments for later runner construction

        Args:
            args (dict):
                dictionary of arguments to be unpacked
            arguments(dict):
                alias for args
        """
        if args is None and arguments is not None:
            args = arguments

        # first grab global arguments and update them with explicit args
        run_arguments = {k: v for k, v in self._global_run_args.items()}
        run_arguments.update(run_args)

        tmp = Runner(args,
                     **run_arguments)

        if tmp.uuid not in self._runs:
            self._logger.debug(f'appending new run with uuid {tmp.uuid}')
            self._runs[tmp.uuid] = tmp
        else:
            self._logger.debug(f'runner with uuid {tmp.uuid} already exists')

        self.database.update(self.pack())

    @property
    def runners(self):
        return self._runs

    @property
    def runner_list(self):
        return [run for run in self._runs.values()]

    @property
    def function(self):
        return self._function

    @property
    def global_run_args(self):
        return self._global_run_args

    @property
    def script(self):
        return self._script

    @script.setter
    def script(self, script):
        self._script = script

    @property
    def submitter(self):
        return self._submitter

    @submitter.setter
    def submitter(self, submitter):
        self._submitter = submitter

    @property
    def url(self):
        if not hasattr(self, '_url'):
            self.url = None
        return self._url

    @url.setter
    def url(self, url=None):
        """
        Returns an empty (local) url connection if url is None

        Args:
            url (URL):
                url to be verified
        """
        self._logger.info(f'new url is being set to {url}')
        if url is None:
            self._logger.warning('no URL specified for this dataset, creating '
                                 'localhost')
            self._url = URL()
        else:
            self._url = url

        if not type(url) == URL and issubclass(type(url), URL):

            init_attrs = locals()

            self._logger.info('url is a computer, collecting attributes')

            self._script = url.script

            attrs = ['name', 'script', 'submitter']

            for attr in attrs:

                init_set = init_attrs.get(attr, None)

                self._logger.debug(f'attr {attr} is set to {init_set}')
                if init_set is None:
                    preset = getattr(url, attr, None)
                    setattr(self, attr, preset)

                    self._logger.info(f'set attribute {attr} to {preset}')

        timeout = self._global_run_args.get('timeout', None)
        max_timeouts = self._global_run_args.get('max_timeouts', None)

        self._url.timeout = timeout
        self._url.max_timeouts = max_timeouts

    @property
    def transport(self):
        if not hasattr(self, '_transport'):
            self.transport = None
        return self._transport

    @transport.setter
    def transport(self, transport=None):
        if transport is None:
            self._logger.warning('no transport specified for this dataset, '
                                 'creating basic rsync')
            self._transport = tp.rsync(self.url)
        else:
            self._transport = transport

    @property
    def serialiser(self):
        if not hasattr(self, '_serialiser'):
            self.serialiser = None
        return self._serialiser

    @serialiser.setter
    def serialiser(self, serialiser=None):
        if serialiser is None:
            self._logger.warning('no serialiser specified,'
                                 'creating basic yaml')

            self._serialiser = serial.serialyaml()

        else:
            self._serialiser = serialiser


    @property
    def dbfile(self):
        return self.database.path

    def remove_database(self):
        os.remove(self.dbfile)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            try:
                name = str(name)
            except TypeError:
                raise ValueError('name can only be str type')

        self._name = name

    @property
    def uuid(self):
        return self._uuid

    @property
    def short_uuid(self):
        return self._uuid[:8]

    def set_all_runner_states(self, state):
        for runner in self.runner_list:
            runner.state = state

    def check_all_runner_states(self, state):
        return all([r.state == state for r in self.runner_list])

    def run(self,
            force: bool = False,
            **run_args):
        """
        Run the functions

        Args:
            force (bool):
                force all runs to go through, ignoring checks
            run_args:
                any arguments to pass to the runners during this run.
                will override any "global" arguments set at Dataset init
        """
        run_store = {}
        if force:
            run_store = {r.uuid: True for r in self.runner_list}

        elif self.skip:
            self._logger.warning('running with skip = True, '
                                 'checking runner archive')

            for runner in self.runner_list:
                uuid = runner.uuid

                if runner.last_status == 'submitted':
                    msg = f'runner is already submitted, skipping'
                    self._logger.info(msg)

                    run_store[uuid] = False
                    continue

                payload = self.database.find(uuid)
                archived = Runner.unpack(payload)
                self._logger.info(f'assessing runner {runner.short_uuid}')
                if 'completed' in archived.status_list:
                    self._logger.info('runner is completed, updating')
                    runner = archived
                    runner.status = 'collected archived completion'
                    run_store[uuid] = False
                else:
                    self._logger.info('no result found, appending to run list')
                    run_store[uuid] = True

        else:
            run_store = {r.uuid: True for r in self.runner_list}

        if hasattr(self.url, 'script'):
            self.script = self.url.script

        for arg, val in run_args.items():
            if arg not in self._global_run_args:
                self._logger.debug(f'updating global arg {arg} -> {val}')
                self._global_run_args[arg] = val

        if self.script:
            self._run_scripted(run_store, run_args)
        elif not self.url.is_local:
            self._run_direct_remote(run_store, run_args)
        else:
            self._run_direct_local(run_store, run_args)

        self.database.update(self.pack())

    def _run_scripted(self, run_store: dict, run_args: dict):

        self._logger.info('preparing for scripted run')

        script = [self.script]

        asynchronous = getattr(self, 'asynchronous', False)

        for runner in self.runner_list:
            if run_store[runner.uuid] is not None and not run_store[runner.uuid]:
                msg = f'skipping run for runner ' \
                      f'{runner.short_uuid}'
                self._logger.info(msg)
                print(msg)
                continue

            runner.update_run_options(run_args)
            runner.state = runner._state_script_remote
            runner.result_extension = self.serialiser.extension
            staged = os.path.join(runner.local_dir, runner.runfile)

            if not os.path.isdir(runner.local_dir):
                self._logger.info('creating local dir for the runner')
                os.makedirs(runner.local_dir)

            dumpstring = [f'\t{line}' for line in
                          self.serialiser.dumpstring(runner.resultfile)]
            runfile = [self.serialiser.importstring,
                       'import os',
                       self.function.dump_to_string(runner.args)] + dumpstring

            with open(staged, 'w+') as o:
                o.write('\n'.join(runfile))

            rundir = runner.run_dir
            if self.url.is_local:
                rundir = os.path.join(os.getcwd(), rundir)
            else:
                rundir = f'$HOME/{rundir}'
            run_line = f'cd "{rundir}" && '\
                       f'touch "{runner.runfile}" && '\
                       f'{self.url.python} "{runner.runfile}"'

            asynchronous = runner.run_option('asynchronous', True)
            if asynchronous and self.submitter == 'bash':
                self._logger.debug('appending "&" for async run')
                run_line += ' &'

            script.append(run_line)

            self.transport.queue_for_push(runner.runfile,
                                          runner.local_dir,
                                          runner.run_dir)

            runner.state = 'submitted'

        _scriptfile = os.path.join(runner.local_dir, self._scriptfile)
        self._logger.info(f'writing scriptfile into {_scriptfile}')
        script_content = '\n'.join(script)
        self._logger.debug(f'script content:\n{script_content}')
        with open(_scriptfile, 'w+') as o:
            o.write(script_content)

        self._logger.info(f'queuing run script into folder {runner.run_dir}')
        self.transport.queue_for_push(os.path.split(_scriptfile)[1],
                                      os.path.split(_scriptfile)[0],
                                      runner.run_dir)

        self.transport.transfer()

        self._logger.debug('running the script')

        remote_script_file = os.path.join(runner.run_dir, self._scriptfile)
        self.url.cmd(f'{self.submitter} {remote_script_file}',
                     asynchronous=asynchronous)

    def _run_direct_local(self, run_store: dict, run_args: dict):

        self._logger.info('running local direct')
        for runner in self.runner_list:
            if run_store[runner.uuid] is not None and \
                    not run_store[runner.uuid]:
                msg = f'skipping run for runner ' \
                      f'{runner.short_uuid}'
                self._logger.info(msg)
                print(msg)
                continue

            runner.run(self.function.object, **run_args)

    def _run_direct_remote(self, run_store: dict, run_args: dict):

        raise NotImplementedError

    def _check_for_resultfiles(self) -> dict:
        self._logger.info('checking for finished runs')
        files_to_check = []
        for runner in self.runner_list:
            files_to_check.append(runner.resultpath)

        return self.url.utils.file_mtime(files_to_check)

    def fetch_results(self,
                      raise_if_not_finished: bool = False) -> list:
        """
        Collect any scripted run resultfiles and insert them into their runners

        Args:
            raise_if_not_finished (bool):
                raise an error if all calculations not finished

        Returns:
            None
        """
        present_runfiles = self._check_for_resultfiles()

        if not any(present_runfiles.values()):
            self._logger.info('no valid results found, exiting early')
            return [None]*len(self.runner_list)

        self._logger.info('present result files:')
        self._logger.info(format_iterable(present_runfiles))
        for runner in self.runner_list:
            if present_runfiles[runner.resultpath]:
                self.transport.queue_for_pull(os.path.split(
                                              runner.resultpath)[1],
                                              runner.local_dir,
                                              runner.run_dir)

        self._logger.info('pulling completed result files')
        self.transport.transfer()
        for runner in self.runner_list:
            pulled = runner.local_resultpath

            result = self.serialiser.load(pulled)

            timestamp = int(os.path.getmtime(pulled))

            if timestamp < runner.last_updated:
                self._logger.warning('calculation not completed yet')
                continue

            mtime = datetime.fromtimestamp(timestamp)
            runner.insert_history(mtime, 'resultfile created remotely')

            runner.result = result

        self.database.update(self.pack())

        if not self.all_finished and raise_if_not_finished:
            raise RuntimeError('Calculations not yet completed!')

    @property
    def is_finished(self):
        ret = {r.uuid: None for r in self.runner_list}
        if self.skip:
            self._logger.info('skip is true, checking runner first')
            for runner in self.runner_list:
                if runner.is_finished:
                    ret[runner.uuid] = True

        if self.script:
            self._logger.info('scripted run, checking for files')
            # look for the resultfiles
            fin = self._check_for_resultfiles()

            # create a list of the resultfiles that are available
            for runner in self.runner_list:
                if ret[runner.uuid] is not None:
                    continue

                resultpath = runner.resultpath
                last_updated = runner.last_updated
                mtime = fin[resultpath]

                self._logger.debug(f'checking file {resultpath}. mtime '
                                   f'{mtime} vs runner time {last_updated}')

                if mtime is None:
                    ret[runner.uuid] = False
                elif mtime >= last_updated:
                    ret[runner.uuid] = True
                else:
                    ret[runner.uuid] = False

            return list(ret.values())

        return [r.is_finished for r in self.runner_list]

    @property
    def all_finished(self):
        return all(self.is_finished)

    @property
    def results(self):
        results = [r.result for r in self.runner_list]
        # if all([r is None for r in results]):
        #     self._logger.info('results are all None, fetching results')
        #     self.fetch_results()
        #     return self.results
        return results

    def clear_results(self):
        for runner in self.runner_list:
            file = runner.resultpath
            self._logger.info(f'attempting to clear result file {file}')
            try:
                os.remove(file)
                self._logger.info('Done')
            except FileNotFoundError:
                self._logger.info('file not found')
