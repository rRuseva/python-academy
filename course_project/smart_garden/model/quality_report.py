import datetime

class QualityReport:
    """Template for evaluation of plant progress"""
    def __init__(self, date_time, author, plant_characterization):
        self.id = None
        self.date_time = datetime.datetime.now()
        self.author = author
        self.plant_characterizations = plant_characterization

    def __repr__(self):
        pass

    def __str__(self):
        pass
