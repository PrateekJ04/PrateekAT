import allure
import pytest
from src.constants.api_constants import Api_Constants
from src.utils.utils import Utility
from src.helpers.api_request_wrapper import Api_Requests_Wrapper
from src.helpers.payload_manager import *
from src.helpers.common_verifications import *
# from test.crud import Test_Create_Booking
readutils = Utility()
apiwrapper = Api_Requests_Wrapper()


class Test_Update_Booking(object):
    @pytest.mark.positive
    @allure.title("Verify if booking is getting updated")
    @allure.description("Details of Booking Id should get updated")
    def test_create_booking(self):
        # URL, Payload, Headers

        response = apiwrapper.put_request(url=Api_Constants.put_patch_delete_url(bookingid=974),
                                          headers=readutils.common_headers_put_delete_auth(
                                              basic_auth_value="YWRtaW46cGFzc3dvcmQxMjM="), auth=None,
                                          payload=payload_update_booking(), in_json=False)

        verification_by_status_code(response_data=response.status_code, expected_data=405)
