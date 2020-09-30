import sys

while True:
    def playermove1():
        global q,w,e,a,s,d,z,x,c,list,move
        if move in list:
            print("There is already a mark there!")
            p1()
        if move not in list:
            list.append(move)
            if move == 'q':q= 'X'
            if move == 'w': w = 'X'
            if move == 'e': e = 'X'
            if move == 'a': a = 'X'
            if move == 's': s = 'X'
            if move == 'd': d = 'X'
            if move == 'z': z = 'X'
            if move == 'x': x = 'X'
            if move == 'c': c = 'X'
            print(
                '-----------\n',
                q, '|', w, '|', e,
                '\n-----------\n',
                a, '|', s, '|', d,
                '\n-----------\n',
                z, '|', x, '|', c,
                '\n-----------')
    def playermove2():
        global q,w,e,a,s,d,z,x,c
        if move in list:
            print("There is already a mark there!")
            p2()
        if move not in list:
            list.append(move)
            if move == 'q':q= 'O'
            if move == 'w': w = 'O'
            if move == 'e': e = 'O'
            if move == 'a': a = 'O'
            if move == 's': s = 'O'
            if move == 'd': d = 'O'
            if move == 'z': z = 'O'
            if move == 'x': x = 'O'
            if move == 'c': c = 'O'
            print(
                '-----------\n',
                q, '|', w, '|', e,
                '\n-----------\n',
                a, '|', s, '|', d,
                '\n-----------\n',
                z, '|', x, '|', c,
                '\n-----------')
    def play():
        global player1, firstone, q, w, e, a, s, d, z, x, c, list, move
        q = w = e = a = d = z = x = c = s = ' '
        list = []
        move = ''
        firstone = input("Who go first? X/O: ").upper()
        print(firstone)
        if firstone != 'X' and firstone != 'O':
            print('Please type X/O only!')
            play()
    def won():
        result = input('Play again?(Y/N): ').upper()
        if result == 'Y':
            play()
        if result == 'N':
            sys.exit()
    def p1():
        if q == w == e == 'X' or a == s == d == 'X' or z == x == c == 'X' or q == s == c == 'X' or e == s == z == 'X' or q == a == z == 'X' or w == s == x == 'X' or e == d == c == 'X' or q == w == e == 'O' or a == s == d == 'O' or z == x == c == 'O' or q == s == c == 'O' or e == s == z == 'O' or q == a == z == 'O' or w == s == x == 'O' or e == d == c == 'O':
            print('X won!')
            won()
        if ' ' not in (q,w,e,a,s,d,z,x,c):
            print('Out of space :(')
            won()
        global move
        move = input("Input your 'X' location: ")
        print(move)
        if len(move) != 1 or move not in ('q,w,e,a,s,d,z,x,c'):
            print('Enter in range q,w,e,a,s,d,z,x,c only!')
            p1()
        playermove1()
        p2()
    def p2():
        if q == w == e == 'X' or a == s == d == 'X' or z == x == c == 'X' or q == s == c == 'X' or e == s == z == 'X' or q == a == z == 'X' or w == s == x == 'X' or e == d == c == 'X' or q == w == e == 'O' or a == s == d == 'O' or z == x == c == 'O' or q == s == c == 'O' or e == s == z == 'O' or q == a == z == 'O' or w == s == x == 'O' or e == d == c == 'O':
            print('O won!')
            won()
        if ' ' not in (q, w, e, a, s, d, z, x, c):
            print('Out of space :(')
            won()
        global move
        move = input("Input your 'O' location: ")
        if len(move) != 1 or move not in ('q,w,e,a,s,d,z,x,c'):
            print('Enter in range q,w,e,a,s,d,z,x,c only!')
            p2()
        playermove2()
        p1()
    play()
    if firstone == 'X':
        p1()
    elif firstone == 'O':
        p2()

