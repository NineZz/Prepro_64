"""โรงเรียนเวทย์มนต์เปิดรับสมัครแล้ว"""
def main():
    """function cut"""
    name = input()
    year = int(input())
    sex = input().lower()
    height = float(input())
    if 13 <= year <= 15:
        if sex == "male" and height >= 160:
            print("Mr. %s Age: %d Height: %.2f"%(name, year, height))
            print("You can study in junior high school.")
        elif sex == "female" and height >= 155:
            print("Miss %s Age: %d Height: %.2f"%(name, year, height))
            print("You can study in junior high school.")
        else:
            if sex == "male":
                print("Mr. %s Age: %d Height: %.2f"%(name, year, height))
                print("You can not join this school.")
            elif sex == "female":
                print("Miss %s Age: %d Height: %.2f"%(name, year, height))
                print("You can not join this school.")
    elif 16 <= year <= 18:
        if sex == "male" and height >= 170:
            print("Mr. %s Age: %d Height: %.2f"%(name, year, height))
            print("You can study in senior high school.")
        elif sex == "female" and height >= 165:
            print("Miss %s Age: %d Height: %.2f"%(name, year, height))
            print("You can study in senior high school.")
        else:
            if sex == "male":
                print("Mr. %s Age: %d Height: %.2f"%(name, year, height))
                print("You can not join this school.")
            elif sex == "female":
                print("Miss %s Age: %d Height: %.2f"%(name, year, height))
                print("You can not join this school.")
    else:
        if sex == "male":
            print("Mr. %s Age: %d Height: %.2f"%(name, year, height))
            print("You can not join this school.")
        elif sex == "female":
            print("Miss %s Age: %d Height: %.2f"%(name, year, height))
            print("You can not join this school.")
main()
