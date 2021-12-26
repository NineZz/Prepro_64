"""Orange Cake"""

def main():
    """money"""
    money = float(input())
    price = float(input())
    num_1 = int(money/price)
    num_2 = num_1*price
    num_3 = money-num_2
    if money >= price:
        print("Orange Cake: %d"%num_1)
        print("Money left: %d"%num_3)
    else:
        print("Not enough money;(")
        print("Money left: %d"%money)
main()
