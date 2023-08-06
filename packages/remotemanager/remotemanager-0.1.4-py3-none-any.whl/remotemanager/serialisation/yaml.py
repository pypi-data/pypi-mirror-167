import yaml

from remotemanager.utils import ensure_filetype
from remotemanager.serialisation.serial import serial


class serialyaml(serial):
    """
    subclass of serial, implementing yaml methods
    """

    def dump(self, obj, file):
        file = ensure_filetype(file, self.extension)
        with open(file, 'w+') as ofile:
            yaml.dump(obj, ofile)

    def load(self, file):
        file = ensure_filetype(file, self.extension)
        with open(file, 'r') as ofile:
            data = yaml.safe_load(ofile)
        return data

    @property
    def extension(self):
        return ".yaml"

    @property
    def importstring(self):
        return "import yaml"

    @property
    def callstring(self):
        return "yaml"
