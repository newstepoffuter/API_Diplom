class CheckData:
    def check_data_load_pet_name_get_by_status(self, data_load, expected_id, expected_name):
        for item in data_load:
            if item['id'] == expected_id and item['name'] == expected_name:
                return True
        return False

    def check_data_load_pet_name_get_by_id(self, data_load, expected_id, expected_name):
        return data_load['id'] == expected_id and data_load['name'] == expected_name

    def check_status_order(self, data_load, expected_status, expected_complete):
        return data_load['status'] == expected_status and data_load['complete'] == expected_complete

    def check_delete_status_response(self, data_load, expected_code, expected_message):
        return data_load['code'] == expected_code and data_load['message'] == expected_message


# Создаем экземпляр класса
make_checking_greate_again = CheckData()
