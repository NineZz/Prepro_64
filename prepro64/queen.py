"""Queen's way"""
def main():
    """function way"""
    for i in range(8):
        for j in range(8):
            if j == 0 or j == 4 or i == j:
                print("*", end= " ")
            else:
                print("|_", end= " ")
        print()
main()
