class Room:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.applications = []

    def new_application(self, application):
        self.applications.append(application)

    def get_applications(self):
        return self.applications
