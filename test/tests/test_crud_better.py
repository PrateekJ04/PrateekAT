import allure
import pytest

# import pytest
from src.constants.api_constants import Api_Constants
from src.helpers.api_request_wrapper import Api_Requests_Wrapper
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Utility

readutils = Utility()
apiwrapper = Api_Requests_Wrapper()


# =============================================================================================================#
class Test_Crud_Better(object):

    @pytest.mark.crud_better
    @allure.title("Verify if booking is getting updated")
    @allure.description("Details of Booking Id should get updated")
    def test_put_booking(self, get_booking_id, get_token):
        response = apiwrapper.put_request(
            url=Api_Constants.put_patch_delete_url(bookingid=get_booking_id),
            headers=readutils.common_headers_put_delete_cookie(
                token=get_token),
            auth=None,
            payload=payload_update_booking(), in_json=False)

        verification_by_status_code(response_data=response.status_code, expected_data=200)

    # =============================================================================================================#
    @pytest.mark.crud_better
    @allure.title("Verify if booking is getting deleted")
    @allure.description("Details of Booking Id should get deleted")
    def test_delete_booking(self, get_booking_id, get_token):
        response = apiwrapper.delete_request(
            url=Api_Constants.put_patch_delete_url(bookingid=get_booking_id),
            auth=None,
            headers=readutils.common_headers_put_delete_cookie(token=get_token),
            in_json=False)
        verification_by_status_code(response_data=response.status_code, expected_data=201)

# =============================================================================================================#
