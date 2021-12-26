"""All of prime"""
def main():
    """function prime"""
    num_1 = int(input())
    num_2 = int(input())
    while(num_1 <= num_2):
        count = 0
        i = 2
        while(i <= num_1//2):
            if (num_1%i == 0):
                count = count+1
                break
            i+= 1
        if (count == 0 and num_1 != 1):
            print("%d"%num_1, end = ' ')
        num_1+=1
    print("\nsum of prime = %s"%sum)
main()
