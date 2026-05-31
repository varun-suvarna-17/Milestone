from data import data
from processor import filter_purchases
from utils.helper import convert_to_float
from tasks import extract_amt, discount, apply_function

def main():
    try:
        purchases =  filter_purchases(data)
        #emppty condition
        if not purchases:
            print("No purchases found.")
        else:
            print(f'Purchases list:')
            for purchase in purchases:
                print(purchase)
       
       # all amount values 
        amounts = extract_amt(data)
        amounts = convert_to_float(amounts)
        print(f'Amounts list (after coverting to float): {amounts}')
       
        # discounted amounts
        discount_amt = discount(amounts)
        print(f'Amounts after discount: {discount_amt}')

        # applying higher order function
        def add_50(amount):
            return amount + 50 
    
        extra_50 = apply_function(add_50, amounts)
        print(f'Amounts after adding 50: {extra_50}')

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        print("Analytics processing completed.")

if __name__ == "__main__":
    main()