class First:
    def func_first(self):
        print("Первый")


class Second:
    def func_second(self):
        print("Вторая функция")


class Three(First, Second):
    pass


# obj = Three()

# obj.func_first()
# obj.func_second()
