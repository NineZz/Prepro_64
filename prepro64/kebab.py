"""na is selling KEBAB"""

def main():
    """function"""
    price = int(input())
    number = int(input())
    word = input()
    nprice = price*number
    if "This kebab is very good" in word:
        print("%.2f"%(nprice*(70/100)))
    elif "This is not good not bad" in word:
        print("%.2f"%(nprice*(95/100)))
    elif "This is not kebab" in word:
        print("%.2f"%(nprice*(116/100)))
    else:
        print("0.00")
main()
