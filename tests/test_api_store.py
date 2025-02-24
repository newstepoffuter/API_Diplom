from methods.api_metods import store_api_responses
from methods.utils_for_tests import make_checking_greate_again
from jsonschema import validate
import allure


@allure.feature('API post')
@allure.story("Добавление заказа")
@allure.link('https://petstore.swagger.io/#/')
@allure.description('Проверка добавления заказа')
@allure.label('Store')
@allure.tag('api')
@allure.severity(allure.severity_level.CRITICAL)
def test_post_store(setup_base_url):
    res = store_api_responses.post_store(setup_base_url)
    data_load = res[1]
    data_validate = res[2]
    with allure.step('Проверяем статус код'):
        assert res[0].status_code == 200, 'Код ответа не равен 200'
    with allure.step('Валидируем данные ответа'):
        validate(data_load, data_validate)
    with allure.step('Проверяем наличие тестовых данных в ответе'):
        make_checking_greate_again.check_status_order(data_load)


@allure.feature('API delete')
@allure.story("Удаление заказа")
@allure.link('https://petstore.swagger.io/#/')
@allure.description('Проверка удаления заказа')
@allure.label('Store')
@allure.tag('api')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_order(setup_base_url):
    order = store_api_responses.post_store(setup_base_url)
    res = store_api_responses.delete_store(setup_base_url, order[3])
    data_load = res[1]
    data_validate = res[2]
    with allure.step('Проверяем статус код'):
        assert res[0].status_code == 200, 'Код ответа не равен 200'
    with allure.step('Валидируем данные ответа'):
        validate(data_load, data_validate)
    with allure.step('Проверяем наличие тестовых данных в ответе'):
        make_checking_greate_again.check_delete_status_response(data_load, order[3])
