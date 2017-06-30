import json


def load_test_json(filename):
    with open(filename, 'r') as f:
        data = f.read()
        return json.loads(data)


def save_test_json(filename, data):
    with open(filename, 'wb') as f:
        f.write(data.encode("utf-8"))
        return filename
