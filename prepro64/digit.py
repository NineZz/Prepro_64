"""How many digit?"""

def main(number):
    """digit"""
    num_1 = str(number).replace(".", "")
    num_2 = str(num_1).replace("-", "")
    num_3 = num_2+"a"
    num_4 = num_3.index("a")
    print(num_4)
main(input())
