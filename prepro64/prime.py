"""PRIME!!!"""
def main():
    """function prime"""
    number = int(input())
    if number > 1:
        for i in range(2, number//2):
            if (number%i) == 0:
                print(number, "is not prime number")
                break
        else:
            print(number, "is prime number")
    else:
        print(number, "is not prime number")
main()
