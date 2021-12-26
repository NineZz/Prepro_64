"""Just MAX it V.2"""

def main():
    """no max"""
    num_1 = float(input())
    num_2 = float(input())
    print(("%.3f"%num_1)*(num_1 > num_2)+(("%.3f"%num_2)*(num_2 > num_1)))
main()
