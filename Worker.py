class Worker:
    def __init__(self, name, education, speciality, year_of_born, stage):
        self.name = name
        self.education = education
        self.speciality = speciality
        self.year_of_born = year_of_born
        self.stage = stage

    def get_name(self):
        return self.name

    def get_education(self):
        return self.education

    def get_speciality(self):
        return self.speciality

    def get_year_of_born(self):
        return self.year_of_born

    def get_stage(self):
        return self.stage


    def __str__(self) -> str:
        return f'Name: {self.name}\n' \
               f'Education: {self.education}\n' \
               f'Specialty: {self.specialty}\n' \
               f'Experience: {self.experience}\n' \
               f'birth: {self.birth}\n'\
