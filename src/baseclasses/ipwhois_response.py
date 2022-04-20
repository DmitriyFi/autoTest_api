from src.enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):                                # пишем конструктор класса, получающий на вход response
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):                                  # здесь происходит валидация нашей pydantic схемы
        if isinstance(self.response, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    def num_of_api_objects(self, number):
        assert len(self.response.json()) == number, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
        return self
