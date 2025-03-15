import allure
from methods.api_metods import pet_api_responses
from methods.utils_for_tests import make_checking_greate_again
from methods.utils import load_schema, validate_response


@allure.feature('API Pet')
@allure.link('https://petstore.swagger.io/#/')
@allure.label('Pet')
@allure.tag('api')
@allure.severity(allure.severity_level.CRITICAL)
class TestPetAPI:
    @allure.story("Добавление питомца")
    @allure.description('Проверка добавления питомца')
    def test_post_pet(self, setup_base_url):
        response, data_load, data_validate = pet_api_responses.create_pet()
        schema = load_schema('post_pet.json')
        validate_response(response, schema)
        expected_id = data_load['id']
        expected_name = data_load['name']
        assert make_checking_greate_again.check_data_load_pet_name_get_by_id(
            data_load, expected_id, expected_name
        ), f"Ожидался питомец с id={expected_id} и name={expected_name}"

    @allure.story("Вывод списка питомцев по статусу")
    @allure.description('Проверка поиска питомца по статусу')
    def test_pet_find_by_status(self, setup_base_url):
        pet_api_responses.create_pet()
        response, data_load, data_validate = pet_api_responses.find_pet_by_status()
        schema = load_schema('get_by_status.json')
        validate_response(response, schema)
        expected_id = data_load[0]['id']
        expected_name = data_load[0]['name']
        assert make_checking_greate_again.check_data_load_pet_name_get_by_status(
            data_load, expected_id, expected_name
        ), f"Ожидался питомец с id={expected_id} и name={expected_name}"

    @allure.story("Поиск питомца по id")
    @allure.description('Проверка поиска питомца по id')
    def test_pet_find_by_id(self, setup_base_url):
        pet_api_responses.create_pet()
        response, data_load, data_validate = pet_api_responses.get_pet_by_id(pet_id=16)
        schema = load_schema('get_by_id.json')
        validate_response(response, schema)
        expected_id = data_load['id']
        expected_name = data_load['name']
        assert make_checking_greate_again.check_data_load_pet_name_get_by_id(
            data_load, expected_id, expected_name
        ), f"Ожидался питомец с id={expected_id} и name={expected_name}"
