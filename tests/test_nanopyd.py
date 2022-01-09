from nanopyd import __version__, NanoID


def test_version():
    assert __version__ == "0.1.0"


def test_alphabet():
    nano = NanoID(alphabet="lowercase")
    assert nano.alphabet == "_-abcdefghijklmnopqrstuvwxyz"


def test_size():
    nano = NanoID(size=8)
    assert len(nano.value) == 8


def test_basic():
    nano = NanoID()
    assert nano.value is not None
