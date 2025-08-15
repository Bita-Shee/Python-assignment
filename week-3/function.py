def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        return price - (price * discount_percent / 100)
    else:
        return price
    
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percent: "))

final_price = calculate_discount(price, discount_percent)

print("Final price:", final_price)