import allure
import pytest
from methods.api_metods import store_api_responses
from methods.utils_for_tests import make_checking_greate_again
from methods.utils import load_schema, validate_response_schema


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
        validate_response_schema(response, schema)
        assert make_checking_greate_again.validate_order_status(
            response_json, expected_status, expected_complete
        ), f"Ожидался заказ со статусом {expected_status} и завершенностью {expected_complete}"

    @allure.story("Удаление заказа")
    @allure.description('Проверка удаления заказа')
    def test_delete_order(self, setup_base_url):
        _, _, _, order_id = store_api_responses.create_order()
        response, response_json, _ = store_api_responses.delete_order(order_id)
        assert response.status_code == 200
        assert response_json['code'] == 200
        assert str(order_id) in response_json['message']