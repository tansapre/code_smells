#Code Smells Example for long method
def calculate_total_price(items):
    total = 0
    for item in items:
        if item.quantity > 0:
            discount_rate = 0.9 if item.price > 100 else 0.95
            discounted_price = item.price * discount_rate
            total += discounted_price
    return total
