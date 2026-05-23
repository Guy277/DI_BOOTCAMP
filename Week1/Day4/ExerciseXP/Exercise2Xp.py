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