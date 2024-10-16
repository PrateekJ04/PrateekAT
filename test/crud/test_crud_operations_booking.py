import allure
import pytest

# import pytest
from src.constants.api_constants import Api_Constants
from src.utils.utils import Utility
from src.helpers.api_request_wrapper import Api_Requests_Wrapper
from src.helpers.payload_manager import *
from src.helpers.common_verifications import *

readutils = Utility()
apiwrapper = Api_Requests_Wrapper()


class Test_Crud_Booking(object):
    @pytest.mark.crud
    @allure.title("Verify if user is able to Log in")
    @allure.description("User should be able to logged in successfully")
    def test_create_token(self):
        response = apiwrapper.post_request(url=Api_Constants.create_auth_url(), auth=None,
                                           headers=readutils.common_headers_json(),
                                           payload=create_token(),
                                           in_json=False)
        global tkn
        tkn = response.json()["token"]
        print(tkn)

    @pytest.mark.crud
    @allure.title("Verify if booking is getting Created")
    @allure.description("Details of Booking Id should get Created")
    def test_get_booking_id(self):
        response = apiwrapper.post_request(url=Api_Constants.create_booking_url(),
                                           headers=readutils.common_headers_put_delete_cookie(
                                               token=tkn), auth=None,
                                           payload=dynamic_payload_create_booking(), in_json=False)
        global booking_id
        booking_id = response.json()["bookingid"]
        print(f"Booking id is: {booking_id}")
        verification_by_status_code(response_data=response.status_code, expected_data=200)
        return booking_id

    # Update Booking
    @pytest.mark.crud
    @allure.title("Verify if booking is getting updated")
    @allure.description("Details of Booking Id should get updated")
    def test_put_booking(self):
        response = apiwrapper.put_request(
            url=Api_Constants.put_patch_delete_url(bookingid=booking_id),
            headers=readutils.common_headers_put_delete_cookie(
                token=tkn), auth=None,
            payload=payload_update_booking(), in_json=False)

        verification_by_status_code(response_data=response.status_code, expected_data=200)

    # @allure.title("Verify if bookingid are getting fetched")
    # @allure.description("Details of Booking Ids should get fetched and displayed")
    # def test_read_booking(self):
    #     response = apiwrapper.get_request(
    #         url=Api_Constants.create_booking_url(),
    #         auth=None,
    #         headers=readutils.common_headers_put_delete_cookie(token=Test_Crud_Booking.test_create_token()),
    #         in_json=False),
    #     fetch_booking_ids = response.json["bookingid"]
    #     print(fetch_booking_ids)
    #     verification_by_status_code(response_data=response.status_code, expected_data=200)
    #     return fetch_booking_ids
    @pytest.mark.crud
    @allure.title("Verify if booking is getting deleted")
    @allure.description("Details of Booking Id should get deleted")
    def test_delete_booking(self):
        response = apiwrapper.delete_request(
            url=Api_Constants.put_patch_delete_url(bookingid=booking_id),
            auth=None,
            headers=readutils.common_headers_put_delete_cookie(token=tkn),
            in_json=False)