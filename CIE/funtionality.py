# TASK 1 

data = [
{"user_id": 1, "event_type": "purchase", "amount": 200},
{"user_id": 2, "event_type": "purchase", "amount": 500},
{"user_id": 3, "event_type": "login", "amount": 0}
]

# TASK 2 

def filter_purchases(data):
    purchases = [] 
    for event in data : 
        if event["event_type"] == "purchase":
            purchases.append(event)
    return purchases

# TASK 3 

def extract_amt(data):
   return list(map(lambda x: x["amount"], data))

# TASK 4 

def discount(amount):
    return (list(map(lambda x: x * 0.9, amount)))

# TASK 5 

def apply_function(func, amt):
    new_amt = []
    for a in amt : 
        new_amt.append(func(a))
    return new_amt

# RUNNING ALL THE FUNCTIONS 
def main():
    purchases =  filter_purchases(data)
    print(f'Purchases list:')
    for purchase in purchases:
        print(purchase)

    amounts = extract_amt(data)
    print(f'Amounts list: {amounts}')

    discount_amt = discount(amounts)
    print(f'Amounts after discount: {discount_amt}')

    def add_50(amount):
        return amount + 50 

    extra_50 = apply_function(add_50, amounts)
    print(f'Amounts after adding 50: {extra_50}')

if __name__ == "__main__":
    main()