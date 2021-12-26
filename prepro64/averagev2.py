"""Just a normal average day V.2"""

def main(num_1, num_2, num_3, num_4, num_5):
    """years"""
    print("CHILD"*(num_1 < 7)+"TEENAGER"*(7 <= num_1 < 25)+ \
        "ADULT"*(25 <= num_1 < 59)+"ELDER"*(num_1 >= 59))
    print("CHILD"*(num_2 < 7)+"TEENAGER"*(7 <= num_2 < 25)+ \
        "ADULT"*(25 <= num_2 < 59)+"ELDER"*(num_2 >= 59))
    print("CHILD"*(num_3 < 7)+"TEENAGER"*(7 <= num_3 < 25)+ \
        "ADULT"*(25 <= num_3 < 59)+"ELDER"*(num_3 >= 59))
    print("CHILD"*(num_4 < 7)+"TEENAGER"*(7 <= num_4 < 25)+ \
        "ADULT"*(25 <= num_4 < 59)+"ELDER"*(num_4 >= 59))
    print("CHILD"*(num_5 < 7)+"TEENAGER"*(7 <= num_5 < 25)+ \
        "ADULT"*(25 <= num_5 < 59)+"ELDER"*(num_5 >= 59))
main(abs(int(input())), abs(int(input())), abs(int(input())), \
    abs(int(input())), abs(int(input())))
