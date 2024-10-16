import allure
import pytest
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *

readutils = Utility()
apiwrapper = Api_Requests_Wrapper()


@pytest.mark.datadriven
@allure.title("Verify if user is able to Log in")
@allure.description("User should be able to logged in successfully")
def test_create_auth_with_excel():
    file_path = "C:\\Users\\prate\\PycharmProjects\\APIAutoFRMWK\\src\\resources\\exceldata.XLSX"
    credentials = read_creds_from_excel(filepath=file_path)
    print(credentials)
    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]

    response = create_auth_request(username=username, password=password)
    global tkn
    tkn = response.json()['token']
    print(response.json()['token'])
    verification_by_status_code(response_data=response.status_code, expected_data=200)
    return tkn


# ==============================================================================================================================


@pytest.mark.datadriven
@allure.title("Verify if booking is getting created")
@allure.description("Booking id should get created and status code should be 200")
def test_create_booking():
    # URL, Payload, Headers

    response = apiwrapper.post_request(url=Api_Constants.create_booking_url(),
                                       headers=readutils.common_headers_put_delete_auth(
                                           basic_auth_value="YWRtaW46cGFzc3dvcmQxMjM="), auth=None,
                                       payload=dynamic_payload_create_booking(), in_json=False)
    global booking_id
    booking_id = response.json()["bookingid"]
    print(f"Booking id is: {booking_id}")
    verification_by_status_code(response_data=response.status_code, expected_data=200)
    return booking_id


# ==================================================================================================================================
@pytest.mark.datadriven
@allure.title("Verify if booking is getting deleted")
@allure.description("Details of Booking Id should get deleted")
def test_delete_booking():
    response = apiwrapper.delete_request(
        url=Api_Constants.put_patch_delete_url(bookingid=booking_id),
        auth=None,
        headers=readutils.common_headers_put_delete_cookie(token=tkn),
        in_json=False)
    print(response.status_code)
    verification_by_status_code(response_data=response.status_code, expected_data=201)
