"""
api keys - 

"""

import requests

url = "https://www.flickr.com/services/rest/"

parametrs = {
    "method":"flickr.photos.getPopular",
    "api_key":"40746a6e5f1a219afba59e859460b29f", #my personal api keys
    "user_id":"195482657@N02", #user id
    "format":"json",
    "nojsoncallback":1
}

r = requests.get(url=url, params=parametrs)

print(r.status_code)
json_response = r.json()
print(json_response)


if (r.status_code == 200 and json_response["stat"] == "ok" ):
    print("API Working")
else:
    print("Not Working")
    print("Error caught :-",json_response["message"])