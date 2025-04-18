import allure
import pytest
from src.constants.api_constants import Api_Constants
from src.utils.utils import Utility
from src.helpers.api_request_wrapper import Api_Requests_Wrapper
from src.helpers.payload_manager import *
from src.helpers.common_verifications import *

readutils = Utility()
apiwrapper = Api_Requests_Wrapper()

#This reference to create token for further requests
@pytest.fixture(scope="session")
def get_token():
    response = apiwrapper.post_request(url=Api_Constants.create_auth_url(), auth=None,
                                       headers=readutils.common_headers_json(),
                                       payload=create_token(),
                                       in_json=False)
    tkn = response.json()["token"]
    return tkn

#This get_booking_id reference to basic auth
@pytest.fixture(scope="session")
def get_booking_id():
    # URL, Payload, Headers

    response = apiwrapper.post_request(url=Api_Constants.create_booking_url(),
                                       headers=readutils.common_headers_put_delete_auth(
                                           basic_auth_value="YWRtaW46cGFzc3dvcmQxMjM="), auth=None,
                                       payload=dynamic_payload_create_booking(), in_json=False)
    booking_id = response.json()["bookingid"]
    return booking_id
