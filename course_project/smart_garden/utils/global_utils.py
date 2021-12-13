import os.path

import config


def construct_filename(name):
    return str(name).replace(" ", "_")

def generate_file_path(name, prefix):
    if prefix:
        prefix = prefix + "_"
    return prefix + str(name).replace(" ", "_") + "." + config.DB_FILE_EXT

def generate_garden_root_dir(name):
    return os.path.join(config.DATA_PATH, construct_filename(name) )

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
