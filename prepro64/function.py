"""Composite Function"""

def main():
    """function fog"""
    number = float(input())
    sol_1 = (number**3)+(4*number)-1
    sol_2 = (15+sol_1-sol_1**3)/((sol_1**2/3)+11)
    sol_3 = (15+number-number**3)/((number**2/3)+11)
    sol_4 = (sol_3**3)+(4*sol_3)-1
    print("%.4f"%sol_2)
    print("%.4f"%sol_4)
main()
