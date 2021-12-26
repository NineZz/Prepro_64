"""4 Mista"""
def mista():
    """function"""
    word_1 = input().lower()
    word_2 = input().lower()
    check_1 = word_1.find("four")
    check_2 = word_1.find("fourth")
    check_3 = word_1.find("4")
    check_4 = word_1.find("4th")
    if word_1.count(word_2) == 4:
        print("It's not safe four Mista....")
    elif check_1 >= 0:
        print("It's not safe four Mista....")
    elif check_2 >= 0:
        print("It's not safe four Mista....")
    elif check_3 >= 0:
        print("It's not safe four Mista....")
    elif check_4 >= 0:
        print("It's not safe four Mista....")
    else:
        print("MISTA, THIS ONE'S 4 U.")
mista()
