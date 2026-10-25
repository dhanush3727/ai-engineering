class Equipment:
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours

    def get_details(self):
        return f"{self.name}: {self.hours} hours"