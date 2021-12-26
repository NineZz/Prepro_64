"""Basic append"""
def main():
    """function append"""
    mylist = []
    max_input = int(input())
    i = 1
    while i <= max_input:
        word = input()
        mylist.append(word)
        i += 1
    for i in mylist:
        print(i, end=" ")
main()
