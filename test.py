import requests

class Test:
    def test(self):
        req = requests.get("http://localhost:8000/health")
        assert req.json()=={ "status": "oK" }
