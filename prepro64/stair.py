"""Stairs V.1"""
def main(number):
    """function stairs"""
    for i in range(1, number+1):
        for number in range(1, i+1):
            print(i, end="")
        print()
main(int(input()))
