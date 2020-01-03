import pytest

def pytest_addoption(parser):
    parser.addoption("--cmdopt",
                    action="store",
                    default = "full",
                    help = "'num' of tests or full")

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")
