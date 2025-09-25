# Task 4 - Functions and Duck Typing

# Finds the price after a discount
def calculate_discount(price, discount):
    
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise TypeError("Price / discount must be numbers.")

    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100.")

    total = price * (1 - discount / 100)
    return round(total, 2)
