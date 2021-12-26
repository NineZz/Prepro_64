"""เอ้า herb herb herb"""

def check(number):
    """herb"""
    if number > 100:
        return 0
    else:
        return number
def main():
    """calculate"""
    num_1 = check(int(input()))
    num_2 = check(int(input()))
    num_3 = check(int(input()))
    num_4 = check(int(input()))
    num_5 = check(int(input()))
    num_6 = check(int(input()))
    num_7 = check(int(input()))
    num_8 = check(int(input()))
    num_9 = check(int(input()))
    num_10 = check(int(input()))
    ans = num_1+num_2+num_3+num_4+num_5+num_6+num_7+num_8+num_9+num_10
    if ans == 420:
        print("herb")
    else:
        print(ans)
main()
