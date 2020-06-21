import pytest
from pickled_dict.PickledDict import PickledDict


@pytest.fixture()
def init_dict(tmpdir):
    pd = PickledDict(tmpdir / "dict.pkl")
    pd["test"] = 2
    return pd


@pytest.fixture()
def get_file_dict(tmpdir):
    return tmpdir / "dict.pkl"


def test_load(init_dict):
    pd = init_dict
    assert pd["test"] == 2


def test_set_data(init_dict, get_file_dict):
    pd = init_dict
    pd["new"] = "data"
    new_pd = PickledDict(get_file_dict)
    assert "data" == new_pd["new"]


def test_overwrite_data(init_dict, get_file_dict):
    pd = init_dict
    pd["test"] = 5
    new_pd = PickledDict(get_file_dict)
    assert 5 == new_pd["test"]
