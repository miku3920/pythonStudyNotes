import json

path = __file__
path = path[:path.rfind('\\')][:path.rfind('/')]+'\\'

data = {
    'name': 'miku3920',
    'shares': 156,
    'price': 47.11
}

json_str = json.dumps(data)
print(json_str)
data = json.loads(json_str)
print(data)
print(data['name'])

with open(path+'data.json', 'w') as f:
    json.dump(data, f)

with open(path+'data.json', 'r') as f:
    data = json.load(f)
