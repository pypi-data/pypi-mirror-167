import functools
import logging
import operator
import yaml

from remotemanager.utils import get_version, ensure_filetype, \
    recursive_dict_update

from remotemanager.logging.utils import format_iterable


class Database:
    """
    Database file for use in the Dataset.
    Does not need to be called by the user

    Args:
        file (str):
            filename to write to
    """

    _versionkey = '~database-version~'

    def __init__(self,
                 file):

        file = ensure_filetype(file, 'yaml')

        self._logger = logging.getLogger(__name__ + '.Database')

        self._path = file
        self._storage = self._read()
        self._tree = None

    def _read(self):
        self._tree = None  # wipe tree cache
        self._logger.info(f'reading {self._path}')
        try:
            with open(self._path, 'r') as o:
                data = yaml.safe_load(o)
        except FileNotFoundError:
            self._logger.warning('file not found, creating')
            data = {Database._versionkey: get_version()}
            self._write(data)

        try:
            version = data.pop(Database._versionkey)
        except KeyError:
            version = "0"

        self._logger.info(f'database file version: {version}')

        return data

    def _write(self, data):
        self._tree = None  # wipe tree cache

        with open(self._path, 'w+') as o:
            yaml.dump(data, o)

    def read(self):
        self._storage = self._read()

    def write(self):
        self._write(self._storage)

    def update(self, payload):

        self._logger.info('updating stored info')

        self._storage = recursive_dict_update(self._storage, payload)
        self.write()

    @property
    def path(self):
        return self._path

    @property
    def tree(self):
        if self._tree is not None:
            return self._tree
        self._tree = self.climb(self._storage)
        return self._tree

    def climb(self,
              data: dict,
              branch: list = None) -> list:
        """
        "climb" a dictionary, returning a list of paths for each element

        Args:
            data (dict):
                dictionary to treat
            branch (list):
                current branch, used for recursion

        Returns:
            list of path-like strings

        """

        if branch is None:
            branch = []

        joinchar = '/'

        ret = []

        if len(data) == 0:
            ret.append(joinchar.join(branch))

        for key in data:
            tmp = []
            if isinstance(data[key], dict):
                tmp.append(key)
                ret += self.climb(data[key], branch + tmp)
            else:
                ret.append(joinchar.join(branch + [key]))
        return ret

    def find(self,
             key: str):
        """
        Find the first instance of key within the database tree
        Args:
            key (str):
                key (uuid) to look for
        Returns:
            database tree below key
        """

        def get_minimum_path(p, k):
            fullpath = p.split('/')
            return fullpath[:fullpath.index(k)+1]

        target = []
        for path in self.tree:
            if key in path:
                target = get_minimum_path(path, key)
                break
        data = chain_get(self._storage, target)

        return data


def chain_get(d: dict,
              keys: str):
    """
    get item from a nested dict using a list of keys
    Args:
        d (dict):
            nested dict to query
        keys (list):
            list of keys to use

    Returns:
        item from dict d
    """
    return functools.reduce(operator.getitem, keys, d)
