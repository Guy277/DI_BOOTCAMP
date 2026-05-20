# Exercice 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
zipper=zip(keys, values)
result = dict(zipper)
print(result)



# Exercice 2

my_dict ={}
n=int(input("Enter the total number of member familly you want to add in the dictionary: "))
for i in range(n):
    name=input("Enter the name of the member familly: ")
    age=int(input("Enter the age of the member familly: "))
    my_dict[name]=age
print(my_dict)

for key, value in my_dict.items():
    print(f"{key} your ticket price is:")
    if value < 3:
        print("billet gratuit")
    elif value >=3 and value < 12:
        print(f"billet : {10} $ ")
    elif value >12 :
        print(f"billet : {15} $ ")

  
# Exercice 3

#creating dictionary

#Create a dictionary called brand with the provided data.
brand = {"name": "Zara", "creation_date": 1975, "creator_name": "Amancio Ortega Gaona", "type_of_clothes": ["men", "women", "children", "home"], "international_competitors": ["Gap", "H&M", "Benetton"], "number_stores": 7000, "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]}}

#Modify 
#Change the value of number_stores to 2.
brand.update({"number_stores": 2})

#Print a sentence describing Zara’s clients using the type_of_clothes key
print("Zara’s clients using the type_of_clothes is: ", brand["type_of_clothes"])

#Add a new key country_creation with the value Spain.
brand["country_creation"] = "Spain"

#Check if international_competitors exists and, if so, add “Desigual” to the list.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual") 

#Delete the creation_date key.
del brand["creation_date"]

#Print the last item in international_competitors
print("The last item in international_competitors is: ", brand["international_competitors"][-1])

#Print the major colors in the US.
print("The major colors in the US are: ", brand["major_color"]["US"])

#Print the number of keys in the dictionary.
print("The number of keys in the dictionary is: ", len(brand))

#Print all keys of the dictionary.
print("All keys of the dictionary are: ", brand.keys())


#Bonus
#Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.
more_on_zara = {"creation_date": 1975, "number_stores": 7000}
brand.update(more_on_zara)
print("Merged dictionary:", brand)


# Exercice 4
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")
describe_city("Abidjan", "Côte d’Ivoire")


# Exercice 5
#import random module to generate random numbers
import random

def number(n):
    return n

n=int(input("Enter a number: "))
if n >= 1 and number(n) <= 100:
    a=number(n)
else:
    print("The number is out of range. Please enter a number between 1 and 100.")

def random_number():
    n=101
    return random.randint(1, n)

b=random_number()
if a == b:
    print(f"Congratulations! You guessed the number.<<<{a}>>>")
else:    print(f"Sorry, {a} differs from the random number {b}. Try again!")



# Exercise 6: Personalized Shirts

# Step 1: Define the function with parameters and default values
def make_shirt(size="large", text="I love Python"):
    # Step 2: Print a summary message using f-string formatting
    print(f"The size of the shirt is {size} and the text is {text}.")

# Step 3: Call the function with default values
make_shirt()  
# Expected output: The size of the shirt is large and the text is I love Python.

# Step 4: Call the function with a custom size but default text
make_shirt("medium")  
# Expected output: The size of the shirt is medium and the text is I love Python.

# Step 5: Call the function with custom size and custom text
make_shirt("small", "Custom message")  
# Expected output: The size of the shirt is small and the text is Custom message.

# Step 6 (Bonus): Call the function using keyword arguments
make_shirt(size="small", text="Hello!")  
# Expected output: The size of the shirt is small and the text is Hello!



# Exercise 7: Temperature Advice
import random

# Step 1: Function to generate a random temperature
# Bonus: using random.uniform for floating-point values
def get_random_temp():
    return round(random.uniform(-10, 40), 1)  # one decimal place

# Step 2: Main function
def main():
    # Call get_random_temp() and store the result
    temp = get_random_temp()
    
    # Print a friendly message
    print(f"The temperature right now is {temp} degrees Celsius.")
    
    # Step 3: Provide advice based on temperature ranges
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif 17 <= temp <= 23:
        print("Nice weather.")
    elif 24 <= temp <= 32:
        print("A bit warm, stay hydrated.")
    else:  # 33–40
        print("It's really hot! Stay cool.")

# Step 4: Call the main function
main()


# Exercise 8: Pizza Toppings

# Base price of the pizza
base_price = 10.0
# Price per topping
topping_price = 2.5

# List to store all chosen toppings
toppings = []

# Loop to ask the user for toppings
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    
    if topping.lower() == "quit":
        break
    else:
        toppings.append(topping)
        print(f"Adding {topping} to your pizza.")

# After exiting the loop, print all toppings
print("\nYour pizza toppings are:", ", ".join(toppings))

# Calculate total cost
total_cost = base_price + (len(toppings) * topping_price)
print(f"Total cost of the pizza: ${total_cost:.2f}")
