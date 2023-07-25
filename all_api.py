import requests
url = "	https://wsp.kbtu.kz/ScheduleTeacherStudent/APP/connector/"
response = requests.get(url, verify=False)
# api_list = response.json()

print(response.status_code)
print(response.headers["content-type"])

# for api in api_list:
#     # api_url = url + api
#     # response = requests.get(api_url)
#     # api_details = response.json()

#     print(api)
#     # do something with the API details

# if (
#     response.status_code != 204 and
#     response.headers["content-type"].strip().startswith("application/json")
# ):
#     try:
#         return response.json()
#     except ValueError:
#         # decide how to handle a server that's misbehaving to this extent