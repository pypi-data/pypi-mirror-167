import logging
import os
import typing

from remotemanager.storage.sendablemixin import SendableMixin
from remotemanager.logging.utils import format_iterable
from remotemanager.utils.uuid import generate_uuid

from datetime import datetime


class Runner(SendableMixin):
    """
    The Runner class stores any info pertaining to this specific run. E.g.
    Arguments, result, run status, files, etc.
    """

    _defaults = {'skip': False}

    _state_direct_remote = 'disconnected - remote direct run'
    _state_script_remote = 'script submitted remotely'
    _state_script_local = 'script submitted locally'

    def __init__(self,
                 arguments: dict,
                 **kwargs):

        self._logger = logging.getLogger(__name__ + '.Runner')

        self._run_options = self._set_defaults(kwargs)

        self._args = arguments
        self._uuid = generate_uuid(format_iterable(arguments))
        self._time_format = '%Y-%m-%d %H:%M:%S'
        self._state_time = None
        self._state = None
        self._result = None
        self._extension = '.yaml'

        self._logger.info(f'new runner (id {self.uuid}) created')

        self._history = {}
        self.state = 'created'

    @staticmethod
    def _set_defaults(kwargs: dict = None) -> dict:
        """
        Sets default arguments as expected. If used as a staticmethod, returns
        the defaults
        """

        if kwargs is None:
            kwargs = {}

        for k, v in Runner._defaults.items():
            if k not in kwargs:
                kwargs[k] = v

        return kwargs

    def _parse_dir(self,
                   dir: str) -> str:
        """
        ensure a properly formatted local path for this run

        Args:
            dir (str):
                path

        Returns:
            formatted abspath
        """
        if dir is None:
            return os.getcwd()
        elif dir == '':
            return os.getcwd()
        elif os.path.isabs(dir):
            return dir
        return os.path.abspath(dir)

    @property
    def uuid(self):
        """
        The uuid of this runner
        """
        return self._uuid

    @property
    def short_uuid(self):
        """
        A short uuid for filenames
        """
        return self.uuid[:8]

    @property
    def runfile(self):
        """
        Runfile name
        """
        return f'{self.short_uuid}-run.py'

    @property
    def runpath(self):
        """
        Runfile name
        """
        return os.path.join(self.local_dir, f'{self.short_uuid}-run.py')

    @property
    def local_dir(self):
        """
        Local staging directory
        """
        return self._run_options.get('local_dir', 'staging')

    @local_dir.setter
    def local_dir(self,
                  path: str) -> None:
        self._run_options['local_dir'] = path

    @property
    def run_dir(self):
        """
        Intended running directory. If not set, attempts to use remote_dir and
        then falls back on local_dir
        """
        if 'run_dir' in self._run_options:
            return self._run_options['run_dir']
        return self._run_options.get('remote_dir', self.local_dir)

    @run_dir.setter
    def run_dir(self,
                dir: str) -> None:
        self._run_options['run_dir'] = dir

    @property
    def resultfile(self):
        """
        Result file name
        """
        return f'{self.short_uuid}-result.{self.result_extension}'

    @property
    def result_extension(self):
        return self._extension

    @result_extension.setter
    def result_extension(self, ext):
        self._extension = ext.strip('.')


    @property
    def resultpath(self):
        """
        Path to result file
        Currently a concatenation of the local dir and file name
        """
        # TODO change this to an adaptive path
        return os.path.join(self.run_dir, self.resultfile)

    @property
    def local_resultpath(self):
        """
        Path to local version of result file
        """
        # TODO change this to an adaptive path
        return os.path.join(self.local_dir, self.resultfile)

    @property
    def args(self):
        """
        Arguments for the function
        """
        return self._args

    @property
    def result(self):
        """
        Result (If available)
        """
        return self._result

    @result.setter
    def result(self, result) -> None:
        self._result = result
        self.state = 'completed'

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self,
              newstate: str) -> None:
        """
        Update the state and store within the runner history
        """

        state_time = datetime.now()

        self.insert_history(state_time, newstate)

        self._state_time = int(state_time.strftime('%s'))
        self._state = newstate

    def format_time(self, time):
        return time.strftime(self._time_format)

    @property
    def history(self):
        """
        Returns (dict):
            State history of this runner
        """
        return self._history

    @property
    def status_list(self):
        return list(self._history.values())

    def insert_history(self,
                       time: datetime,
                       newstate: str) -> None:
        """
        Insert a state into this runner's history
        Args:
            time (datetime.time):
                time this state change occurred
            newstate (str):
                status to update

        Returns:
            None
        """
        if not isinstance(time, datetime):
            raise ValueError(f'time of type {type(time)} should be a datetime '
                             f'instance')

        base_timekey = self.format_time(time)
        idx = 0
        timekey = f'{base_timekey}/{idx}'
        while timekey in self._history:
            idx += 1

            timekey = f'{base_timekey}/{idx}'
            self._logger.info(f'timekey updated to {timekey}')

        self._logger.info(f'updating runner {self.short_uuid} state -> '
                          f'{newstate}')
        self._history[timekey] = newstate

    @property
    def last_updated(self):
        """
        Time that this runner state last changed
        """
        return self._state_time

    @property
    def last_status(self):
        """
        Most recent status
        """
        return self.status_list[-1]

    def run(self,
            function: typing.Callable,
            **kwargs) -> None:
        """
        Substitutes runner args into function and runs, storing the result
        Args:
            function:
                typing.Callable:
                    function to run
        Returns:
            None
        """
        self._logger.info(f'running function {self.uuid}')
        self.state = 'submitted'

        self.update_run_options(kwargs)

        result = function(**self.args)

        self.result = result
        self._logger.info(f'run complete for {self.uuid}')

    @property
    def is_finished(self):
        """
        Attempts to determine if this runner has completed its run

        Returns (bool):
            completion status
        """
        self._logger.info(f'checking finished state of runner '
                          f'{self.short_uuid}')

        if 'completed' in self.status_list:
            self._logger.info('state is completed: True')
            return True

        elif Runner._state_script_local in self.status_list:
            self._logger.info(f'script based submission, checking for '
                              f'file {self.resultpath}')
            # last status update was a script based submission
            # check for results file
            return os.path.isfile(self.resultpath)

        elif Runner._state_script_remote in self.status_list:
            self._logger.info('remote scripted run, dataset needs '
                              'to check this')
            # need to search for the results file
            return False

        elif Runner._state_direct_remote in self.status_list:
            self._logger.info('remote direct run, dataset needs '
                              'to check this')
            # this runner is "orphaned", and the result needs to be grabbed
            # remotely
            return False

        return False

    def update_run_options(self,
                           run_args: dict) -> None:
        """
        Update run args with dict `run_args`
        Args:
            run_args (dict):
                new run arguments

        Returns:
            None
        """
        self._logger.info('updating run options with new run args:')
        self._logger.info(format_iterable(run_args))

        self._run_options.update(run_args)

    def run_option(self,
                   option: str,
                   default=None):
        """
        Return a run option

        Args:
            option (str):
                key to search for
            default:
                default argument to provide to get

        Returns:
            option if available, else None
        """
        ret = self._run_options.get(option, default)
        self._logger.debug(f'getting run option {option}: {ret}')
        return ret

    @property
    def run_args(self):
        """
        Display the run arguments

        Returns:
            (dict) run_args
        """
        return self._run_options
