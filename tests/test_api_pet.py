import allure
from methods.api_metods import pet_api_responses
from methods.utils_for_tests import make_checking_greate_again
from methods.utils import load_schema, validate_response_schema
from Data.data import Pet


@allure.feature('API Pet')
@allure.link('https://petstore.swagger.io/#/')
@allure.label('Pet')
@allure.tag('api')
@allure.severity(allure.severity_level.CRITICAL)
class TestPetAPI:
    @allure.story("Добавление питомца")
    @allure.description('Проверка добавления питомца')
    def test_post_pet(self, setup_base_url):
        expected_pet = Pet(
            id=16,
            name="Alex",
            status="available",
            photoUrls=["string"]
        )
        response, created_pet = pet_api_responses.create_pet()
        schema = load_schema('post_pet.json')
        validate_response_schema(response, schema)
        assert make_checking_greate_again.validate_post_pet_response(
            expected_pet, created_pet
        ), f"Ожидался питомец с id={expected_pet.id}, name={expected_pet.name}, status={expected_pet.status}, photoUrls={expected_pet.photoUrls}"

    @allure.story("Вывод списка питомцев по статусу")
    @allure.description('Проверка поиска питомца по статусу')
    def test_pet_find_by_status(self, setup_base_url):
        expected_pet = Pet(
            id=16,
            name="Alex",
            status="available",
            photoUrls=["string"]
        )
        pet_api_responses.create_pet()
        response, response_json, _ = pet_api_responses.find_pet_by_status()
        schema = load_schema('get_by_status.json')
        validate_response_schema(response, schema)
        assert make_checking_greate_again.check_data_load_pet_name_get_by_status(
            response_json, expected_pet
        ), f"Ожидался питомец с id={expected_pet.id} и name={expected_pet.name}"
