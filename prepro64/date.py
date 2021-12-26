"""Date of birth"""

def main():
    """Date of birth"""
    name = input()
    day = int(input())
    month = int(input())
    year_1 = int(input())
    year_2 = year_1-543
    print("\'%s\' %02d/%02d/%04d"%(name, month, day, year_2))
main()
