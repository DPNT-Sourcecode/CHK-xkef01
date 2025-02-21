

# noinspection PyUnusedLocal
# skus = unicode string
# The purpose of this function is to implement a supermarket checkout that calculates the total price of a number of items.

# In a normal supermarket, things are identified using Stock Keeping Units, or SKUs. 
# In our store, we'll use individual letters of the alphabet (A, B, C, and so on). 
# Our goods are priced individually. In addition, some items are multi-priced: buy n of them, and they'll cost you y pounds. 
# For example, item A might cost 50 pounds individually, but this week we have a special offer: 
#  buy three As and they'll cost you 130.

# Our price table and offers: 
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+

def checkout(skus):
    # Define the price table and offers
    price_table = {
        'A': {'price': 50, 'offer': {'quantity': 3, 'offer_price': 130}},
        'B': {'price': 30, 'offer': {'quantity': 2, 'offer_price': 45}},
        'C': {'price': 20, 'offer': None},
        'D': {'price': 15, 'offer': None}
    }
    
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

