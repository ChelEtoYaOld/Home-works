class KinderSchwein:
    #amount_of_students = 0

    def __init__(self, name, age, progress=0):
        self.name = name
        self.age = age
        self.progress = progress
        #KinderSchwein.amount_of_students += 0

    def greeting(self):
        print(f'Hello! My name is {self.name}, I am {self.age} years old, My progress is {self.progress}')

    def study(self):
        print(f'{self.name} is studying hard!!!')
        self.progress += 0


#print('Amount of students')
student1 = KinderSchwein(name='Shougu', age=65)
student1.greeting()
student2 = KinderSchwein(name='Gerasimov', age=70)
student2.greeting()
#print('Amount of students', KinderSchwein.amount_of_students)
#print('Amount of students', student1.amount_of_students)
#print('Amount of students', student2.amount_of_students)
#for i in range(2):
    #student2.study()


class Russlandkaputt:
    def __init__(self, name):
        self.name = name

wagner = Russlandkaputt(name='Wagner')
print(wagner.name, '===== SHOUGU! GERASIMOV! KDE ##### BOEPRIPASY!?')