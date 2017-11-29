from collections import deque

RIGHT = 1
LEFT = -1

f = open("p21.input")
inputs = [l.strip() for l in f.readlines()]


def swap_pos(s, x, y):
    new_pwd = list(s)
    new_pwd[x], new_pwd[y] = s[y], s[x]
    return ''.join(new_pwd)

def swap_letter(s, x, y):
    new_pwd = ""
    for c in s:
        if c == x:
            c = y
        elif c == y:
            c = x
        new_pwd += c
    return new_pwd

def rotate_dir(s, d, x):
    new_pwd = deque(s)
    new_pwd.rotate(d*(x%len(s)))
    return ''.join(new_pwd)

def rotate_pos(s, x):
    i = s.index(x)
    num_rots = 2 + i if i >= 4 else 1 + i
    return rotate_dir(s, RIGHT, num_rots)

def rev_pos(s, x, y):
    return s[:x] + s[x:y+1][::-1] + s[y+1:]

def mov_pos(s, x, y):
    new_pwd = list(s)
    c = new_pwd.pop(x)
    return ''.join(new_pwd[:y] + [c] + new_pwd[y:])

pwd = 'abcdefgh'
rev_pwd = [pwd]

for i in inputs:

    # swap
    if i[0] == 's':

        # letter or pos?
        if i[5] == 'p':
            x, y = int(i[14]), int(i[30])
            pwd = swap_pos(pwd, x, y)
        else:
            x, y = i[12], i[26]
            pwd = swap_letter(pwd, x, y)
    # rotate/reverse
    elif  i[0] == 'r':

        # rev
        if i[1] == 'e':
            x, y = int(i[18]), int(i[28])
            pwd = rev_pos(pwd, x, y)
            
        # rotate dir
        elif i[7] == 'l':
            x = int(i[12])
            pwd = rotate_dir(pwd, LEFT, x)
        elif i[7] == 'r':
            x = int(i[13])
            pwd = rotate_dir(pwd, RIGHT, x)
        # rotate pos
        else:
            x = i[len(i)-1]
            pwd = rotate_pos(pwd, x)
    #mov_pos
    elif  i[0] == 'm':
        x, y = int(i[14]), int(i[28])
        pwd = mov_pos(pwd, x, y)
    
    rev_pwd = [pwd] + rev_pwd

    #print pwd
print "Final password:", pwd

for p in rev_pwd:
    print p
    

    
    


