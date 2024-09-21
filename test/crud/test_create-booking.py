import allure
import pytest
from src.constants.api_constants import Api_Constants
from src.utils.utils import Utility
from src.helpers.api_request_wrapper import Api_Requests_Wrapper
from src.helpers.payload_manager import *
from src.helpers.common_verifications import *

readutils = Utility()
apiwrapper = Api_Requests_Wrapper()


class Test_Create_Booking(object):
    @pytest.mark.positive
    @allure.title("Verify if booking is getting created")
    @allure.description("Booking id should get created and status code should be 200")
    def test_create_booking(self):
        # URL, Payload, Headers

        response = apiwrapper.post_request(url=Api_Constants.create_booking_url(),
                                           headers=readutils.common_headers_put_delete_auth(
                                               basic_auth_value="YWRtaW46cGFzc3dvcmQxMjM="), auth=None,
                                           payload=dynamic_payload_create_booking(), in_json=False)
        booking_id = response.json()["bookingid"]
        verification_by_status_code(response_data=response.status_code, expected_data=200)
