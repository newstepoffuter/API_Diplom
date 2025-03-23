from Data.data import Pet


class CheckData:
    def validate_pet_response(self, response_data: dict, expected_pet: Pet) -> bool:
        """
        Проверяет, что данные питомца в ответе API соответствуют ожидаемым.
        :param response_data: Данные питомца из ответа API.
        :param expected_pet: Ожидаемый питомец (объект Pet).
        :return: True, если данные совпадают, иначе False.
        """
        return (
                response_data['id'] == expected_pet.id
                and response_data['name'] == expected_pet.name
                and response_data['status'] == expected_pet.status
                and response_data['photoUrls'] == expected_pet.photoUrls
        )

    def find_pet_in_list(self, pet_list: list, expected_pet: Pet) -> bool:
        """
        Проверяет, что в списке питомцев есть объект с ожидаемыми данными.
        :param pet_list: Список питомцев (JSON-ответ от API).
        :param expected_pet: Ожидаемый питомец (объект Pet).
        :return: True, если питомец найден, иначе False.
        """
        for pet in pet_list:
            if (
                    pet['id'] == expected_pet.id
                    and pet['name'] == expected_pet.name
                    and pet['status'] == expected_pet.status
                    and pet['photoUrls'] == expected_pet.photoUrls
            ):
                return True
        return False

    def validate_order_status(self, order_data: dict, expected_status: str, expected_complete: bool) -> bool:
        """
        Проверяет, что статус и завершенность заказа соответствуют ожидаемым.
        :param order_data: Данные заказа из ответа API.
        :param expected_status: Ожидаемый статус заказа.
        :param expected_complete: Ожидаемая завершенность заказа.
        :return: True, если данные совпадают, иначе False.
        """
        return (
                order_data['status'] == expected_status
                and order_data['complete'] == expected_complete
        )

    def validate_delete_response(self, delete_response: dict, expected_code: int, expected_message: str) -> bool:
        """
        Проверяет, что код и сообщение в ответе на удаление соответствуют ожидаемым.
        :param delete_response: Ответ на удаление (JSON-ответ от API).
        :param expected_code: Ожидаемый код ответа.
        :param expected_message: Ожидаемое сообщение.
        :return: True, если данные совпадают, иначе False.
        """
        return (
                delete_response['code'] == expected_code
                and delete_response['message'] == expected_message
        )


# Создаем экземпляр класса
make_checking_greate_again = CheckData()
