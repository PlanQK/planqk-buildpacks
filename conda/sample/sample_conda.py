import json

def read_json_file_and_print_to_console(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print('File was not found')
    except json.JSONDecodeError as e:
        print(f"Failure while decoding Json: {str(e)}")

if __name__ == "__main__":
    file_path = '/app/example.json' # directory at docker container
    read_json_file_and_print_to_console(file_path)
