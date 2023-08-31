'''
  A partir de agora vou tentar enviar dados
do servidor flask, porta 5000,
pro servidor express, porta 5600.
'''
import requests

data = {
  "info": "Luis",
  "value": 255,
}
# To JavaScript
request = requests.post("http://127.0.0.1:5600/teste", json=data)
print(f"Answer: {request}")
print(f"Answer text: {request.text}")
print(f"Answer status code: {request.status_code}")
# To Python
request = requests.post("http://127.0.0.1:5000/teste", json=data)
print(f"Answer: {request}")
print(f"Answer text: {request.text}")
print(f"Answer status code: {request.status_code}")
