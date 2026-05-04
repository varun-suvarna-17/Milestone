from data import data
from processor import filter_purchases
from utils.helper import convert_to_float

from tasks import extract_amt, discount, apply_function

def main():
    purchases =  filter_purchases(data)
    print(f'Purchases list:')
    for purchase in purchases:
        print(purchase)

    amounts = extract_amt(data)
    amounts = convert_to_float(amounts)
    print(f'Amounts list (after coverting to float): {amounts}')

    discount_amt = discount(amounts)
    print(f'Amounts after discount: {discount_amt}')

    def add_50(amount):
        return amount + 50 

    extra_50 = apply_function(add_50, amounts)
    print(f'Amounts after adding 50: {extra_50}')

if __name__ == "__main__":
    main()