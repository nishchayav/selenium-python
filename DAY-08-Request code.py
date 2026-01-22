import requests

BASE_URL = "http://127.0.0.1:5000"


# GET all users
res = requests.get(f"{BASE_URL}/users")
print(res.status_code, res.json())


# POST new user
res = requests.post(
    f"{BASE_URL}/users",
    json={"name": "Apple"}
)
print(res.status_code, res.json())


# PUT update
res = requests.put(
    f"{BASE_URL}/users/1",
    json={"name": "Apple Updated"}
)
print(res.status_code, res.json())


# PATCH update
res = requests.patch(
    f"{BASE_URL}/users/2",
    json={"name": "Vish Partial"}
)
print(res.status_code, res.json())


# DELETE user
res = requests.delete(f"{BASE_URL}/users/1")
print(res.status_code, res.json())





import requests

geturl="http://127.0.0.1:5000/users"


headers={
    "Accept":"application/json",
    "User-Agent":"Python-Requests-Client"

}
response=requests.get(geturl,headers=headers,timeout=10)

print("get status code",response.status_code)
print(response.json())

posturl="http://127.0.0.1:5000/users"

body1={
    "name":"leena"
}

r1=requests.post(posturl,json=body1);
print("post status code",r1.status_code)
print(r1.json())
 