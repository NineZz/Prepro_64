"""Kanomwhan Bakery"""

def main(people, price, disc):
    """kanomwhan"""
    ans1 = people*price
    ans2 = people*price
    if people >= 3:
        ans1 = ans1-(ans1*disc/100)
    if people >= 4:
        ans2 = (people//4)*(3*price)+(people%4*price)
    if ans1 > ans2:
        print("Promotion 2 %.3f Baht"%ans2)
    else:
        print("Promotion 1 %.3f Baht"%ans1)
    print("Purchase successfully !")
    print("Have a good meal with \"Kanomwhan\"")
main(int(input()), float(input()), int(input()))
