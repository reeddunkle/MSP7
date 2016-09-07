import struct

class ParseMPS7(object):

    def __init__(self, file_path):
        with open(file_path, 'rb') as f:
            self.file = f.read()

    @property
    def header(self):
        magic_string = self.file[:4]
        return {
            "magic_string": magic_string,
            "version": self.version,
            "num_records": self.num_records
        }

    @property
    def version(self):
        return self.file[4]

    @property
    def num_records(self):
        return struct.unpack(">I", self.file[5:9])[0]
