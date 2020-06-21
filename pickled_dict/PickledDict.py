import pickle
from collections.abc import MutableMapping
from os import PathLike


class PickledDict(MutableMapping):
    """
    This Dictionary gets stored as a file and is able to handle complex objects, like a Numpyarray.
    Use it the following way. Either load a dict from the filesystem

    data = PickledDict('the/way/to/your/file')

    or save an existing dict to the filesystem and bind it to the Variable, by setting kwargs

    regular_dict = {'key1': 'value1', 'key2': 'value2'}
    data = PickledDict('the/way/to/your/file', **regular_dict)

    To write data inside simply use:

    data[key] = value

    It saves the data on every write action onto the filesystem

    Attention: if you have two instances reading and writing to the same file it is possible to experience Issues.

    :param filename: this is the name of the pickled_dict (and the path)
    """

    def __init__(self, filename: PathLike = "dict.pkl", **kwargs):
        # should not be changed after creation
        self._filename = filename
        # without kwargs it loads the data from filename
        if kwargs:
            self.data = dict(kwargs)
            self._dump()
        else:
            self.data = self._load()

    def __str__(self):
        return self.data.__str__()

    def __repr__(self):
        return self.__class__.__name__ +  self.data.__repr__()

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        yield self.data.keys()

    def __getitem__(self, item):
        self._load()
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value
        self._dump()

    def __delitem__(self, key):
        del self.data[key]
        self._dump()

    def _load(self) -> dict:
        """
        gets called everytime something is loaded from the file
        :return:
        """
        tmp = {}
        try:
            with open(self._filename, 'rb') as fileobj:
                tmp = dict(pickle.load(fileobj))
        finally:
            print(tmp)
            return tmp

    def _dump(self) -> None:
        """
        is called to update the file object
        :return:
        """
        try:
            with open(self._filename, 'wb') as fileobj:
                pickle.dump(self.data, fileobj, protocol=pickle.HIGHEST_PROTOCOL)
        except PermissionError:
            print("Can't open the File")


if __name__ == '__main__':
    test_dict = {"help": 'me', "please": "i need this"}
    pd = PickledDict(**test_dict)
    pd["test"] = "world"
    pd["test"] = "test2"
    new_pd = PickledDict()
    new_pd["try"] = "me"
    # print(type(new_pd._load()))
    pd._load()
    print(pd.__repr__())
    #print(new_pd.__repr__())
