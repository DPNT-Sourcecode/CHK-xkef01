# noinspection PyUnusedLocal
# skus = unicode string

# Our price table and offers: 
# +------+-------+---------------------------------+
# | Item | Price | Special offers                  |
# +------+-------+---------------------------------+
# | A    | 50    | 3A for 130, 5A for 200          |
# | B    | 30    | 2B for 45                       |
# | C    | 20    |                                 |
# | D    | 15    |                                 |
# | E    | 40    | 2E get one B free               |
# | F    | 10    | 2F get one F free               |
# | G    | 20    |                                 |
# | H    | 10    | 5H for 45, 10H for 80           |
# | I    | 35    |                                 |
# | J    | 60    |                                 |
# | K    | 70    | 2K for 120                      |
# | L    | 90    |                                 |
# | M    | 15    |                                 |
# | N    | 40    | 3N get one M free               |
# | O    | 10    |                                 |
# | P    | 50    | 5P for 200                      |
# | Q    | 30    | 3Q for 80                       |
# | R    | 50    | 3R get one Q free               |
# | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | U    | 40    | 3U get one U free               |
# | V    | 50    | 2V for 90, 3V for 130           |
# | W    | 20    |                                 |
# | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
# +------+-------+---------------------------------+

def checkout(skus):
    # Define the price table and offers
    
    price_table = {
        'A': {'price': 50, 'offer': [{'quantity': 3, 'offer_price': 130}, {'quantity': 5, 'offer_price': 200}]},
        'B': {'price': 30, 'offer': [{'quantity': 2, 'offer_price': 45}]},
        'C': {'price': 20, 'offer': []},
        'D': {'price': 15, 'offer': []},
        'E': {'price': 40, 'offer': []},
        'F': {'price': 10, 'offer': [{'quantity': 3, 'offer_price': 20}]},
        'G': {'price': 20, 'offer': []},
        'H': {'price': 10, 'offer': [{'quantity': 5, 'offer_price': 45}, {'quantity': 10, 'offer_price': 80}]},
        'I': {'price': 35, 'offer': []},
        'J': {'price': 60, 'offer': []},
        'K': {'price': 70, 'offer': [{'quantity': 2, 'offer_price': 120}]},
        'L': {'price': 90, 'offer': []},
        'M': {'price': 15, 'offer': []},
        'N': {'price': 40, 'offer': []},
        'O': {'price': 10, 'offer': []},
        'P': {'price': 50, 'offer': [{'quantity': 5, 'offer_price': 200}]},
        'Q': {'price': 30, 'offer': [{'quantity': 3, 'offer_price': 80}]},
        'R': {'price': 50, 'offer': []},
        'S': {'price': 20, 'offer': []},
        'T': {'price': 20, 'offer': []},
        'U': {'price': 40, 'offer': [{'quantity': 4, 'offer_price': 120}]},
        'V': {'price': 50, 'offer': [{'quantity': 2, 'offer_price': 90}, {'quantity': 3, 'offer_price': 130}]},
        'W': {'price': 20, 'offer': []},
        'X': {'price': 17, 'offer': []},
        'Y': {'price': 20, 'offer': []},
        'Z': {'price': 21, 'offer': []},

    }

    free_items = {
        'B': {'associated_item': 'E', 'quantity': 2},
        'M': {'associated_item': 'N', 'quantity': 3},
        'Q': {'associated_item': 'R', 'quantity': 3},
    }

    any_three_items = ['X', 'S', 'T', 'Y', 'Z'] #arranged in ascending order of price
    any_three_items_offer_price = 45

    # Check if the input is valid
    for item in skus:
        if item not in price_table:
            return -1
        
    # Count the number of each item
    item_count = count_items(skus)
    free_item_count = get_free_item_count(item_count, free_items)
    item_count_minus_free_items = {item: item_count[item] - free_item_count.get(item, 0) for item in item_count}
    any_three_offer_total_price = get_any_three_items_total_offer_price(item_count_minus_free_items, any_three_items, any_three_items_offer_price)
    item_count_minus_free_items_and_any_three_items = {item: item_count_minus_free_items[item] for item in item_count_minus_free_items if item not in any_three_items}

    # Calculate the total price based on the price table and offers
    total_price = any_three_offer_total_price  # Initialize total_price to any three items offer price
    for item, count in item_count_minus_free_items_and_any_three_items.items():
        if item in price_table:
            price = price_table[item]['price']
            offers = price_table[item]['offer']
            
            if len(offers)> 0:
                while count > 0:
                    best_offer = get_best_offer(offers, count)
                    
                    if best_offer:
                        offer_count = count // best_offer['quantity']
                        print(f"item:{item}, offer_count: {offer_count}")

                        remaining_count = count % best_offer['quantity']
                        print(f"item:{item},remaining_count: {remaining_count}")

                        total_price += offer_count * best_offer['offer_price'] 
                        count = remaining_count
                    else:
                        total_price += count * price
                        count = 0
                    print(f"item:{item},total_price: {total_price}")
            else:
                total_price += count * price
    
    return total_price

def count_items(skus):
    item_count = {}
    for item in skus:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    return item_count

def get_free_item_count(item_count, free_items):
    free_item_count = {}
    for free_item in free_items:
        if free_item in item_count and free_items[free_item]['associated_item'] in item_count:
            associated_item_count = item_count[free_items[free_item]['associated_item']]
            free_item_count[free_item] = associated_item_count // free_items[free_item]['quantity']
    return free_item_count


def get_best_offer(offers, count):
    best_offer = None
    for offer in offers:
        if count >= offer['quantity']:
            if not best_offer or offer['quantity'] > best_offer['quantity']:
                best_offer = offer
    return best_offer

def get_any_three_items_total_offer_price(item_count, any_three_items, any_three_items_offer_price):
    offer_price = 0
    any_three_item_count = {item: item_count[item] for item in any_three_items if item in item_count}
    any_three_item_quantity = sum(any_three_item_count.values())
    offer_count = any_three_item_quantity // 3
    remaining_count = any_three_item_quantity % 3
    offer_price = offer_count * any_three_items_offer_price
    offer_price += remaining_count * min([item_count[item] for item in any_three_items if item in item_count])
    return  offer_price