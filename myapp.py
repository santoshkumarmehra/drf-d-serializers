import requests
import json

url="http://127.0.0.1:8000/stucreate/"

data = {'name':'sonam', 'roll':100, 'city':'jaipur'}
json_data = json.dumps(data)
r = requests.post(url=url, data=json_data)
revert_data = r.json()
print(revert_data)

