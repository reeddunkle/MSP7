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


    def records(self):
        # Returns dict of records by ID
        pass

    def total_debit(self):
        # Return total amount in dollars of debits
        pass

    def total_credit(self):
        # Return total amount in dollars of credits
        pass

    def autopay_started(self):
        # Returns number of autopays started
        pass

    def autopay_ended(self):
        # Returns number of autopays ended
        pass

    def balance(self, id):
        # Returns balance of user ID
        pass
