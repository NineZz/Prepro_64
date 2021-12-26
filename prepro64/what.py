"""What is it then?"""
def main():
    """nan"""
    word = input()
    if word.isalpha():
        print("'"+word+"'", "is an alphabet.")
    elif word.isnumeric():
        print("'"+word+"'", "is numeric.")
    else:
        print("'"+word+"'", "is not both an alphabet and numeric.")
main()
