"""Just MAX it V.4"""
def check(xxxx, yyyy):
    """function check"""
    return xxxx > yyyy and xxxx or yyyy
def main():
    """function max"""
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    num_4 = float(input())
    num_5 = float(input())
    num_6 = float(input())
    num_7 = float(input())
    num_8 = float(input())
    num_9 = float(input())
    num_10 = float(input())
    print("%.2f"%check(check(check(check(check(check(check(check(check(num_1, num_2), \
        num_3), num_4), num_5), num_6), num_7), num_8), num_9), num_10))
main()
