import json

def read_json(filename):
    with open(f"jsonFiles\{filename}", "r") as file:
        file_data = json.load(file)
        file.close()

    return file_data

def stringify(json_to_encrypt):
    return json.dumps(json_to_encrypt)

def writeJson(file, jsonData):
    with open(f"jsonFiles\{file}", "w") as f:
        json.dumps
        json.dump(jsonData, f, indent=4)
        f.close()
