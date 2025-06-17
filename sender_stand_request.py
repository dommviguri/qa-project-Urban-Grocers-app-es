#mi primer automatización de pruebas uwu

import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)
auth_token = (response.json())['authToken']
print(auth_token)

headers_2 = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer [auth_token]'
}

def post_new_client_kit(kit_body):
        return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=headers_2)
response_2 = post_new_client_kit(data.kit_body);
print(response.status_code)
print(response.json())


