"""กา กะ บาท"""
def main():
    """function X"""
    k = len(input())
    for i in range(1, k+1):
        for j in range(1, k+1):
            if j == 1 and not i == 2 or j == k or i == j:
                print(i, end=" ")
            else:
                print(" ", end=" ")
        print()
main()
