from ..python.functions import check_name

def test_check_name():
    assert check_name("Joe Blow")
    assert not check_name("thequickbrownfoxjumpedoverthelazydogs")
    assert not check_name("4")
    assert not check_name("!")
    assert not check_name(1)
