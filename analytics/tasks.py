def extract_amt(data):
   return list(map(lambda x: x["amount"], data))



def discount(amount):
    return (list(map(lambda x: x * 0.9, amount)))


def apply_function(func, amt):
    new_amt = []
    for a in amt : 
        new_amt.append(func(a))
    return new_amt
