"""OG is waiting for you"""
def main():
    """function Q"""
    year = int(input())
    if 17 <= year <= 23:
        if year < 20:
            allow = input()
            if allow == "Y":
                play = int(input())
                if play >= 12:
                    travel = input()
                    if travel == "Y":
                        print("You can be in OG!")
                    else:
                        print("May be next time.")
                else:
                    print("May be next time.")
            else:
                print("May be next time.")
        elif year >= 20:
            play = int(input())
            if play >= 12:
                travel = input()
                if travel == "Y":
                    print("You can be in OG!")
                else:
                    print("May be next time.")
            else:
                print("May be next time.")
        else:
            print("May be next time.")
    else:
        print("May be next time.")
main()
