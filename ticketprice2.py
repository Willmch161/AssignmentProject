import random

# Function to get the material price range based on the material and brand
def get_material_price(material, brand):
    material_prices = {
        'Stainless Steel': {
            'Brand A': (30, 50),  # Brand A Stainless Steel is expensive
            'Brand B': (20, 40),  # Brand B Stainless Steel is moderately priced
            'Brand C': (15, 30),  # Brand C Stainless Steel is cheaper
        },
        'Carbon Steel': {
            'Brand A': (40, 70),  # Brand A Carbon Steel is very expensive
            'Brand B': (30, 60),  # Brand B Carbon Steel is moderately priced
            'Brand C': (20, 50),  # Brand C Carbon Steel is affordable
        },
        'Plastic': {
            'Brand A': (10, 20),  # Brand A Plastic is low-cost
            'Brand B': (8, 15),   # Brand B Plastic is cheaper
            'Brand C': (5, 12),   # Brand C Plastic is very affordable
        },
        'Titanium': {
            'Brand A': (80, 150),  # Brand A Titanium is premium
            'Brand B': (60, 120),  # Brand B Titanium is moderately priced
            'Brand C': (50, 100),  # Brand C Titanium is affordable
        }
    }
    return random.randint(*material_prices.get(material, {}).get(brand, (10, 30)))

# Function to get size-based price range
def get_size_price(size):
    size_prices = {
        'Small': (5, 15),   # Small scissors are cheaper
        'Medium': (10, 25),  # Medium scissors have moderate price range
        'Large': (20, 50)    # Large scissors are more expensive
    }
    return random.randint(*size_prices.get(size, (10, 25)))

# Function to calculate the total price
def calculate_scissors_price(material, size, brand):
    material_price = get_material_price(material, brand)
    size_price = get_size_price(size)

    # Total price is the sum of material and size price
    total_price = material_price + size_price
    return total_price

# Input specifications from the user
print("Choose the scissors specifications:")

material = input("Material (Stainless Steel, Carbon Steel, Plastic, Titanium): ")
size = input("Size (Small, Medium, Large): ")
brand = input("Brand (Brand A, Brand B, Brand C): ")

# Calculate the price
price = calculate_scissors_price(material, size, brand)

print(f"\nThe price of the scissors is: ${price}")
