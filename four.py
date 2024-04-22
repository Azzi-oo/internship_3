class Car:

    def __init__(self, marka, color, speed):
        self.marka = marka
        self.color = color
        self.speed = speed

    def __str__(self):
        return self.marka
