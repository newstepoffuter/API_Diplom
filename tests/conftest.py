import pytest


@pytest.fixture()
def setup_base_url():
    request_base_url = 'https://petstore.swagger.io/v2/'
    return str(request_base_url)
