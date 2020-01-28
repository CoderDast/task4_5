class Guns:
    bullet = 0 # количество пули в начале

    def __init__(self, name_gun):
        self.name_gun = name_gun

    def reload(self, number):
        self.bullet += number


class Soldier:
    def __init__(self, name):
        self.name = name

    def fire(self):
        print("tigi-tigitish")
        self.bullet -= 5
    


class Act_of_Shooting(Guns, Soldier):
    def __init__(self, name, name_gun):
        Guns.__init__(self, name_gun)
        Soldier.__init__(self, name)








war = Act_of_Shooting("Ryan", "AK-47")
print(war.bullet)
war.reload(30)
sum = '123456'
for i in  sum:
    print(war.bullet)
    war.fire()
print(war.bullet)



