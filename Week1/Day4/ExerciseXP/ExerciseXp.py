# Exercice 1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'  

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal_obj = Bengal("Bengal", 3)
chartreux_obj = Chartreux("Chartreux", 5)       
siamese_obj = Siamese("Siamese", 2)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets = Pets(all_cats)
sara_pets.walk()   
                          


# Exercice2

# Step 1: Create the Dog Class
class Dog():
    def __init__(self, name, age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'
    def run_speed(self):
        if self.age == 0:
            return 0
        return self.weight/self.age*10
    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f'{self.name} won the fight'
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
            return f'{other_dog.name} won the fight'
        else:
            return 'The fight is a tie'


# Step 2: Create dog instances
dog1 = Dog("Buddy", 5, 20)
dog2 = Dog("Max", 3, 15)
dog3 = Dog("Charlie", 4, 25)

# Step 3: Test dog methods

print(dog1.bark())
print(dog1.run_speed())

print(dog2.bark())
print(dog2.run_speed())

print(dog1.fight(dog2))




# Exercice 3
from Exercise2Xp import Dog
import random


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        all_dogs = ", ".join([self.name] + list(args))
        print(f"{all_dogs} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet")

# Test
pet_dog1 = PetDog("Rex", 2, 10)
pet_dog1.train()
pet_dog1.play("Buddy", "Max", "Charlie")
pet_dog1.do_a_trick()


# Exercice 4

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18
    
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_member = Person(first_name, age)
        new_member.last_name = self.last_name
        self.members.append(new_member)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("Person not found in the family.")

    def family_presentation(self):
        print(f"Family Name: {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, Age: {member.age}")


# Test
family = Family("Smith")
family.born("Jane", 25)
family.born("John", 17)
family.born("Alice", 14)

family.family_presentation()
print()
family.check_majority("Jane")
family.check_majority("John")
family.check_majority("Bob") 

