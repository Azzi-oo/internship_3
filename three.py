class Calculator:

    def plus(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def umnozhenie(self, a, b):
        return a * b

    def delenie(self, a, b):
        if b != 0:
            return a / b
        else:
            print("Делить на ноль нельзя")
