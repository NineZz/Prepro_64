"""PvP"""

def main():
    """Option"""
    player_1 = input()
    hp_1 = int(input())
    atk_1 = int(input())
    def_1 = int(input())
    player_2 = input()
    hp_2 = int(input())
    atk_2 = int(input())
    def_2 = int(input())
    hp_3 = "O"*hp_1
    hp_4 = "O"*hp_2
    print("##############")
    print("# %10s #"%player_1)
    print("# HP:%7s #"%hp_3)
    print("# ATk || DEF #")
    print("# %04d||%04d #"%(atk_1, def_1))
    print("############## VS ##############")
    print("                  # %10s #"%player_2)
    print("                  # HP:%7s #"%hp_4)
    print("                  # ATk || DEF #")
    print("                  # %04d||%04d #"%(atk_2, def_2))
    print("                  ##############")
main()
