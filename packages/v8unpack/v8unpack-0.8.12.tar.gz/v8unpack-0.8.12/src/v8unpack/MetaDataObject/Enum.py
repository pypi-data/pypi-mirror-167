from ..MetaDataObject.core.Simple import Simple


class Enum(Simple):
    @classmethod
    def get_decode_header(cls, header_data):
        return header_data[0][1][5][1]
