"""Alphabet Order V.2"""

def main():
    """alphabet"""
    number_1 = int(input())
    number_2 = number_1+64
    alphabet_1 = chr(number_2)
    alphabet_2 = alphabet_1.lower()
    print("%s, %s"%(alphabet_2, alphabet_1))
main()
