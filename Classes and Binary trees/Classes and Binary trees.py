class Cat:
    def __init__(self, size, color, race, price):
        self.size = size
        self.color = color
        self.race = race
        self.price = price

    def walkin(self):
         print(f"{self.race} is the race")   
Euripides = Cat("Small","Orange", "Somali", "Adopt")
print(f"Euripides: {Euripides.size}, {Euripides.color}, {Euripides.race}, {Euripides.price}")
Anaxagoras = Cat("Big","White","Maine coon","5000")
print(f"Anaxagoras: {Anaxagoras.size}, {Anaxagoras.color}, {Anaxagoras.race}, {Anaxagoras.price}")
Bills = Cat("Medium","Skin","Sphynx", "3000")
print(f"Bills: {Bills.size}, {Bills.color}, {Bills.race}, {Bills.price}")
Heraclito = Cat("Medium","Orange","Somali", "3000")
print(f"Heraclito: {Heraclito.size}, {Heraclito.color}, {Heraclito.race}, {Heraclito.price}")
Peter = Cat("Medium","Black","japanese Bobtail", "3000")
print(f"Peter: {Peter.size}, {Peter.color}, {Peter.race}, {Peter.price}")

class Dog:
    def __init__(self, size, color, race, price):
        self.size = size
        self.color = color
        self.race = race
        self.price = price

    def walking(self):
        print(f"{self.race} is the race")
Francisco = Dog("Small", "Brown","Pug","Free" )
print(f"Francisco: {Francisco.size}")

Hades = Dog("Big", "Black","Husky", 5000 )
print(f"Hades: {Hades.size}")

Tairon = Dog("Small", "White","Bulldog",1000 )
print(f"Tairon: {Tairon.size}, {Tairon.color}, {Tairon. race}, {Tairon.price}.")

Uniqua = Dog("Big", "Brown","Golden Retriever","Free" )
print(f"Uniqua: {Uniqua.size}, {Uniqua.color}, {Uniqua. race}, {Uniqua.price}.")

Grecia = Dog("Small", "Brown","Chihuahua","Free" )
print(f"Grecia: {Grecia.size}, {Grecia.color}, {Grecia. race}, {Grecia.price}.")




class people:
    def __init__(me,size, haircolor, eyesize, mood):
        me.size = size
        me. haircolor = haircolor
        me. eyesize = eyesize
        me.mood = mood
        
    def fealing(me):
        print(f"{me.mood} is the mood")


Andrea = people(1.59, "Brown","Big","bored" )
print(f"{Andrea.size}, {Andrea.haircolor}, {Andrea.eyesize}")
Andrea.fealing()

Julian = people(1.69, "Brown","small","joker" )
print(f"{Julian.size}, {Julian.haircolor}, {Julian.eyesize}")
Julian.fealing()

Alvaro = people(1.70, "Brown","Big","Mad")
print(f"{Alvaro.size}, {Alvaro.haircolor}, {Alvaro.eyesize}")

Camilo = people(1.83, "Brown","Small","Focus")
print(f"{Camilo.size}, {Camilo.haircolor}, {Camilo.eyesize}")

Sergio= people(1.78, "Black","Medium","Sad")
print(f"{Sergio.size}, {Sergio.haircolor}, {Sergio.eyesize}")