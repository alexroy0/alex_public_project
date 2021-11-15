from alex_public_project.lib import try_me


def test_type_return():
    assert isinstance(try_me(), str)
