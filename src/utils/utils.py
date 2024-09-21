

class Utility(object):
    def common_headers_json(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    def common_headers_put_delete_auth(self,basic_auth_value):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic "+ str(basic_auth_value),

        }
        return headers

    def common_headers_put_delete_cookie(self,token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token),

        }
        return headers

    def read_csv_file(self):
        pass

        