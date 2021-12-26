"""Aladin & The Magic Burger (Extra)"""

def main():
    """burger"""
    bur = input().lower()
    ger = bur.find("b")
    ala = len(bur)%10
    print("(|"*ala + "{}"*ger + "|)"*ala)
main()
