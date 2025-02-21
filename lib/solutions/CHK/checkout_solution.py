

# noinspection PyUnusedLocal
# skus = unicode string

# The checkout feature is great and our supermarket is doing fine. Is time to think about growth.
# Our marketing teams wants to experiment with new offer types and we should do our best to support them.

# We are going to sell a new item E.
# Normally E costs 40, but if you buy 2 of Es you will get B free. How cool is that ? Multi-priced items also seemed to work well so we should have more of these.

# Our price table and offers: 
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+


# Notes: 
#  - The policy of the supermarket is to always favor the customer when applying special offers.
#  - All the offers are well balanced so that they can be safely combined.
#  - For any illegal input return -1


def checkout(skus):
    # Define the price table and offers
    price_table = {
        'A': {'price': 50, 'offer': {'quantity': 3, 'offer_price': 130}},
        'B': {'price': 30, 'offer': {'quantity': 2, 'offer_price': 45}},
        'C': {'price': 20, 'offer': None},
        'D': {'price': 15, 'offer': None},
        'E': {'price': 40, 'offer': {'quantity': 2, 'free_item': 'B'}}
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
                # this line is erroring because E does not have an offer price
                offer_price = offer['offer_price'] if 'offer_price' in offer else 0
                offer_count = count // offer['quantity']
                remaining_count = count % offer['quantity']
                total_price += offer_count * offer_price + remaining_count * price
                if item == 'E':
                    free_item = offer['free_item']
                    free_item_count = min(offer_count, item_count.get(free_item, 0))
                    total_price -= free_item_count * price_table[free_item]['price']
            else:
                total_price += count * price
    
    return total_price


