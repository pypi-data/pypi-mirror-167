"""
URL base class for connecting to remote systems
"""
import logging
import os
import re
import typing

from remotemanager.logging.utils import format_iterable
from remotemanager.connection.cmd import CMD
from remotemanager.storage.sendablemixin import SendableMixin
from remotemanager.utils import ensure_list


class URL(SendableMixin):
    """
    Container to store the url info for a Remote run

    The url should contain everything pertaining to the _remote_, allowing
    Dataset to be remote-agnostic

    Arguments:
        user (str):
            username for the remote system
        host (str):
            host address of the remote system
        port (int, str):
            port to connect to for ssh tunnels
        verbose (bool):
            base-verbosity for connections
        timeout (int):
            time to wait before issuing a timeout for cmd calls
        max_timeouts (int):
            number of times to attempt cmd communication in case of a timeout
        python (str):
            string used to initiate a python instance
    """

    _localhost = 'localhost'

    def __init__(self,
                 user: str = None,
                 host: str = None,
                 port: int = None,
                 verbose: bool = False,
                 timeout: int = 5,
                 max_timeouts: int = 3,
                 python: str = 'python',
                 raise_errors: bool = True):

        if host is None:
            host = URL._localhost
        self._conn = {'user': user,
                      'host': host,
                      'port': port}

        self.timeout = timeout
        self.max_timeouts = max_timeouts
        self.python = python

        self._verbose = verbose
        self._raise_errors = raise_errors
        self._ssh_override = None

        self.utils = URLUtils(self)

        self._logger = logging.getLogger(__name__ + '.URL')
        self._logger.info('new url created with url details:'
                          f'{format_iterable(self._conn)}')

    @property
    def user(self) -> str:
        """
        Returns:
            (str) currently configured username
        """
        return self._conn['user']

    @property
    def host(self) -> str:
        """
        Returns:
           (str) currently configured hostname
        """
        return self._conn['host'] or URL._localhost

    @property
    def userhost(self):
        """
        Returns:
           (str) user@host string if possible
        """
        if self.user is None:
            return self.host
        else:
            return f'{self.user}@{self.host}'

    @property
    def port(self) -> int:
        """
        Returns:
            (int) currently configured port (defaults to 22)
        """
        port = self._conn['port'] or 22
        return port

    @property
    def ssh(self):
        """
        Returns:
            ssh insert for commands on this connection
        """
        if self.is_local:
            raise ValueError('ssh cannot be generated for a local url')

        if not self._ssh_override:
            ret = [f'ssh -p {self.port} ']
        else:
            return self._ssh_override

        if self.user is not None:
            tmp = [self.user]
            if not self.is_local:
                tmp.append('@')

            ret.append(''.join(tmp))

        ret.append(self.host)

        return ''.join(ret)

    @ssh.setter
    def ssh(self,
            newssh: str) -> None:
        """
        Allows forced override of the ssh command

        Inserting extra flags into the ssh can be done as follows:

        >>> url = URL()
        >>> print(url.ssh)
        >>> "ssh"
        >>> url.ssh = "LANG=C " + url.ssh
        >>> print(url.ssh)
        >>> "LANG=C ssh"

        Args:
            newssh (str):
                new ssh string to insert

        Returns:
            None
        """
        self._ssh_override = newssh

    def clear_ssh_override(self):
        """
        Wipe any override applied to ssh. Can also be done by setting
        url.ssh = None

        Returns:
            None
        """
        self._ssh_override = None

    @property
    def is_tunnel(self):
        """
        Uses the presence of an assigned port to determine if we are tunnelling
        or not

        Returns:
            (bool) True if this is a tunnelled connection
        """
        return self._conn['port'] is not None

    @property
    def is_local(self):
        """
        Returns True if this connection has no external end

        Returns:
            (bool) True if this connection is purely local
        """
        host = self.host
        if host == URL._localhost:
            return True
        elif host.startswith('127.'):
            return True
        return False

    def folder(self, path):
        """
        returns a remoteFolder instance at `path`
        Args:
            path (str):
                absolute path to folder

        Returns:
            Folder
        """

    def cmd(self,
            cmd: str,
            asynchronous: bool = False,
            local: [bool, None] = None,
            stdout: str = None,
            stderr: str = None,
            timeout: int = None,
            max_timeouts: int = None,
            raise_errors: bool = None,
            dry_run: bool = False) -> typing.Union[CMD, str]:
        """
        Creates and executes a command
        Args:
            asynchronous (bool):
                run this command asynchronously
            cmd (str):
                command to execute
            local (bool, None):
                force a local or remote execution. Defaults to None
            stdout (str):
                optional file to redirect stdout to
            stderr (str):
                optional file to redirect stderr to
            timeout (int):
                time to wait before issuing a timeout
            max_timeouts (int):
                number of times to attempt communication in case of a timeout
            raise_errors (bool):
                override for global setting. Raise any stderr if encountered
            dry_run (bool):
                don't exec the command if True, just returns the string
        Returns:
            (remotemanager.connection.cmd.CMD):
                returned command instance
        """
        if local is not None and not local:
            self._logger.info('forced remote call; appending ssh to cmd')
            cmd = f'{self.ssh} "{cmd}"'
        elif local is None and not self.is_local:
            self._logger.info('implicit remote call; appending ssh to cmd')
            cmd = f'{self.ssh} "{cmd}"'
        if raise_errors is None:
            raise_errors = self._raise_errors

        timeout = self.timeout \
            if timeout is None else timeout
        max_timeouts = self.max_timeouts \
            if max_timeouts is None else max_timeouts

        if dry_run:
            return cmd.strip()

        thiscmd = CMD(cmd.strip(),
                      asynchronous=asynchronous,
                      stdout=stdout,
                      stderr=stderr,
                      timeout=timeout,
                      max_timeouts=max_timeouts,
                      raise_errors=raise_errors)
        thiscmd.exec()

        return thiscmd


class URLUtils:
    """
    Extra functions to go with the URL class, called via URL.utils

    As it requires a parent `URL` to function, and is instantiated with a
    `URL`, there is little to no purpose to using this class exclusively

    Arguments:
        parent (URL):
            parent class to provide utils to
    """
    def __init__(self, parent: URL):

        self._logger = logging.getLogger(__name__ + '.URLUtils')
        self._logger.info(f'creating a utils extension to parent: {parent}')

        self._parent = parent

    def file_mtime(self,
                   files: list,
                   local: bool = None):
        """
        Check file modification times of [files]

        Args:
            files (list):
                list of paths to files
            local (bool):
                force a local search

        Returns (dict):
            {file: mtime (unix)} dictionary

        """

        def regex_stat_error(stderr):
            search = re.search("\'(.*)\'", stderr)
            if search is None:
                return None
            return search.group(0).strip("'")

        self._logger.info(f'performing stat on files: {files}')
        if local is None:
            local = self._parent.is_local

        files = ensure_list(files)

        basecmd = 'stat -c %Y'
        if len(files) == 0:
            raise ValueError('file list cannot be empty!')
        elif len(files) <= 1:
            cmd = f'{basecmd} {files[0]}'
        else:
            cmd = f'{basecmd} {{' + ','.join(files) + '}'

        ret = self._parent.cmd(cmd,
                               local=local,
                               raise_errors=False)
        # stdout will contain a list of valid times
        times = [int(t) for t in ret.stdout.split('\n') if t != '']
        self._logger.info(f'valid file times: {times}')
        # stderr should contain a list of files which do not exist
        error = [regex_stat_error(e) for e in ret.stderr.split('\n')]
        self._logger.info(f'invalid file names: {error}')

        output = {}
        idx = 0
        for file in files:
            if file in error:
                output[file] = None
            else:
                output[file] = times[idx]
                idx += 1

        return output

    def file_presence(self,
                      files: list,
                      local: bool = None):
        """
        Search for a list of files, returning a boolean presence dict

        Args:
            files (list):
                list of paths to files
            local (bool):
                force a local search
        Returns:
            {file: present} dictionary
        """
        self._logger.info(f'checking for presence of files: {files}')
        if local is None:
            local = self._parent.is_local

        files = ensure_list(files)

        times = self.file_mtime(files,
                                local=local)

        return {f: times[f] is not None for f in files}

    def search_folder(self,
                      files: list,
                      folder: str,
                      local: bool = None) -> dict:
        """
        Search `folder` for `files`, returning a boolean presence dict

        Arguments:
            files (list):
                list of filenames to check for. Optionally, a string for a
                single file
            folder (str):
                folder to scan
            local (bool):
                perform the scan locally (or remotely)
        Returns (dict):
            {file: present} dictionary
        """
        if local is None:
            local = self._parent.is_local
        fpath = os.path.abspath(folder)  # not locally available ?

        self._logger.debug(f'scanning folder {fpath}')
        self._logger.debug('searching for files:')
        self._logger.debug(f'{format_iterable(files)}')

        ls_return = self.ls(fpath, local=local, as_list=True)

        scan = [os.path.basename(f) for f in ls_return]

        self._logger.debug('scan sees:')
        self._logger.debug(f'{format_iterable(scan)}')

        if isinstance(files, str):
            self._logger.info('files is a string, running in singular mode')
            ret = {files: os.path.basename(files) in scan}
        else:
            ret = {file: os.path.basename(file) in scan for file in files}

        return ret

    def touch(self,
              file: str,
              local: bool = None,
              raise_errors: bool = True):
        """
        perform unix `touch`, creating or updating `file`

        Arguments:
            file (str):
                filename or path to file
            local (bool):
                force local (or remote) execution
            raise_errors (bool):
                raise any stderr encountered
        """
        if local is None:
            local = self._parent.is_local
        self._logger.debug(f'utils touch on file {file}')
        fname = os.path.abspath(file)
        return self._parent.cmd(f'touch {fname}',
                                local=local,
                                raise_errors=raise_errors)

    def mkdir(self,
              file: str,
              local: bool = None,
              raise_errors: bool = True):
        """
        perform unix `mkdir -p`, creating a folder structure

        Arguments:
            file (str):
                name or path to folder
            local (bool):
                force local (or remote) execution
            raise_errors (bool):
                raise any stderr encountered
        """
        if local is None:
            local = self._parent.is_local
        self._logger.debug(f'utils mkdir on path {file}')
        fname = os.path.abspath(file)
        # print(f'making dir {fname}')
        return self._parent.cmd(f'mkdir -p {fname}',
                                local=local,
                                raise_errors=raise_errors)

    def ls(self,
           file: str,
           as_list: bool = True,
           local: bool = None,
           raise_errors: bool = True):
        """
        Identify the files present on the directory

        Arguments:
            file (str):
                name or path to folder.
            as_list (bool):
                convert to a list format
            local (bool):
                force local (or remote) execution
            raise_errors (bool):
                raise any stderr encountered
        """
        if local is None:
            local = self._parent.is_local
        self._logger.debug(f'utils ls on path {file}')
        fname = os.path.abspath(file) if local else file

        ret = self._parent.cmd(f'ls {fname}',
                               local=local,
                               raise_errors=raise_errors)

        if as_list:
            ret = [f for f in ret.stdout.split('\n') if f != '']
        return ret