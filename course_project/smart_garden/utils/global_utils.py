import os.path

def generate_filename(name):
    return str(name).replace(" ", "_")

def generate_pot_filename(name):
    return "pot_" + str(name).replace(" ", "_") + ".json"

def extract_name(filepath):
    name = os.path.basename(filepath).split('.')[0]
    name = " ".join(name.split('_'))
    # print("***", name)
    return name

def dict_repr(dict):
    line = ""
    for key, value in dict.items():
        key = " ".join(str(key).capitalize().split('_')).strip()
        line+= f"{key:<8}: {str(value):<15}\n"
    return line
