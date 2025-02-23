# noinspection PyUnusedLocal
# skus = unicode string



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
    item_count = count_items(skus)

    # Calculate the total price based on the price table and offers
    total_price = 0  # Initialize total_price to 0
    for item, count in item_count.items():
        if item in price_table:
            price = price_table[item]['price']
            offers = price_table[item]['offer']
            
            if len(offers)> 0:
                while count > 0:
                    best_offer = get_best_offer(offers, count)
                    
                    if best_offer:
                        offer_count = count // best_offer['quantity']
                        print(f"offer_count: {offer_count}")

                        remaining_count = count % best_offer['quantity']
                        print(f"remaining_count: {remaining_count}")
                        if item != 'E':

                            total_price += offer_count * best_offer['offer_price'] #+ remaining_count * price
                        else:
                            total_price += best_offer['quantity'] * price #+ remaining_count * price

                        if item == 'E':
                            free_item = best_offer['free_item']
                            free_item_count = min(offer_count, item_count.get(free_item, 0))
                            total_price -= free_item_count * price_table[free_item]['price']
                        count = remaining_count
                    else:
                        total_price += count * price
                        count = 0
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

def get_best_offer(offers, count):
    best_offer = None
    for offer in offers:
        if count >= offer['quantity']:
            # the best offer is the one with the highest quantity
            if not best_offer or offer['quantity'] > best_offer['quantity']:
                best_offer = offer
    return best_offer
