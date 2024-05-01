import json

file_path = r"./rpc.json"

def read_variable_json(variable_name: str):
    """
    Helper function that will return the value of the given variable name.
    """
    global file_path
    try:
        with open(file_path, "r") as file:
            data = json.load(file)

        if variable_name in data:
            return data[variable_name]
    except Exception as e:
        print(f"Erreur while trying to read the rpc.json: {e}")


def edit_variable_json(variable_name: str, new_value):
    """
    Helper function that will edit the value of the given variable name to the given value.
    """
    global file_path
    with open(file_path, "r") as file:
        data = json.load(file)

    if variable_name in data:
        data[variable_name] = new_value

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)