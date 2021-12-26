"""Way to travel"""
def check(distance):
    """way to travel"""
    if distance < 0:
        print("Error")
    elif 0 <= distance < 1:
        print("Walk")
    elif 1 <= distance < 20:
        print("Motorcycle")
    elif 20 <= distance < 300:
        print("Car")
    elif distance >= 300:
        print("Private jet")
def main():
    """fanction travel"""
    word_1 = input()
    word_2 = input()
    word_3 = float(input())
    if word_2 == "important":
        check(word_3)
    elif word_2 == "not important":
        if word_1 == "rainy":
            print("Not go")
        else:
            check(word_3)
main()
