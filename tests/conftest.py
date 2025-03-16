import pytest
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.fixture()
def setup_base_url():
    request_base_url = os.getenv('BASE_URL')
    if not request_base_url:
        pytest.fail("Переменная окружения BASE_URL не установлена.")
    return request_base_url
