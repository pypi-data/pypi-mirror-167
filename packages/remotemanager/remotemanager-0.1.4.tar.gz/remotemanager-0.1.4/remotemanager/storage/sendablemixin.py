import collections.abc
import importlib
import inspect
import logging
import os.path

import yaml

CLASS_STORAGE_KEY = '~serialisedclass~'

_logger = logging.getLogger(__name__)


class SendableMixin:
    """
    baseclass for a "sendable" object, providing methods for conversion to
    yaml format
    """

    def pack(self,
             uuid: str = None,
             file: str = None):
        """
        "packs" the object into a dict-format, ready for yaml-dump

        Args:
            uuid (str):
                optional uuid string to package this data inside
            file (str):
                package to file

        Returns:
            (dict):
                packaged Runner
        """
        # remove any attributes not to be packaged
        # these objects are either not needed, or can be re-created on the
        # recipient end
        do_not_package = ['_logger',
                          '_database',
                          '_url',
                          '_serialiser'
                          ]

        payload = {k: self.serialise(v)
                   for k, v in self.__dict__.items()
                   if k not in do_not_package}

        payload[CLASS_STORAGE_KEY] = get_class_storage(self)

        if uuid:

            if '_uuid' in payload and payload['_uuid'] != uuid:
                raise ValueError('passed uuid and _uuid key in payload do'
                                 'not match!')

            payload['_uuid'] = uuid

            payload = {uuid: payload}

        if file is not None:
            print(f'dumping payload to {file}')
            with open(file, 'w+') as o:
                yaml.dump(payload, o)

            return None

        return payload

    @classmethod
    def unpack(cls,
               data: dict = None,
               file: str = None,
               limit: bool = True):
        """
        Re-create an object from a packaged payload coming from obj.pack

        .. note ::

            use this function to unpack from a payload _outside_ an object

        If the object takes a `dummy` flag, this will be inserted into the args
        The `dummy` kwarg MUST be in the arguments for a class which cannot be
        simply initialised with blank args, and logic within that object's
        __init__ to account for this, something along the lines of

        >>> def __init__(self, dummy):
        >>>     if dummy:
        >>>         return

        will break the object creation at that point

        Args:
            data (dict):
                __dict__ payload from the object that was packaged
            file (str):
                filepath to unpack from, if data is not given
            limit (bool):
                disable to allow outside classes to be unserialised
        Returns: re-created object
        """

        if data is None:
            if file is None:
                raise ValueError('please provide a data payload or filepath '
                                 'to read from')
            elif not os.path.isfile(file):
                raise FileNotFoundError(f'could not find file {file}')

            with open(file, 'r') as o:
                data = yaml.safe_load(o)

        # if the data passed is a {uuid: {data}} format dict, search for a uuid
        # within and extract the {data}
        firstkey = list(data)[0]
        if data[firstkey] is not None \
                and '_uuid' in data[firstkey] \
                and data[firstkey]['_uuid'] == firstkey:
            data = data[firstkey]

        # grab the required arguments for the class, and fill with placeholders
        # of the correct type
        params = inspect.signature(cls).parameters
        required_args = {}
        for arg_name, v in params.items():
            if v.default is inspect._empty and arg_name != 'kwargs':
                required_args[arg_name] = v.annotation

        if 'dummy' in params.keys():
            required_args['dummy'] = True

        # create a new instance of this class, using the placeholder args
        new = cls(**required_args)
        if hasattr(new, '_logger'):
            new._logger.info('blank class created with args')
        # update this object with the values extracted from the payload
        if isinstance(data, str):
            _logger.debug(f'importing from filename {data}')
            data = yaml.safe_load(data)

        # this is REQUIRED to be separate to the return call
        new.inject_payload(data, limit)

        return new

    def inject_payload(self,
                       payload: dict,
                       limit: bool = True):
        """
        inject payload into the __dict__, effectively re-creating the object

        .. note ::

            use this function to unpack _within_ an object

        Args:
            payload (dict):
                __dict__ payload from the object that was packaged
            limit (bool):
                enable or disable safeties
        """
        if hasattr(self, '_logger'):
            self._logger.info(f'finalising unpacking of {type(self)}')

        # temporary attribute to check for a valid class
        self._unpack_validate = True

        if CLASS_STORAGE_KEY in payload:
            selfkey = get_class_storage(self)
            packkey = payload[CLASS_STORAGE_KEY]

            if selfkey != packkey:
                raise RuntimeError(f'attempting to unpack class '
                                   f'{packkey["name"]} as '
                                   f'{selfkey["name"]}')

            delattr(self, '_unpack_validate')

        unpacked = {k: self.unserialise(v, limit) for k, v in payload.items()}

        self.__dict__.update(unpacked)

    def serialise(self,
                  obj):
        """
        Recurse over any iterable objects, or call the pack() method of any
        `SendableMixin` objects, for serialisation
        Args:
            obj:
                object to be packaged
        Returns:
            yaml-friendly object
        """
        if issubclass(type(obj), SendableMixin):

            payload = obj.pack()

            # add a passthrough for the object to be imported and recreated
            payload[CLASS_STORAGE_KEY] = get_class_storage(obj)
            return payload

        elif isinstance(obj, collections.abc.Mapping):
            # dict type
            return {k: self.serialise(v) for k, v in obj.items()}

        elif hasattr(obj, '__setitem__'):
            # list-type
            return [self.serialise(v) for v in obj]

        return obj

    def unserialise(self,
                    obj,
                    limit: bool = True):
        """
        Undo a serialised packaging, by importing the called object and calling
        its unpack() method
        Args:
            obj:
                payload to be unpacked
            limit (bool):
                exit if the object to be unpacked is not part of the
                remotemanager package
        Returns:
            object before packaging
        """
        try:
            unpackable = obj.get(CLASS_STORAGE_KEY)
        except AttributeError:
            unpackable = False

        if unpackable:
            # print(f'unserialising unpackable object {obj}')
            # extract the class to import
            source = obj.pop(CLASS_STORAGE_KEY)

            # import the module
            modulename = source['mod']
            if limit and not modulename.startswith('remotemanager'):
                raise ValueError('module to import is not within the '
                                 'remotemanager package, exiting for safety')
            mod = importlib.import_module(modulename)

            # now get the actual class to import and unpack
            cls = getattr(mod, source['name'])

            return cls.unpack(obj)

        elif isinstance(obj, collections.abc.Mapping):
            # dict type
            return {k: self.unserialise(v) for k, v in obj.items()}

        elif hasattr(obj, '__setitem__'):
            # list-type
            return [self.unserialise(v) for v in obj]

        return obj


def get_class_storage(obj):
    return {'mod': obj.__module__,
            'name': obj.__class__.__name__}
