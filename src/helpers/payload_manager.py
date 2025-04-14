import faker
import openpyxl


from src.constants.api_constants import Api_Constants
from src.utils.utils import Utility
from src.helpers.api_request_wrapper import Api_Requests_Wrapper

readutils = Utility()
apiwrapper = Api_Requests_Wrapper()

fake = faker.Faker()


def payload_create_booking():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_update_booking():
    payload = {
        "firstname": fake.name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(100,1000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Lunch"
    }
    return payload


def dynamic_payload_create_booking():
    payload = {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=1500),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": fake.random_element(["Breakfast", "Lunch", "Parking"])
    }
    return payload


# def read_from_excel_data_create_booking():
#     payload = {
#         "firstname":"readdata",
#         "lastname": "readdata",
#         "totalprice": "readdata",
#         "depositpaid": "readdata",
#         "bookingdates": {
#             "checkin": "2018-01-01",
#             "checkout": "2019-01-01"
#         },
#         "additionalneeds": "readdata"
#     }
#     return payload


def create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload


def read_creds_from_excel(filepath):
    # filepath="src/resources/DDPytest_Read.XLSX"
    credentials = []
    workbook = openpyxl.load_workbook(filename=filepath)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append(({

            "username": username,
            "password": password

        }))

    return credentials


def create_auth_request(username, password):
    payload = {
        "username": username,
        "password": password

    }
    response = apiwrapper.post_request(url=Api_Constants.create_auth_url(), auth=None,
                                       headers=readutils.common_headers_json(),
                                       payload=payload,
                                       in_json=False)
    return response
