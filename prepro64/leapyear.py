"""Do you know leap year?"""
def main():
    """function leap"""
    year = int(input())
    if year%100 == 0:
        if year%400 == 0:
            print("%d"%year, "is a leap year.")
        else:
            print("%d"%year, "is not a leap year.")
    else:
        if year%4 == 0:
            print("%d"%year, "is a leap year.")
        else:
            print("%d"%year, "is not a leap year.")
main()
