class CheckData:
    def __init__(self):
        pass

    def check_data_load_pet_name_get_by_status(self, data_load):
        for i in data_load:
            if i['id'] == 16 and i['name'] == 'Alex':
                return True

    def check_data_load_pet_name_get_by_id(self, data_load):
        if data_load['id'] == 16 and data_load['name'] == 'Alex':
            return True

    def check_status_order(self, data_load):
        if data_load['status'] == 'placed' and data_load['complete'] is True:
            return True

    def check_delete_status_response(self, data_load, id_order):
        if data_load['code'] == 200 and data_load['message'] == id_order:
            return True


make_checking_greate_again = CheckData()
