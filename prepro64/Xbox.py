"""Xbox"""
def main():
    """function xbox"""
    for i in range(5):
        for j in range(5):
            if j == 0 or j == 4 or i == 0 or i == 4 or i == j or\
                 i == 1 and j == 3 or i == 3 and j == 1:
                print("*", end= " ")
            else:
                print(" ", end= " ")
        print()
main()
