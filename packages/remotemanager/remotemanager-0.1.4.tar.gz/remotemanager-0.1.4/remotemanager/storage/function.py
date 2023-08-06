import importlib
import inspect
import logging
import os
import typing

from remotemanager.storage.sendablemixin import SendableMixin
from remotemanager.utils.uuid import generate_uuid


_SCRIPT_TEMPLATE = """
{function}

if __name__ == '__main__':    
\tkwargs = {args}
    
\tresult = {name}(**kwargs)
"""


class Function(SendableMixin):
    """
    serialise function to an executable python file for transfer

    Args:
        func:
            python function for serialisation
    Returns:
        (str) function file, to be written
    """
    def __init__(self,
                 func: typing.Callable,
                 dummy: bool = False):

        self._logger = logging.getLogger(__name__ + '.Function')
        self._logger.debug(f'creating new serialisable function for {func}')

        self._uuid = ''

        if dummy:
            # return in __init__ is janky, but we need to escape the call if
            # we're unpacking
            return

        self._source = inspect.getsource(func)
        self._uuid = generate_uuid(self._source)
        self._fname = func.__name__

    @property
    def name(self):
        return self._fname

    @property
    def raw_source(self):
        return self._source

    @property
    def uuid(self):
        return self._uuid

    @property
    def object(self):
        """
        Recreates the function object by writing out the source, and importing
        Returns:
            typing.Callable:
                the originally passed function

        """

        tmp_file = os.path.abspath(f'{self.uuid}.py')

        with open(tmp_file, 'w+') as o:
            o.write(self.raw_source)

        func_module = importlib.import_module(self.uuid)
        func_object = getattr(func_module, f'{self.name}')

        os.remove(tmp_file)

        return func_object

    def dump_to_string(self, args):
        """
        Dump this function to a serialised string, ready to be written to a
        python file
        Args:
            args (dict):
                arguments to be used for this dumped run
        Returns:
            (str):
                serialised file
        """

        if args is None:
            args = {}

        return _SCRIPT_TEMPLATE.format(**{'function': self.raw_source,
                                          'name': self.name,
                                          'args': args})
