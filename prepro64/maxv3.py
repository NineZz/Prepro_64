"""Just MAX it V.3"""

def main(xxxx, yyyy):
    """function min"""
    zzzz = min(xxxx, yyyy)
    sus = (xxxx+yyyy)-zzzz
    return sus

def number():
    """function input"""
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    num_4 = float(input())
    num_5 = float(input())
    num_6 = float(input())
    num_7 = float(input())
    num_8 = float(input())
    ans = main(main(main(main(main(main(main(num_1, num_2), num_3), \
        num_4), num_5), num_6), num_7), num_8)
    print("%.2f"%ans)
number()
