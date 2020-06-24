def occup(first1, second1, str1):
    if first1 == 1 and second1 == 1 and str1[6] != '_':
        print('This cell is occupied! Choose another one!')
        return 0
    if first1 == 1 and second1 == 2 and str1[3] != '_':
        print('This cell is occupied! Choose another one!')
        return 0
    if first1 == 1 and second1 == 3 and str1[0] != '_':
        print('This cell is occupied! Choose another one!')
        return 0
    if first1 == 2 and second1 == 3 and str1[1] != '_':
        print('This cell is occupied! Choose another one!')
        return 0
    if first1 == 2 and second1 == 2 and str1[4] != '_':
        print('This cell is occupied! Choose another one!')
        return 0
    if first1 == 2 and second1 == 1 and str1[7] != '_':
        print('This cell is occupied! Choose another one!')
        return 0
    if first1 == 3 and second1 == 1 and str1[8] != '_':
        print('This cell is occupied! Choose another one!')
        return 0
    if first1 == 3 and second1 == 2 and str1[5] != '_':
        print('This cell is occupied! Choose another one!')
        return 0
    if first1 == 3 and second1 == 3 and str1[2] != '_':
        print('This cell is occupied! Choose another one!')
        return 0


def the_table(answer):
    print('---------')
    c = 0
    for i in answer:
        if c % 3 == 0:
            print('| ', end='')
        print(i, end=' ')
        c = c + 1
        if c % 3 == 0:
            print('|')
    print('---------')


def put_X(first1, second1, str1):
    new_list = list(str1)
    if first1 == 1 and second1 == 1:
        new_list[6]='X';
        str1 = "".join(new_list)
        return str1
    if first1 == 1 and second1 == 2:
        new_list[3] = 'X';
        str1 = "".join(new_list)
        return str1
    if first1 == 1 and second1 == 3:
        new_list[0] = 'X';
        str1 = "".join(new_list)
        return str1
    if first1 == 2 and second1 == 3:
        new_list[1] = 'X';
        str1 = "".join(new_list)
        return str1
    if first1 == 2 and second1 == 2:
        new_list[4] = 'X';
        str1 = "".join(new_list)
        return str1
    if first1 == 2 and second1 == 1:
        new_list[7] = 'X';
        str1 = "".join(new_list)
        return str1
    if first1 == 3 and second1 == 1:
        new_list[8] = 'X';
        str1 = "".join(new_list)
        return str1
    if first1 == 3 and second1 == 2:
        new_list[5] = 'X';
        str1 = "".join(new_list)
        return str1
    if first1 == 3 and second1 == 3:
        new_list[2] = 'X';
        str1 = "".join(new_list)
        return str1


x = 0
o = 0
imp = 0
who_wins = ''


answer = input('Enter cells: >')
the_table(answer)

for i in answer:
    if i == 'X':
        x = x + 1
    if i == 'O':
        o = o + 1

if abs(x - o) >= 2:
    imp = 1

if answer[0] == answer[1] and answer[0] == answer[1]:
    if who_wins != '':
        imp = 1
    elif answer[0] == 'X':
        who_wins = 'X'
    elif answer[0] == 'O':
        who_wins = 'O'
if answer[0] == answer[3] and answer[0] == answer[6]:
    if who_wins != '':
        imp = 1
    if answer[0] == 'X':
        who_wins = 'X'
    elif answer[0] == 'O':
        who_wins = 'O'
if answer[0] == answer[4] and answer[0] == answer[8]:
    if who_wins != '':
        imp = 1
    if answer[0] == 'X':
        who_wins = 'X'
    elif answer[0] == 'O':
        who_wins = 'O'
if answer[4] == answer[3] and answer[4] == answer[5]:
    if who_wins != '':
        imp = 1
    if answer[4] == 'X':
        who_wins = 'X'
    elif answer[4] == 'O':
        who_wins = 'O'
if answer[4] == answer[1] and answer[4] == answer[7]:
    if who_wins != '':
        imp = 1
    if answer[4] == 'X':
        who_wins = 'X'
    elif answer[4] == 'O':
        who_wins = 'O'
if answer[4] == answer[2] and answer[4] == answer[6]:
    if who_wins != '':
        imp = 1
    if answer[4] == 'X':
        who_wins = 'X'
    elif answer[4] == 'O':
        who_wins = 'O'
if answer[8] == answer[5] and answer[8] == answer[2]:
    if who_wins != '':
        imp = 1
    if answer[8] == 'X':
        who_wins = 'X'
    elif answer[8] == 'O':
        who_wins = 'O'
if answer[8] == answer[7] and answer[8] == answer[6]:
    if who_wins != '':
        imp = 1
    if answer[8] == 'X':
        who_wins = 'X'
    elif answer[8] == 'O':
        who_wins = 'O'

# if imp == 1:
#    print('Impossible')
# elif who_wins == 'X':
#    print('X wins')
# elif who_wins == 'O':
#   print('O wins')
# elif x + o != 9:
#    print('Game not finished')
# else:
#    print('Draw')
flag = 1
while flag == 1:
    first = 0
    second = 0
    flag = 0
    move = input('Enter the coordinates: >')
    move = move.strip()
    lst = move.split()

    if lst[0].isdigit() and lst[1].isdigit():
        first = int(lst[0])
        second = int(lst[1])
        if first not in [1, 2, 3] or second not in [1, 2, 3]:
            print('Coordinates should be from 1 to 3!')
            flag = 1
    else:
        print('You should enter numbers!')
        flag = 1
    if occup(first, second, answer) == 0:
        flag = 1

    if flag == 0:
        new_table = put_X(first, second, answer)
        the_table(new_table)

