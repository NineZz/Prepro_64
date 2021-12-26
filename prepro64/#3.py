"""#3"""
def main():
    """function count"""
    upper_range = int(input())
    number = int(input())
    mylist = []
    for i in range(upper_range+1):
        mylist.append(i)
        count = mylist.count(number)
    print(count)
main()
