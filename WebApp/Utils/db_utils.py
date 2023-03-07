import requests
from requests.auth import HTTPBasicAuth
import json
class SurrealClient:

    def __init__(self, host, port, username, password, namespace, db):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.namespace = namespace
        self.db = db

    def query(self, data):
        headers = {"Accept":"application/json", "NS":self.namespace, "DB":self.db}
        response = requests.post(f"http://{self.host}:{self.port}/sql", headers=headers, auth=HTTPBasicAuth(self.username, self.password), data=data)
        return json.loads(response.text)



client = SurrealClient(
    host = "db",
    port = "8000",
    username = "root",
    password = "root",
    namespace = "test",
    db = "test"
    )