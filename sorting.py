import pandas as pd

# Load data from a CSV file
data = pd.read_csv("data/16_04_2023.csv.csv")

# Create dictionaries of keywords for each category
meat_poultry = ['beef', 'pork', 'chicken', 'turkey', 'lamb', 'sausage', 'patties', 'steak']
fish_seafood = ['fish', 'salmon', 'shrimp', 'crab', 'lobster', 'prawn', 'mussels', 'fillet']
fridge_deli = ['cheese', 'yogurt', 'milk', 'cream', 'butter', 'egg', 'ham', 'bacon', 'salami', 'olivani', 'hummus', 'dip']
bakery = ['bread', 'bagel', 'pastry', 'croissant', 'muffin', 'buns', 'bakery']
frozen = ['ice cream', 'pizza', 'frozen vegetables', 'frozen fruits']
pantry = ['cereal', 'pasta', 'rice', 'beans', 'sauces', 'spices', 'chips', 'spread', 'cereal', 'sauce', 'chocolate', 'biscuits', 'crackers', 'noodles', 'coffee', 'espresso']
beer_wine = ['beer', 'wine', 'spirits', 'whiskey', 'vodka', 'rose', 'pinot', 'sauvignon', 'cider', 'brut', 'shiraz']
drinks = ['soda', 'juice', 'water', 'tea', 'coffee']
health_body = ['vitamins', 'supplements', 'shampoo', 'soap', 'lotion', 'tissues', 'toothpaste', 'conditioner', 'body wash', 'mouthwash', 'hand wash']
household = ['cleaning supplies', 'laundry detergent', 'paper towels', 'batteries', 'dishwash', 'laundry']
baby_child = ['diapers', 'baby food', 'toys']
pet = ['dog food', 'cat food', 'pet toys']

# Categorize items based on keywords
category_list = []
for product_name in data['item_name']:
    category = 'Unknown'
    for keyword in meat_poultry:
        if keyword in product_name.lower():
            category = 'Meat & Poultry'
            break
    for keyword in fish_seafood:
        if keyword in product_name.lower():
            category = 'Fish & Seafood'
            break
    for keyword in fridge_deli:
        if keyword in product_name.lower():
            category = 'Fridge & Deli'
            break
    for keyword in bakery:
        if keyword in product_name.lower():
            category = 'Bakery'
            break
    for keyword in frozen:
        if keyword in product_name.lower():
            category = 'Frozen'
            break
    for keyword in pantry:
        if keyword in product_name.lower():
            category = 'Pantry'
            break
    for keyword in beer_wine:
        if keyword in product_name.lower():
            category = 'Beer & Wine'
            break
    for keyword in drinks:
        if keyword in product_name.lower():
            category = 'Drinks'
            break
    for keyword in health_body:
        if keyword in product_name.lower():
            category = 'Health & Body'
            break
    for keyword in household:
        if keyword in product_name.lower():
            category = 'Household'
            break
    for keyword in baby_child:
        if keyword in product_name.lower():
            category = 'Baby & Child'
            break
    for keyword in pet:
        if keyword in product_name.lower():
            category = 'Pet'
            break
    category_list.append(category)

# Add category column to the data frame
data['category'] = category_list

# Print the data frame with category column
print(data[['item_name', 'category']])
