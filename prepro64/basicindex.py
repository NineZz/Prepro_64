"""Basic index"""
def main():
    """function index"""
    i = 1
    wordlist = []
    while i >= 0:
        word_1 = input()
        wordlist.append(word_1)
        word_2 = word_1.lower()
        if word_2 == "end":
            break
    wordlist.pop()
    number = int(input())
    if number <= len(wordlist)-1:
        print('List[%d] = "%s"'%(number, wordlist[number]))
    else:
        print("Index Not Found")
main()
