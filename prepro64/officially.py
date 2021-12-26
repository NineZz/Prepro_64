"""Officially! #7echnaldooooo"""
def main():
    """นายเทค"""
    pain = input().lower()
    if pain == "y":
        print("you will unavaliable")
    elif pain == "n":
        time = input().lower()
        if time == "n":
            print("you will be a starter")
        elif time == "y":
            work = input().lower()
            if work == "y":
                print("you will be a substitute ")
            elif work == "n":
                print("you won't be selected")
main()
