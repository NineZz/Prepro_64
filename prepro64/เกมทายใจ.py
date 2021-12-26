"""เกมทายใจ"""
def main():
    """function guess"""
    number = int(input())
    max_input = int(input())
    i = 1
    while i <= max_input:
        word = int(input())
        if word != number:
            i += 1
        elif word == number:
            print("Yes! It is %d."%number)
            break
    if word != number:
        print("No more chances. You lose.")
main()
