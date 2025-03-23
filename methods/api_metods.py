import requests
import json
import allure
from Data.data import Pet
from path import path_resources, path_schemas
from utils.allure_logging import allure_log


class BaseAPI:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')

    def _make_request(self, method, endpoint, params=None, json_data=None):
        """
        Выполняет HTTP-запрос и возвращает ответ.
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, params=params, json=json_data)
        allure_log.logging(response)
        return response

    def _validate_response(self, response, schema_file):
        """
        Валидирует ответ API по схеме и возвращает JSON-ответ.
        """
        with open(path_schemas(schema_file)) as file:
            expected_json = json.load(file)
        with allure.step(f'Получение ответа метода {schema_file}'):
            response_json = response.json()
        return response, response_json, expected_json

    def _load_data(self, data_file):
        """
        Загружает данные из JSON-файла.
        """
        with open(path_resources(data_file)) as file:
            return json.load(file)


class PetAPI(BaseAPI):
    def __init__(self, base_url):
        super().__init__(base_url)

    def find_pet_by_status(self, status='available'):
        response = self._make_request('GET', 'pet/findByStatus', params={'status': status})
        return self._validate_response(response, 'get_by_status.json')

    def get_pet_by_id(self, pet_id):
        response = self._make_request('GET', f'pet/{pet_id}')
        return self._validate_response(response, 'get_by_id.json')

    def create_pet(self):
        data_upload = self._load_data('post_pet.json')
        response = self._make_request('POST', 'pet', json_data=data_upload)
        response, response_json, _ = self._validate_response(response, 'post_pet.json')
        pet = Pet(
            id=response_json['id'],
            name=response_json['name'],
            status=response_json['status'],
            photoUrls=response_json['photoUrls'],
            category=response_json.get('category'),
            tags=response_json.get('tags')
        )
        return response, pet


class StoreAPI(BaseAPI):
    def __init__(self, base_url):
        super().__init__(base_url)

    def create_order(self):
        data_upload = self._load_data('post_store.json')  # Загружаем данные для создания заказа
        response = self._make_request('POST', 'store/order', json_data=data_upload)
        response, response_json, expected_json = self._validate_response(response, 'post_store.json')
        order_id = response_json["id"]  # Получаем ID созданного заказа
        return response, response_json, expected_json, order_id

    def delete_order(self, order_id):
        response = self._make_request('DELETE', f'store/order/{order_id}')
        return self._validate_response(response, 'delete_store.json')


# Создаем экземпляры классов с базовым URL
pet_api_responses = PetAPI(base_url='https://petstore.swagger.io/v2/')
store_api_responses = StoreAPI(base_url='https://petstore.swagger.io/v2/')
