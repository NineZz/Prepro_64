"""Lucky One V.1"""

def main():
    """function main"""
    word_1 = input()
    number = int(input())
    word_2 = word_1.replace(" ", "")
    word_3 = word_2[number-1]
    print(word_3.lower())
main()
