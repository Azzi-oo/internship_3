class Sotrudnik:
    def get_paid():
        pass


class Manager(Sotrudnik):
    def __init__(self, qualified_pos, bonus) -> None:
        super().__init__()
        self.qualified_pos = qualified_pos
        self.bonus = bonus

    def get_paid(self):
        return self.bonus + self.qualified_pos


class Rabotnik(Sotrudnik):
    def __init__(self, name, hourly_rating, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rating
        self.hours_worked = hours_worked

    def get_paid(self):
        return self.hourly_rate * self.hours_worked
