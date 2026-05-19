# Exercise 1 : 

#Affiche 4 fois  Hello world 
for i in range(4):
    print("Hello world") 




# Exercise 2

#Some Math
print((99**3)*8)




# Exercise 3

#What is the output?

# 5 < 3   #False


# 3 == 3   # True


# 3 == "3"  #False


# "3" > 3  #False


# "Hello" == "hello"  #False




# Exercise 4

#Your computer brand

computer_brand = "HP"

print("I have a ",computer_brand," computer.") # Affiche "I have a HP computer."    



# Exercice 5

#Your information

name = "Guy Achille"
age = 23
shoe_size = 44

info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."
print ( info )




# Exercice 6

#A & B

a = 5
b = 3
if a > b:
    print("Hello World")



# Exercice 7

#Odd "impair" or Even "pair"
number = 7
if number % 2 == 0:
    print("The number is even.") # Affiche nombre est pair 
else:
    print("The number is odd.") # Affiche nombre est impair 



# Exercice 8

# Demander le nom de l'utilisateur
user_name = input("What is your name? ")

# Ton propre nom
my_name = "Achille"

# Comparaison
if user_name == my_name:
    print("Wow! We have the same name ")
else:
    print(f"Nice to meet you, {user_name}! But my name is cooler ")


# Exercice 9

# Demander la taille en centimètres
height = int(input("Enter your height in cm: "))

# Vérifier la condition
if height > 145:
    print("You are tall enough to ride ")
else:
    print("Sorry, you need to grow some more to ride ")

