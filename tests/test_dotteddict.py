from dotteddict import dotteddict

def test_single_level_dots():
    d = dotteddict({'key': 'value'})
    assert(d.key == 'value')

def test_multi_level_dots():
    d = dotteddict({'root': {'leaf': 'value'}})
    assert(d.root.leaf == 'value')

def test_single_level_set():
    d = dotteddict()
    d.key = 'value'
    assert(d.key == 'value')

def test_multi_level_set():
    d = dotteddict()
    d['root.leaf'] = 'value'
    assert(d.root.leaf == 'value')
