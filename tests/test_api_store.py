import allure
import pytest
from methods.api_metods import store_api_responses
from methods.utils_for_tests import make_checking_greate_again
from methods.utils import load_schema, validate_response


@allure.feature('API Store')
@allure.link('https://petstore.swagger.io/#/')
@allure.label('Store')
@allure.tag('api')
@allure.severity(allure.severity_level.CRITICAL)
class TestStoreAPI:
    @allure.story("Добавление заказа")
    @allure.description('Проверка добавления заказа')
    @pytest.mark.parametrize("expected_status, expected_complete", [
        ("placed", True),
    ])
    def test_post_store(self, setup_base_url, expected_status, expected_complete):
        response, response_json, expected_json, order_id = store_api_responses.create_order()
        schema = load_schema('post_store.json')
        validate_response(response, schema)
        assert make_checking_greate_again.check_status_order(
            response_json, expected_status, expected_complete
        ), f"Ожидался заказ со статусом {expected_status} и завершенностью {expected_complete}"

    @allure.story("Удаление заказа")
    @allure.description('Проверка удаления заказа')
    @pytest.mark.parametrize("expected_code, expected_message", [
        (200, "16"),
    ])
    def test_delete_order(self, setup_base_url, expected_code, expected_message):
        _, order_response_json, _, order_id = store_api_responses.create_order()
        response, response_json, _ = store_api_responses.delete_order(order_id)
        schema = load_schema('delete_store.json')
        validate_response(response, schema)
        assert make_checking_greate_again.check_delete_status_response(
            response_json, expected_code, expected_message
        ), f"Ожидался код {expected_code} и сообщение {expected_message}"
