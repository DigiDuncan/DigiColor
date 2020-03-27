class AttrDict:
    def __init__(self, data):
        self.__dict__ = data

    def __iter__(self):
        return iter(self.__dict__.items())
