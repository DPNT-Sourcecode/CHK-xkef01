

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
        'A': {'price': 50, 'offer': [{'quantity': 3, 'offer_price': 130}, {'quantity': 5, 'offer_price': 200}]},
        'B': {'price': 30, 'offer': [{'quantity': 2, 'offer_price': 45}]},
        'C': {'price': 20, 'offer': []},
        'D': {'price': 15, 'offer': []},
        'E': {'price': 40, 'offer': [{'quantity': 2, 'free_item': 'B'}]}
    }
    # Check if the input is valid
    for item in skus:
        if item not in price_table:
            return -1
        
    # Count the number of each item
    item_count = {}
    for item in skus:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1

    # Calculate the total price based on the price table and offers
    total_price = 0  # Initialize total_price to 0
    for item, count in item_count.items():
        if item in price_table:
            price = price_table[item]['price']
            offers = price_table[item]['offer']
            
            if offers.length > 0:
                best_offer = None
                for offer in offers:
                    if count >= offer['quantity']:
                        if not best_offer or offer['offer_price'] < best_offer['offer_price']:
                            best_offer = offer
                
                if best_offer:
                    offer_count = count // best_offer['quantity']
                    remaining_count = count % best_offer['quantity']
                    total_price += offer_count * best_offer['offer_price'] + remaining_count * price
                    if item == 'E':
                        free_item = best_offer['free_item']
                        free_item_count = min(offer_count, item_count.get(free_item, 0))
                        total_price -= free_item_count * price_table[free_item]['price']
                else:
                    total_price += count * price
            else:
                total_price += count * price
    
    return total_price



