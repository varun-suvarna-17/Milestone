def filter_purchases(data):
    purchases = [] 
    for event in data : 
        if event["event_type"] == "purchase":
            purchases.append(event)
    return purchases

