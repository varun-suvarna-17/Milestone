def extract_amt(data):
    try:
        return list(map(lambda x: x["amount"], data))
    except KeyError as ke:
        print(f"Field 'amount' not found in data: {ke}")
        

def discount(amount):
    try:
        return list(map(lambda x: x * 0.9, amount))
    except TypeError as te:
        print(f"Type error in discount: {te}")


def apply_function(func, amt):
    new_amt = []
    for a in amt : 
        new_amt.append(func(a))
    return new_amt
