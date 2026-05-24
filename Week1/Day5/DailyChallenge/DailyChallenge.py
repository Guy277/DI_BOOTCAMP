import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        # On peut créer un cercle avec le rayon OU le diamètre
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2  # On convertit le diamètre en rayon
        else:
            raise ValueError("Vous devez fournir un rayon ou un diamètre")

    @property
    def diameter(self):
        # Decorator @property : diameter se calcule automatiquement depuis radius
        return self.radius * 2

    def area(self):
        # Calcule l'aire du cercle : π * r²
        return round(math.pi * self.radius ** 2, 2)

    def __str__(self):
        # Affiche les attributs du cercle lisiblement
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area()})"

    def __repr__(self):
        # Représentation technique du cercle
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        # Additionne deux cercles → retourne un nouveau cercle
        new_radius = self.radius + other.radius
        return Circle(radius=new_radius)

    def __gt__(self, other):
        # Compare si ce cercle est plus grand que l'autre
        return self.radius > other.radius

    def __eq__(self, other):
        # Vérifie si deux cercles sont égaux
        return self.radius == other.radius

    def __lt__(self, other):
        # Compare si ce cercle est plus petit (nécessaire pour sort())
        return self.radius < other.radius


# ---- Tests ----

# Créer des cercles
c1 = Circle(radius=5)
c2 = Circle(diameter=12)  # rayon = 6
c3 = Circle(radius=3)

# Afficher les attributs
print(c1)  # __str__
print(c2)

# Aire
print(f"Aire de c1: {c1.area()}")

# Additionner deux cercles
c4 = c1 + c2
print(f"c1 + c2 = {c4}")  # radius = 5 + 6 = 11

# Comparer les cercles
print(f"c1 > c2 : {c1 > c2}")   # 5 > 6 → False
print(f"c1 == c3 : {c1 == c3}") # 5 == 3 → False
print(f"c2 > c3 : {c2 > c3}")   # 6 > 3 → True

# Trier une liste de cercles
circles = [c1, c2, c3]
circles.sort()  # utilise __lt__
print(f"Cercles triés: {circles}")