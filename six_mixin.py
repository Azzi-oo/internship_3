class PrintMixin:
    def printing(self):
        print(f"Имя: {self.name}, Оценка: {self.ocenka}")


class Uchitel:
    def __init__(self, name, predmet):
        self.name = name
        self.predmet = predmet


class Uchenik(PrintMixin, Uchitel):
    def __init__(self, name, age, ocenka):
        super().__init__(name, age)
        self.ocenka = ocenka


employee = Uchenik("Иван", 15, 5)
employee.printing()
