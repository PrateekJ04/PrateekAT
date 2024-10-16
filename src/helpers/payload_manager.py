import faker

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
        "firstname": "Miles",
        "lastname": "Morals",
        "totalprice": 112,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
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

