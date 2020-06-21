import pickle, os, shutil
from collections.abc import MutableMapping
from os import PathLike


class PickledDict2(MutableMapping):
    def __init__(self, *args, filename: PathLike = "dict.pkl", **kwargs):
        self.filename = filename
        # without args and kwargs it loads the data from filename
        if not (args and kwargs):
            self.data = self._load()
        else:
            self.data = dict(*args, **kwargs)
            self._dump()

    def __str__(self):
        return self.data.__str__()

    def __repr__(self):
        return self.data.__repr__()

    def __len__(self):
        return len(self.keys())

    def __iter__(self):
        yield self.data.keys()

    def __getitem__(self, item):
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
            with open(self.filename, 'rb') as fileobj:
                tmp = dict(pickle.load(fileobj))
        finally:
            return tmp

    def _dump(self) -> None:
        """
        is called to update the file object
        :return:
        """
        try:
            with open(self.filename, 'wb') as fileobj:
                pickle.dump(self.data, fileobj, protocol=pickle.HIGHEST_PROTOCOL)
        except PermissionError:
            print("Can't open the File")


if __name__ == '__main__':
    pd = PickledDict2()
    pd["test"] = "world"
    pd._dump()
    new_pd = PickledDict2()
    print(type(new_pd._load()))
    print(pd.__repr__())
