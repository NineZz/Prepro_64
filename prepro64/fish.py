"""How much is this fish?"""

def main():
    """compute"""
    fish_1 = float(input())
    fish_2 = fish_1**2
    fish_3 = fish_1 / 10
    ans = (fish_2 + 5) / fish_3
    print("This fish is %.2f pokeCoins!"%ans)
main()
