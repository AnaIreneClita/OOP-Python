from Owner import Owner
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def activities(self):
        pass

class Cat(Animal):
    def __init__(self, name, birth_date, breed, species, owner_name):
        self.name = name
        self.birth_date = birth_date
        self.breed = breed
        self.species = species
        self.owner_name = owner_name

    def sleep(self):
        print(f"{self.name} sleeps on the windowsill.")

    def sound(self):
        print("Meow!")

    def activities(self):
        print("Plays with a ball.")

class Dog(Animal):
    def __init__(self, name, birth_date, breed, species, owner_name):
        self.name = name
        self.birth_date = birth_date
        self.breed = breed
        self.species = species
        self.owner_name = owner_name

    def sleep(self):
        print(f"{self.name}, dog of breed {self.breed}, sleeps with a bone in its mouth.")

    def sound(self):
        print(f"The dog {self.name} makes the sound Woof Woof when it is angry.")

    def activities(self):
        print("Chases its tail, nothing interesting.")

animal_1 = Cat('Mitzy', 'June 17, 2020', 'Birman', 'Feline', 'Marius')
animal_1.sleep()

animal_2 = Dog('Azorel', '01.20.2024', 'Husky', 'Canine', 'Maria')
animal_2.sound()
animal_2.activities()