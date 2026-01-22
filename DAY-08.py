import requests

geturl= "https://api.restful-api.dev/objects"

getres = requests.get(geturl)

print(getres.status_code)
print(getres.json())





posturl="https://api.restful-api.dev/objects"

postbody={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

postres=requests.post(posturl,json=postbody);
print(postres.status_code)
print(postres.json())







puturl="https://api.restful-api.dev/objects/7"

putbody={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}

putres=requests.put(puturl,json=putbody);
print(putres.status_code)
print(putres.json())




patchurl="https://api.restful-api.dev/objects/7"

patchbody={
   "name": "Apple MacBook Pro 16 (Updated Name)"
}

patchres=requests.patch(patchurl,json=patchbody);
print(patchres.status_code)
print(patchres.json())






delurl="https://api.restful-api.dev/objects/6"


delres=requests.delete(delurl)
print(delres.status_code)
print(delres.json())