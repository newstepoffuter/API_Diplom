import allure
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
    def test_post_store(self, setup_base_url):
        response, data_load, data_validate, id_order = store_api_responses.create_order()
        schema = load_schema('post_store.json')
        validate_response(response, schema)
        expected_status = data_load['status']
        expected_complete = data_load['complete']
        assert make_checking_greate_again.check_status_order(
            data_load, expected_status, expected_complete
        ), f"Ожидался заказ со статусом {expected_status} и завершенностью {expected_complete}"

    @allure.story("Удаление заказа")
    @allure.description('Проверка удаления заказа')
    def test_delete_order(self, setup_base_url):
        order_response, order_data_load, order_data_validate, order_id = store_api_responses.create_order()
        response, data_load, data_validate = store_api_responses.delete_order(order_id)
        schema = load_schema('delete_store.json')
        validate_response(response, schema)
        expected_code = 200
        expected_message = str(order_id)
        assert make_checking_greate_again.check_delete_status_response(
            data_load, expected_code, expected_message
        ), f"Ожидался код {expected_code} и сообщение {expected_message}"
