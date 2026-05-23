# Exercie 1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create Cat Objects
cat1 = Cat("Milo", 3)
cat2 = Cat("Luna", 7)
cat3 = Cat("Oscar", 5)

# Step 2: Create a Function to Find the Oldest Cat
def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1  # On suppose que cat1 est le plus vieux au départ
    
    if cat2.age > oldest.age:
        oldest = cat2
    
    if cat3.age > oldest.age:
        oldest = cat3
    
    return oldest

# Step 3: Print the Oldest Cat’s Details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

""" #others solutions:
# Exercice 1 
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"Cat name is {name} and age is {age}")
    
cat1=Cat("boby",7)
cat2=Cat("malosse",6)
cat3=Cat("minou",9) 
    
def find_oldest(cat1,cat2,cat3):
    tab=[cat1,cat2,cat3]
    oldest =tab[0]
    for cat in tab :
        if cat.age>oldest.age :
            oldest=cat
    print(f"le chat le plus age est {oldest.name}")
    
find_oldest(cat1,cat2,cat3) """



# Exercise 2

# Étape 1 : Créer la classe Dog
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes woof!")
    
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Étape 2 : Créer les objets chiens
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 35)

# Étape 3 : Afficher les détails et appeler les méthodes
print(f"David's dog: {davids_dog.name}, height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

print()  # ligne vide pour séparer

print(f"Sarah's dog: {sarahs_dog.name}, height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

print()  # ligne vide

# Étape 4 : Comparer les tailles
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}")
else:
    print("Both dogs are the same size!")



# Exercise 3

# Step 1: Create the Song Class
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Step 2: Create a Song Object with the Given Lyrics
stairway = Song([
    "There's a lady who's sure",
    "all that glitters is gold",
    "and she's buying a stairway to heaven"
])

# Step 3: Call the Method
stairway.sing_me_a_song()


# Exercise 4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    def get_animals(self):
        return self.animals #print(self.animals)
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    def sort_animals(self):
        self.animals.sort()  # Trie alphabétiquement
        groups = {}
        
        for animal in self.animals:
            first_letter = animal[0].upper()  # Première lettre
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(animal)
        
        return groups
    def get_groups(self):
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")


# Étape 2 : Créer un objet Zoo
brooklyn_safari = Zoo("Brooklyn Safari")

# Étape 3 : Tester les méthodes
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Lion")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.add_animal("Zebra")
brooklyn_safari.add_animal("Bear")   # doublon test

print()
brooklyn_safari.get_animals()

print()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.sell_animal("Tiger")  # n'existe pas test

print()
brooklyn_safari.get_animals()

print()
brooklyn_safari.get_groups()


