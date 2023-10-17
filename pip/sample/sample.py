import json

def run(user_file):
    try:
        with open(user_file, 'r') as json_file:
            data = json.load(json_file)
            # Hier wird der JSON Inhalt in einen Atring konvertiert
            print(json.dumps(data,indent=4))
            return json.dumps(data, indent=4)
            
    except FileNotFoundError:
        return "Die Datei konnte nicht gefunden werden."
    except json.JSONDecodeError as e:
        return str(e)



run(r'C:\Users\RobertBrennenstuhl\Desktop\New\planqk-buildpacks\pip\sample\sampe_data.json')
