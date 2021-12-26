"""Locker"""

def main():
    """available"""
    full = int(input())
    use = int(input())
    empty = full-use
    ans = "X"*use+"O"*empty
    print(ans, "(available: %d)"%empty)
main()
