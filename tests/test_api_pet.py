from methods.api_metods import pet_api_responses
from methods.utils_for_tests import make_checking_greate_again
from jsonschema import validate
import allure


@allure.feature('API post')
@allure.story("Добавление питомца")
@allure.link('https://petstore.swagger.io/#/')
@allure.description('Проверка добавления питомца')
@allure.label('Pet')
@allure.tag('api')
@allure.severity(allure.severity_level.CRITICAL)
def test_post_pet(setup_base_url):
    res = pet_api_responses.post_pet(setup_base_url)
    data_load = res[1]
    data_validate = res[2]
    with allure.step('Проверяем статус код'):
        assert res[0].status_code == 200, 'Код ответа не равен 200'
    with allure.step('Валидируем данные ответа'):
        validate(data_load, data_validate)
    with allure.step('Проверяем наличие тестовых данных в ответе'):
        make_checking_greate_again.check_data_load_pet_name_get_by_id(data_load)


@allure.feature('API get')
@allure.story("Вывод списка питомцев по статусу")
@allure.link('https://petstore.swagger.io/#/')
@allure.description('Проверка поиска питомца по статусу')
@allure.label('Pet')
@allure.tag('api')
@allure.severity(allure.severity_level.CRITICAL)
def test_pet_find_by_status(setup_base_url):
    pet_api_responses.post_pet(setup_base_url)
    res = pet_api_responses.pet_find_by_status_get(setup_base_url)
    data_load = res[1]
    data_validate = res[2]
    with allure.step('Проверяем статус код'):
        assert res[0].status_code == 200, 'Код ответа не равен 200'
    with allure.step('Валидируем данные ответа'):
        validate(data_load, data_validate)
    with allure.step('Проверяем наличие тестовых данных в ответе'):
        make_checking_greate_again.check_data_load_pet_name_get_by_status(data_load)


@allure.feature('API get')
@allure.story("Поиск питомца по id")
@allure.link('https://petstore.swagger.io/#/')
@allure.description('Проверка поиска питомца по id')
@allure.label('Pet')
@allure.tag('api')
@allure.severity(allure.severity_level.CRITICAL)
def test_pet_find_by_id(setup_base_url):
    pet_api_responses.post_pet(setup_base_url)
    res = pet_api_responses.pet_id_get(setup_base_url, 16)
    data_load = res[1]
    data_validate = res[2]
    with allure.step('Проверяем статус код'):
        assert res[0].status_code == 200, 'Код ответа не равен 200'
    with allure.step('Валидируем данные ответа'):
        validate(data_load, data_validate)
    with allure.step('Проверяем наличие тестовых данных в ответе'):
        make_checking_greate_again.check_data_load_pet_name_get_by_id(data_load)
