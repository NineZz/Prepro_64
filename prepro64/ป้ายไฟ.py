"""ป้ายไฟ"""

def main():
    """function"""
    word_1 = input()
    word_2 = word_1.upper()
    num_1 = len(word_1)
    num_2 = num_1+4
    print("|%s|"%("-"*num_2))
    print("|  %s  |"%word_2)
    print("|%s|"%("-"*num_2))
main()
