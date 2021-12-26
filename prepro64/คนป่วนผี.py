"""คน ป่วน ผี"""

def main():
    """function"""
    number = int(input())
    num_1 = ((number%10**5)//(10**4))
    num_2 = ((number%10**4)//(10**3))
    num_3 = ((number%10**3)//(10**2))
    num_4 = ((number%10**2)//(10**1))
    num_5 = (number%10)
    ans = (num_1+num_2+num_3+num_4+num_5)
    if ans%2 == 0 and ans%4 == 0:
        print("ผีตานี")
    elif ans%2 == 0 and ans%4 != 0:
        print("ผีกระหัง")
    elif ans%2 != 0 and ans%5 == 0:
        print("ผีกระสือ")
    elif ans%2 != 0 and ans%5 != 0:
        print("ผีปอบ")
main()
