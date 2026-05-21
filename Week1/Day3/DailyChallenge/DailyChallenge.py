#Challenge

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type=None, count=1, **kwargs):
        # Ajout normal (un seul animal)
        if animal_type:
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count
        
        # Bonus Step 8 : ajout via kwargs
        for animal, quantity in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += quantity
            else:
                self.animals[animal] = quantity

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-0!"
        return info

    # Bonus Step 6
    def get_animal_types(self):
        return sorted(self.animals.keys())

    # Bonus Step 7
    def get_short_info(self):
        animal_types = self.get_animal_types()
        
        # Ajouter "s" si count > 1
        animals_with_s = []
        for animal in animal_types:
            if self.animals[animal] > 1:
                animals_with_s.append(animal + "s")
            else:
                animals_with_s.append(animal)
        
        # Construire la phrase
        if len(animals_with_s) == 1:
            animals_str = animals_with_s[0]
        else:
            animals_str = ", ".join(animals_with_s[:-1]) + " and " + animals_with_s[-1]
        
        return f"{self.name}'s farm has {animals_str}."


# ---- Test ----
macdonald = Farm("McDonald")

# Méthode classique
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

print()

# Bonus Step 8 : kwargs
macdonald.add_animal(chicken=3, horse=1)
print(macdonald.get_info())

print()
print(macdonald.get_short_info())
