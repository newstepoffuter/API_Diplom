import json
from pathlib import Path
from jsonschema.exceptions import ValidationError
import tests
from jsonschema import validate
import allure
from allure_commons.types import AttachmentType
import logging


def load_schema(file_name):
    schema_path = Path(tests.__file__).parent.parent.joinpath(f'json/schema/{file_name}')
    with open(schema_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def validate_response_schema(response, schema):
    allure.attach(
        body=json.dumps(response.json(), indent=4, ensure_ascii=True),
        name="Response",
        attachment_type=AttachmentType.JSON,
        extension="json"
    )
    logging.info(f"Response URL: {response.request.url}")
    logging.info(f"Response Status Code: {response.status_code}")
    logging.info(f"Response Body: {response.text}")
    try:
        validate(instance=response.json(), schema=schema)
        logging.info("Валидация прошла успешно.")
    except ValidationError as e:
        logging.error(f"Ошибка валидации: {e.message}")
        allure.attach(
            body=str(e),
            name="Validation Error",
            attachment_type=AttachmentType.TEXT,
            extension="txt"
        )
        raise e