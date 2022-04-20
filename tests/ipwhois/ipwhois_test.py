from src.baseclasses.ipwhois_response import Response
from src.schemas.ipwhois_schema import Atributes_Ip


def test_ipwhois_check_status_code_and_data(get_api_attributes):
    test_object = Response(get_api_attributes)
    test_object.assert_status_code(200).num_of_api_objects(29).validate(Atributes_Ip)



