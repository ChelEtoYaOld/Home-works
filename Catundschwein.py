class Cat:
    def __init__(self, name=None, object=None, power=1100, speed=240):
        self.name = name
        self.object = object
        self.power = power
        self.speed = speed
    def power_down(self, power):
        if self.power < 120:
            print('keine schnelle die Katze')
        else:
            print('Schnelle die Katze')

mann = Cat(name="Erik", object='schwein')
print(mann.name, mann.object, mann.power, mann.speed, sep='; ')
milka = Cat(name="Milka", object='kotik', power=550, speed=350)
print(milka.name, milka.object, milka.power, milka.speed, sep='; ')
