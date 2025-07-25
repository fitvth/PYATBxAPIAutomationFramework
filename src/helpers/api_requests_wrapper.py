# Pre-built methods for get, post, put, patch , delete request

# response_data_booking_id=requests.put(url=full_url_booking_id,headers=headers,json=payload)

# response_data_booking_id=requests.get(url=full_url_booking_id)

import json
import requests

def get_request(url,auth):
    response=requests.get(url=url,auth=auth)
    return response.json()

def post_request(url,auth,headers,payload,in_json):
    post_response = requests.post(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json:
        return post_response.json()
    return post_response

def put_request(url,auth,headers,payload,in_json):
    put_response = requests.post(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json:
        return put_response.json()
    return put_response

def patch_request(url,auth,headers,payload,in_json):
    patch_response = requests.post(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json:
        return patch_response.json()
    return patch_response

def delete_request(url,auth,headers,in_json):
    delete_response=requests.delete(url=url,auth=auth,headers=headers)
    if in_json:
        return delete_response.json()
    return delete_response


