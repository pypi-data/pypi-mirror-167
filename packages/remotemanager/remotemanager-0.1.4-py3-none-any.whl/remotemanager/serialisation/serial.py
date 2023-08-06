from remotemanager.utils import ensure_filetype


class serial:

    """
    Baseclass for holding serialisation methods. Subclass this class when
    implementing new serialisation methods
    """

    def __init__(self):
        pass

    def dump(self, obj, file: str) -> None:
        """
        Dumps object `obj` to file `file`
        Args:
            obj:
                object to be dumped
            file (str):
                filepath to dump to

        Returns:
            None
        """
        raise NotImplementedError

    def load(self, file: str):
        """
        Loads previously dumped data from file `file`
        Args:
            file (str):
                filepath to load

        Returns:
            Stored object
        """
        raise NotImplementedError

    @property
    def extension(self) -> str:
        """
        Returns (str):
            intended file extension
        """
        raise NotImplementedError

    @property
    def importstring(self) -> str:
        """

        Returns:
            Module name to import.
            See subclasses for examples
        """
        raise NotImplementedError

    @property
    def callstring(self) -> str:
        """

        Returns:
            Intended string for calling this module's dump.
            See subclasses for examples
        """
        raise NotImplementedError

    def dumpstring(self, file: str) -> str:
        """

        Args:
            file (str):
                filename to dump to

        Returns (str):
            Formatted string for run files.
            See subclasses for examples
        """
        file = ensure_filetype(file, self.extension)
        string = [f"with open('{file}', 'w+') as o:",
                  f'\t{self.callstring}.dump(result, o)']
        return string
