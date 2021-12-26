"""test"""
def main():
    """function test"""
    number = []
    max_input = 10
    i = 1
    while i <= max_input:
        n = int(input())
        number.append(n)
        i+=1
    sum = 0
    i = 1
    while i <= max_input:
        print(number[i-1], end = ', ')
        sum+= number[i-1]
        i+= 1
    print('\nSum = %d'%sum)
main()
