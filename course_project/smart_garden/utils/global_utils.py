def generate_filename(name):
    return str(name).replace(" ", "_")

def generate_pot_filename(name):
    return "pot_" + str(name).replace(" ", "_") + ".json"
