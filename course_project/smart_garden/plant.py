class Plant:
    """Plant model cass
    stores information about:
    - conditions of which plant needs
    - plant characterisations - to evaluate plant progress"""
    def __init__(self, name, humidity, soil_moisture, temperature, light_levels, height, leaves_density,notes = None ):
        self.id = None
        self.name = name
        self.notes = notes

        ### the needed conditions for the plant
        self.humidity = humidity # percentages
        self.soil_moisture = soil_moisture # percentages
        self.temperature = temperature # celsius
        self.light_levels = light_levels # hours sun light per day

        ### plant characterizations
        self.height = height
        self.leaves_density = leaves_density

    def __repr__(self):
        return f"{self.name} needs of {self.humidity} percentages of humidity, " \
               f"{self.soil_moisture} percentages of soil moisture, " \
               f"average temperature of {self.temperature} Celsius, and " \
               f"average {self.light_levels} hours per day"

    def __str__(self):
        return f"{self.name} needs of: " \
               f"air humidity - {self.humidity} % | "\
               f"soil moisture - {self.soil_moisture} % | " \
               f"air temperature - {self.temperature} C | " \
               f"sun light per day - {self.light_levels} h;"

    def get_conditions(self):
        return {
            "humidity" : self.humidity,
            "soil_temperature": self.soil_moisture,
            "temperature": self.temperature,
            "light_levels": self.light_levels
        }

    def get_characteristics(self):
        return {
            "height" : self.height,
            "leaves_density": self.leaves_density,
        }
