# noinspection PyUnusedLocal
# skus = unicode string

# Our price table and offers: 
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
# +------+-------+------------------------+

def checkout(skus):
    # Define the price table and offers
    
    price_table = {
        'A': {'price': 50, 'offer': [{'quantity': 3, 'offer_price': 130}, {'quantity': 5, 'offer_price': 200}]},
        'B': {'price': 30, 'offer': [{'quantity': 2, 'offer_price': 45}]},
        'C': {'price': 20, 'offer': []},
        'D': {'price': 15, 'offer': []},
        'E': {'price': 40, 'offer': []},
        'F': {'price': 10, 'offer': [{'quantity': 3, 'offer_price': 20}]}
    }

    free_items = {
        'B': {'associated_item': 'E', 'quantity': 2}
    }
    # Check if the input is valid
    for item in skus:
        if item not in price_table:
            return -1
        
    # Count the number of each item
    item_count = count_items(skus)
    free_item_count = get_free_item_count(item_count, free_items)
    item_count_minus_free_items = {item: item_count[item] - free_item_count.get(item, 0) for item in item_count}

    # Calculate the total price based on the price table and offers
    total_price = 0  # Initialize total_price to 0
    for item, count in item_count_minus_free_items.items():
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

