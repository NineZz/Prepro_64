"""สมการตัวน้อย V.2"""

def main():
    """calculate"""
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    num_4 = int(input())
    num_5 = int(input())
    num_6 = int(input())
    cal = (((num_2/((num_1**2)/num_4))+\
        (num_5*(num_2/num_1)))*num_6)/(num_6*num_3)
    print("%.2f"%cal)
main()
