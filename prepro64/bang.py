"""แบง แบงค์ bang"""

def main():
    """bang"""
    money = int(input())
    num_1 = money//1000
    print(num_1)
    num_1 = money%1000
    num_2 = num_1//500
    print(num_2)
    num_2 = num_1%500
    num_3 = num_2//100
    print(num_3)
    num_3 = num_2%100
    num_4 = num_3//50
    print(num_4)
    num_4 = num_3%50
    num_5 = num_4//20
    print(num_5)
main()
