import json

def verify_json(file_path):
    try:
        with open(file_path, 'r') as file:
            json_document = json.load(file)

        policy_document = json_document.get("PolicyDocument", {})

        statements = policy_document.get("Statement", [])

        for statement in statements: # contains list of statements https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json
            resource = statement.get("Resource")

            if resource == "*":
                return False

        return True

    except FileNotFoundError:
        print(f"Error: file does not not exist at this path: {file_path}")
        raise FileNotFoundError

    except Exception as e:
        print(f"Error: unexpected error: {e}")
        raise e

if __name__ == "__main__":
    import sys
    output = verify_json(sys.argv[1])
    if output:
        print("JSON does not contain * in resource field")
    else:
        print("JSON contains * in resource field")
