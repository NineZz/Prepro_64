"""Final Battle"""

def main():
    """function"""
    ben99 = int(input())
    gwen10 = int(input())
    all10 = gwen10*(int(input()))/100
    goku = int(input())
    if all10 + goku > ben99:
        print("The world is save!")
    elif all10 + goku == ben99:
        print("The world is save but we lost our hero.")
    else:
        print("Ben 99 is going to ruin the world.")
main()
