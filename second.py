class Chelovek:
    def __init__(self, name, city, bitrh_year):
        self.name = name
        self.city = city
        self.birth_year = bitrh_year

    def age_in_year(self, age_in_moment):
        age = age_in_moment - self.birth_year
        return age
