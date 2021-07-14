from requests import Response
import json
class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"REsponse is not in JSON format. Responsee text '{response.text}"
        assert name in response_as_dict, f"Ressponse doesnt have '{name}"
        assert response_as_dict[name] == expected_value, error_message
