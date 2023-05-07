import random

class Student:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.progress = 0
        self.active = True
        self.money = 50

    def to_work(self):
        print('Time to Zavod!')
        self.money += 100
        self.happiness += 3
        self.progress += 0.1

    def to_study(self):
        print('Time to study!')
        self.progress += 0.12
        self.happiness -= 5
        self.money -= 40


    def to_sleep(self):
        print('Zzzzz patriot')
        self.happiness += 3

    def to_chill(self):
        print('Chill time!')
        self.happiness += 5
        self.progress -= 0.1
        self.money -= 40

    def is_active(self):
        if self.progress < -0.5:
            print('Vidrahuyavannya!')
            self.active = False
        elif self.happiness < 0:
            print('Dead Inside!')
            self.active = False
        elif self.progress > 15:
            print('Passed externally!')
            self.active = False
        elif self.money < 10:
            print('Daite denyah!!!')
            self.to_work()


    def status(self):
        print(f'Happiness - {self.happiness}')
        print(f'Progress - {round(self.progress, 2)}')
        print(f'Money - {self.money}')

    def live_a_day(self, day):
        day_str = f'Day {day} of {self.name} life'
        print(f'{day_str:^50}')
        dice = random.randint(1, 4)
        if dice == 1:
            self.to_study()
        elif dice == 2:
            self.to_sleep()
        elif dice == 3:
            self.to_chill()
        elif dice == 4:
            self.to_work()
        self.status()
        self.is_active()

michael = Student(name='Michael')
for day in range(365):
    if michael.active:
        michael.live_a_day(day)
    else:
        break
if michael.active:
    print('HURRAAAH! Rossii bolshe NEET!')

