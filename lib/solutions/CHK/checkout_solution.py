

# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    # Define the price table and offers
    price_table = {
        'A': {'price': 50, 'offer': {'quantity': 3, 'offer_price': 130}},
        'B': {'price': 30, 'offer': {'quantity': 2, 'offer_price': 45}},
        'C': {'price': 20, 'offer': None},
        'D': {'price': 15, 'offer': None}
    }
    # Check if the input contains any illegal characters
    if any(item not in price_table for item in skus):
        return -1
    
    # Initialize the total price
    total_price = 0
    
    # Count the quantity of each item
    item_count = {}
    for item in skus:
        item_count[item] = item_count.get(item, 0) + 1
    
    # Calculate the total price based on the price table and offers
    for item, count in item_count.items():
        if item in price_table:
            price = price_table[item]['price']
            offer = price_table[item]['offer']
            
            if offer and count >= offer['quantity']:
                offer_price = offer['offer_price']
                offer_count = count // offer['quantity']
                remaining_count = count % offer['quantity']
                total_price += offer_count * offer_price + remaining_count * price
            else:
                total_price += count * price
    
    return total_price

