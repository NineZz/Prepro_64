"""Secret code"""

def main():
    """code"""
    password = int(input())
    num_1 = str(password%10**9//10**8)
    num_2 = str(password%10**7//10**6)
    num_3 = str(password%10**5//10**4)
    num_4 = str(password%10**3//10**2)
    num_5 = str(password%10)
    print(num_1+num_2+num_3+num_4+num_5)
main()
