import json
import os

def load_data(filename):
    path = os.path.join(os.path.dirname(__file__), filename)

    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(filename, data):
    path = os.path.join(os.path.dirname(__file__), filename)

    with open(path, "w") as f:
        json.dump(data, f, indent=4)