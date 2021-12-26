"""What grade?"""

def main():
    """grade"""
    score = int(float(input()))
    if 80 <= score:
        print("A")
    elif 79 >= score >= 75:
        print("B+")
    elif 74 >= score >= 70:
        print("B")
    elif 69 >= score >= 65:
        print("C+")
    elif 64 >= score >= 60:
        print("C")
    elif 59 >= score >= 55:
        print("D+")
    elif 54 >= score >= 50:
        print("D")
    elif 50 > score:
        print("F")
main()
