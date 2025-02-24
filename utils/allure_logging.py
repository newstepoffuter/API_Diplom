import allure
from allure_commons.types import AttachmentType
import logging
import json


class AllureMethods:
    def logging(self, response):
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)


allure_log = AllureMethods()
