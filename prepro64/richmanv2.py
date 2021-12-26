"""Richman V.2"""

def main():
    """moneyyyyyy"""
    money_1 = input()
    money_2 = money_1.replace(",", "")
    money_3 = money_2.replace("-", "")
    money_4 = money_3.lstrip("0")
    money_5 = len(money_4)
    print(money_5)
main()
