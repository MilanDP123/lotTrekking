class Applicant:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def print(self):
        return self.get_full_name() + " " + self.email
