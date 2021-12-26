"""Apex pack"""
def main():
    """function pack"""
    level = int(input())
    if level <= 20:
        print(level-1, "Packs opened")
        print(500-(level-1), "Packs more")
    elif 21 <= level <= 300:
        print((19+((level-20)//2)), "Packs opened")
        print(500-(19+((level-20)//2)), "Packs more")
    elif 301 <= level <= 500:
        print(159+((level-300)//5), "Packs opened")
        print(500-(159+((level-300)//5)), "Packs more")
    elif level >= 500:
        print("199 Packs opened")
        print("301 Packs more")
main()
