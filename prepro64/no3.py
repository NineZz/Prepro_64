"""ซูม หรือ ซัม V.2"""

def main():
    """calculate"""
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    if num_1 == num_2 == num_3:
        print("0")
    elif num_1 == num_2:
        print(num_3)
    elif num_1 == num_3:
        print(num_2)
    elif num_2 == num_3:
        print(num_1)
    else:
        print(num_1+num_2+num_3)
main()
