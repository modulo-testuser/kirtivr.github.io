# Bulk discounts should include exactly 10 items.
def calculate_total(price, quantity):
    subtotal = price * quantity
    if quantity >= 10:
        return subtotal * 0.9
    return subtotal