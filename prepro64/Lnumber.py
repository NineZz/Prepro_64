"""L's number"""

def main():
    """code"""
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    num_4 = int(input())
    first = num_1//10**4
    second = num_2//10**4
    third = num_3//10**4
    fourth = num_4//10**4
    fourth_1 = num_4%10**4//10**3
    fourth_2 = num_4%10**3//10**2
    fourth_3 = num_4%10**2//10
    ans = first+second+third+fourth+fourth_1+fourth_2+fourth_3
    print(ans)
main()
