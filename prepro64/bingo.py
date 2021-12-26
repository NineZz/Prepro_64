"""RollingBingo!!"""
def bingo():
    """funnction bingo"""
    mylist = []
    i = 1
    while i <= 3:
        color = input().lower()
        mylist.append(color)
        i += 1
    count_1 = mylist.count("red")
    count_2 = mylist.count("blue")
    count_3 = mylist.count("green")
    count_4 = mylist.count("gold")
    if count_1 == 3:
        print("GiftVoucher")
    elif count_2 == 3:
        print("DoraemonDoll")
    elif count_3 == 3:
        print("FruitBasketBoxset")
    elif count_4 == 3:
        print("NintendoSwitch")
    elif count_1 == 1 and count_2 == 1 and count_3 == 1 or count_1 == 1 and count_3 == 1 and \
        count_4 == 1 or count_2 == 1 and count_3 == 1 and count_4 == 1 or count_1 == 1 and \
        count_2 == 1 and count_4 == 1:
        print("TissueBox")
    else:
        print("NoodleCups")
bingo()
