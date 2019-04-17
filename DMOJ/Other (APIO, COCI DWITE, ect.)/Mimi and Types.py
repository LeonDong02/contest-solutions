    import sys


    def input():
        return sys.stdin.readline().strip()


    s = list(map(int, list(input())))
    c = s[0]
    for i in range(1, len(s)):
        c -= 1
        if c < 0:
            print('Invalid')
            sys.exit()
        c += s[i]
    print('Valid' if not c else 'Invalid')
