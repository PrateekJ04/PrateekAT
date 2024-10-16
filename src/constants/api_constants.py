


class Api_Constants(object):

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def create_booking_url():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def create_auth_url():
        return "https://restful-booker.herokuapp.com/auth"

    @staticmethod
    def put_patch_delete_url(bookingid):
        return "https://restful-booker.herokuapp.com/booking/"+ str(bookingid)

