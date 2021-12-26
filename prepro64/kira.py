"""Kira's Number"""
def main():
    """function number"""
    number_1 = input()
    number_2 = int(number_1)
    num_1 = (number_2%10**20)//(10**19)
    num_2 = (number_2%10**19)//(10**18)
    num_3 = (number_2%10**18)//(10**17)
    num_4 = (number_2%10**17)//(10**16)
    num_5 = (number_2%10**16)//(10**15)
    num_6 = (number_2%10**15)//(10**14)
    num_7 = (number_2%10**14)//(10**13)
    num_8 = (number_2%10**13)//(10**12)
    num_9 = (number_2%10**12)//(10**11)
    num_10 = (number_2%10**11)//(10**10)
    num_11 = (number_2%10**10)//(10**9)
    num_12 = (number_2%10**9)//(10**8)
    num_13 = (number_2%10**8)//(10**7)
    num_14 = (number_2%10**7)//(10**6)
    num_15 = (number_2%10**6)//(10**5)
    num_16 = (number_2%10**5)//(10**4)
    num_17 = (number_2%10**4)//(10**3)
    num_18 = (number_2%10**3)//(10**2)
    num_19 = (number_2%10**2)//(10**1)
    num_20 = (number_2%10)
    ans_1 = num_1+num_2+num_3+num_4+num_5+num_6+num_7+num_8+num_9+num_10+\
        num_11+num_12+num_13+num_14+num_15+num_16+num_17+num_18+num_19+num_20
    ans_2 = ans_1**3
    number_5 = (number_2%10**20)//(10**15)
    ans_3 = ans_2+number_5
    ans_4 = str(ans_3)
    if len(ans_4) >= 5:
        print(ans_4[0:5])
    elif len(ans_4) < 5:
        number_5_2 = 5-len(ans_4)
        print("0"*number_5_2+ans_4)
main()
