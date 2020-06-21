import pytest
from pickled_dict.PickledDict2 import PickledDict2

@pytest.fixture()
def init_dict(tmpdir):
    pd = PickledDict2(tmpdir / "dict.dat")
    pd["test"] = [1,2,3,4]
    pd._dump()
    return pd

def test_sync():
    assert False


def test_load(init_dict):
    pd = init_dict
    assert pd["test"][1] == 2

def test_dump():
    assert False


def test__available():
    assert False
