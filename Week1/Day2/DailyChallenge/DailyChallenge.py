# Challenge 1: 

# Letter Index Dictionary


word = input("Enter a word: ") # Example: "hello"
letter_indices = {}

for index, char in enumerate(word): # index will be 0,1,2,3,4 and char will be 'h','e','l','l','o'
    if char in letter_indices:
        letter_indices[char].append(index) 
    else:
        letter_indices[char] = [index]

print(letter_indices) 


# Challenge 2: 

# Affordable Items

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# Data cleaning - remove $ and commas
def clean_price(price_str):
    return int(price_str.replace("$", "").replace(",", ""))

wallet = clean_price(wallet)

basket = []

for item, price in items_purchase.items():
    price = clean_price(price)
    if price <= wallet:
        basket.append(item)
        wallet -= price

if not basket:
    print("Nothing")
else:
    print(sorted(basket))