
import pytest


@pytest.mark.parametrize("dict, key, val", [
({},'ccc',3),
({'ccc':5}, 'ccc', 3),
({'aaa':12, 'vvv':13}, "ccc", 3)
])
def test_dict_add_set(dict, key, val):
    dict[key] = val
    assert dict[key] == val

def test_dict_remove():
    d = {'ccc':5}
    assert('ccc' in d)
    try:
        del d['zzz']
    except KeyError:
        pass
    else:
        assert False

def test_dict_count():
    d = {'ccc':5, 'ddd':3, 'ccc':5}
    count = 0
    for i in enumerate(d):
        count += 1
    assert len(d) == count

def test_set_add():
    testset = {1,2,3,4}
    assert 99 not in testset
    testset.add(99)
    assert 99 in testset

def test_set_uniquiness():
    testlist_from_set = list(set('hello'))

    for i in range(len(testlist_from_set)):
        for q in range(len(testlist_from_set)):
            assert(i==q or testlist_from_set[i] != testlist_from_set[q])

def test_set_copy():
    testset = {11, 19, 21}
    testset_copy = testset.copy()
    testset.add(99)

    assert 99 not in testset_copy
