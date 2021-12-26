"""Thai Measurement"""

def meters1(meters_1):
    """measurement"""
    kueb = meters_1/0.25
    sok = meters_1/0.5
    wa_1 = meters_1/2
    sen = meters_1/40
    yot = meters_1/16000
    print("%d"%meters_1, "m")
    print("= %.3f"%kueb, "kueb")
    print("= %.3f"%sok, "sok")
    print("= %.3f"%wa_1, "wa")
    print("= %.3f"%sen, "sen")
    print("= %.3f"%yot, "yot")
    print()
meters1(200)
meters1(500)

def meters2(meters_2):
    """measurement"""
    kueb = meters_2/0.25
    sok = meters_2/0.5
    wa_1 = meters_2/2
    sen = meters_2/40
    yot = meters_2/16000
    print("%d"%(meters_2//10**3), "km")
    print("= %.3f"%kueb, "kueb")
    print("= %.3f"%sok, "sok")
    print("= %.3f"%wa_1, "wa")
    print("= %.3f"%sen, "sen")
    print("= %.3f"%yot, "yot")
    print()
meters2(1000)
meters2(2000)
meters2(5000)
