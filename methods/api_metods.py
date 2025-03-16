import requests
import json
import allure
from path import path_resources, path_schemas
from utils.allure_logging import allure_log


class PetAPI:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')

    def _make_request(self, method, endpoint, params=None, json_data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, params=params, json=json_data)
        allure_log.logging(response)
        return response

    def find_pet_by_status(self, status='available'):
        response = self._make_request('GET', 'pet/findByStatus', params={'status': status})
        with open(path_schemas('get_by_status.json')) as file:
            expected_json = json.load(file)  # Схема для валидации
        with allure.step('Получение ответа метода pet.findByStatus'):
            response_json = response.json()  # JSON-ответ от API
        return response, response_json, expected_json

    def get_pet_by_id(self, pet_id):
        response = self._make_request('GET', f'pet/{pet_id}')
        with open(path_schemas('get_by_id.json')) as file:
            expected_json = json.load(file)  # Схема для валидации
        with allure.step('Получение ответа метода get.pet'):
            response_json = response.json()  # JSON-ответ от API
        return response, response_json, expected_json

    def create_pet(self):
        with open(path_resources('post_pet.json')) as file:
            data_upload = json.load(file)  # Данные для создания питомца
        response = self._make_request('POST', 'pet', json_data=data_upload)
        with open(path_schemas('post_pet.json')) as file:
            expected_json = json.load(file)  # Схема для валидации
        with allure.step('Получение ответа метода post.pet'):
            response_json = response.json()  # JSON-ответ от API
        return response, response_json, expected_json


class StoreAPI:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')

    def _make_request(self, method, endpoint, params=None, json_data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, params=params, json=json_data)
        allure_log.logging(response)
        return response

    def create_order(self):
        with open(path_resources('post_store.json')) as file:
            data_upload = json.load(file)  # Данные для создания заказа
        response = self._make_request('POST', 'store/order', json_data=data_upload)
        with allure.step('Получение ответа метода post.order'):
            response_json = response.json()  # JSON-ответ от API
        order_id = response_json["id"]  # ID созданного заказа
        with open(path_schemas('post_store.json')) as file:
            expected_json = json.load(file)  # Схема для валидации
        return response, response_json, expected_json, order_id

    def delete_order(self, order_id):
        response = self._make_request('DELETE', f'store/order/{order_id}')
        with allure.step('Получение ответа метода delete.order'):
            response_json = response.json()  # JSON-ответ от API
        with open(path_schemas('delete_store.json')) as file:
            expected_json = json.load(file)  # Схема для валидации
        return response, response_json, expected_json


# Создаем экземпляры классов с базовым URL
pet_api_responses = PetAPI(base_url='https://petstore.swagger.io/v2/')
store_api_responses = StoreAPI(base_url='https://petstore.swagger.io/v2/')