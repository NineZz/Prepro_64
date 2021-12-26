"""Sandwich's Degrees"""

def main():
    """math"""
    import math
    num_1 = float(input())
    num_2 = float(input())
    ans_1 = math.atan(num_1/num_2)
    ans_2 = math.degrees(ans_1)
    print("%.2f deg"%ans_2)
main()
