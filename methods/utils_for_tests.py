from Data.data import Pet


class CheckData:
    def validate_pet_response(self, response_data: dict, expected_pet: Pet) -> bool:
        return (
                response_data['id'] == expected_pet.id
                and response_data['name'] == expected_pet.name
                and response_data['status'] == expected_pet.status
                and response_data['photoUrls'] == expected_pet.photoUrls
        )

    def find_pet_in_list(self, pet_list: list, expected_pet: Pet) -> bool:
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
        return (
                order_data['status'] == expected_status
                and order_data['complete'] == expected_complete
        )

    def validate_delete_response(self, delete_response: dict, expected_code: int, expected_message: str) -> bool:
        return (
                delete_response['code'] == expected_code
                and delete_response['message'] == expected_message
        )


make_checking_greate_again = CheckData()
