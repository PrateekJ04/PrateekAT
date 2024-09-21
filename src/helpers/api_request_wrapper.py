import requests
import json

class Api_Requests_Wrapper():
    def get_request(self, url, auth):
        get_response= requests.get(url=url,auth=auth)
        return get_response.json()

    def post_request(self,url, auth, headers, payload, in_json):
        post_response= requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
        if in_json is True:
            return post_response.json()
        return post_response

    def patch_request(self,url, auth, headers, payload, in_json):
        patch_response= requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
        if in_json is True:
            return patch_response.json()
        return patch_response

    def put_request(self,url, auth, headers, payload, in_json):
        put_response= requests.put(url=url, auth=auth, headers=headers, data=json.dumps(payload))
        if in_json is True:
            return put_response.json()
        return put_response

    def delete_request(self,url, auth, headers, in_json):
        delete_response= requests.delete(url=url, auth=auth, headers=headers)
        if in_json is True:
            return delete_response.json()
        return delete_response