import json

def verify_input_json(file_path):
    # Check if the file has a JSON extension
    if not file_path.lower().endswith('.json'):
        print(f"File '{file_path}' is not a JSON file.")
        return False

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

            # Ensure the required fields exist
            if "PolicyDocument" not in data or "Statement" not in data["PolicyDocument"]:
                print(f"Required fields are missing in JSON file '{file_path}'.")
                return False


            # Check if the "Resource" field contains a single asterisk
            statement = data["PolicyDocument"]["Statement"]
            for stmt in statement:
                if not isinstance(stmt, dict):
                    print("Invalid statement structure in JSON file.")
                    return False

                resource = stmt.get("Resource")
                if not isinstance(resource, str):
                    print("Invalid resource type in JSON file.")
                    return False

                if resource == "*":
                    return False

            return True

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return False

    except json.JSONDecodeError:
        print(f"Invalid JSON format in file '{file_path}'.")
        return False
