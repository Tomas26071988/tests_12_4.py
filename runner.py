
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('Имя может быть только строкой')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError('Скорость не может быть отрицательной')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed
