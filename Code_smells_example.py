#Code Smells Example for long method
def calculate_discounted_price(item):
    if item.quantity <= 0:
        return 0
    discount_rate = 0.9 if item.price > 100 else 0.95
    return item.price * discount_rate

def calculate_total_price(items):
    total = 0
    for item in items:
        total += calculate_discounted_price(item)
    return total
