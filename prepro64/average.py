"""Just a normal average day V.1"""

def main():
    """averange"""
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    num_4 = float(input())
    num_5 = float(input())
    num_6 = float(input())
    avg = (num_1+num_2+num_3+num_4+num_5+num_6)/6
    print("max : %.2f"%max(num_1, num_2, num_3, num_4, num_5, num_6))
    print("min : %.2f"%min(num_1, num_2, num_3, num_4, num_5, num_6))
    print("sum : %.2f"%(num_1+num_2+num_3+num_4+num_5+num_6))
    print("avg : %.4f"%avg)
main()
