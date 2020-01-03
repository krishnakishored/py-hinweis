# content of test_foobar.py
import pytest
from foobar import foo, bar
import sys

# conditional skipif
@pytest.mark.skipif(
    sys.version_info[0] == 3 and sys.version_info[1] == 6,
    reason="Python version has to be higher than 3.5!")
# @pytest.mark.crazy
def test_foo():
    assert foo() == "foo"


@pytest.mark.crazy
# unconditional skipif
@pytest.mark.skip(reason="Even fooer than foo, so we skip!")
def test_bar():
    assert bar() == "bar"