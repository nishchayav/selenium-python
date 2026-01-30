import pytest

# Function-scoped fixture (runs before each test)
@pytest.fixture(scope="function")
def numbers():
    return 10, 2


# Module-scoped fixture (runs once per file)
@pytest.fixture(scope="module")
def calculator_resource():
    print("\n[SETUP] Calculator resource initialized")
    yield
    print("\n[TEARDOWN] Calculator resource released")


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests against"
    )

import pytest

@pytest.fixture
def env(request):
    return request.config.getoption("--env")
