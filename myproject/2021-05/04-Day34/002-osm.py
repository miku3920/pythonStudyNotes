import osmapi
api = osmapi.OsmApi()
print(api.NodeGet(123))

username = "????????@gmail.com"
password = "????????"

api = osmapi.OsmApi(api="https://api06.dev.openstreetmap.org",
                    username=username, 
                    password=password)

api.ChangesetCreate({"comment": "My first test"})
print(api.NodeCreate({"lon": 1, "lat": 1, "tag": {}}))
api.ChangesetClose()
