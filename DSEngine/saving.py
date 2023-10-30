import json

def save(filename: str, data: dict):
  y = json.dumps(data)
  with open(filename, "w+") as f:
    f.write(y)
  return None

def load(filename: str):
  with open(filename, "r+") as f:
    raw_data = f.read()
  data = json.loads(raw_data)
  return data
