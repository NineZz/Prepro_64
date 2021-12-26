"""Nintendo Battery"""
def main():
    """function battery"""
    battery = int(input())
    max_range = int(input())
    num_1 = int((battery/100)*max_range)
    print("(%s%s) %d"%("O"*num_1, \
        "_"*(max_range-num_1), battery)+"%")
main()
