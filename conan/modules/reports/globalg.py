import json

def ggen(*args):
    generated_data = {}
    for arg in args:
        if arg is None:
            continue
        data = json.loads(arg)
        generated_data[data["type"]] = data
        del generated_data[data["type"]]["type"]
        
    return generated_data
