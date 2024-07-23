def create_tree(height, interval):
    count = 1
    n = 1
    space = height - 1
    print(' ' * space + 'X' + ' ' * space)
    print(' ' * space + '^' + ' ' * space)
    for i in range(height - 1):
        line = ' ' * (space - 1) + '/'
        for j in range(n):
            if j % 2 == 0:
                line += '*'
            elif interval == 1 or (count % interval == 1):
                line += 'O'
                count += 1
            else:
                line += '*'
                count += 1
        print(line + '\\' + ' ' * (space - 1))
        n += 2
        space -= 1
    print(' ' * (height - 2) + '|' + ' ' + '|' + ' ' * (height - 2))


def add_tree(height, interval):
    count = 1
    n = 1
    space = (height-1)
    line = []
    for j in range(height + 2):
        line.append([])
        if j == 0:
            for i in range(space):
                line[j].append(' ')
            line[j].append('X')
            for i in range(space):
                line[j].append(' ')
        elif j == 1:
            for i in range(space):
                line[j].append(' ')
            line[j].append('^')
            for i in range(space):
                line[j].append(' ')
        elif j == (height + 1):
            for i in range(height - 2):
                line[j].append(' ')
            line[j].append('|')
            line[j].append(' ')
            line[j].append('|')
            for i in range(height-2):
                line[j].append(' ')
        else:
            for i in range(space-1):
                line[j].append(' ')
            line[j].append('/')
            for k in range(n):
                if k % 2 == 0:
                    line[j].append('*')
                elif k % 2 != 0:
                    if interval == 1 or (count % interval == 1):
                        line[j].append('O')
                        count += 1
                    else:
                        line[j].append('*')
                        count += 1
            line[j].append('\\')
            for i in range(space-1):
                line[j].append(' ')
            n += 2
            space -= 1
    return line


def create_space_card(width, height):
    postcard = []
    for i in range(height):
        postcard.append([])
        for j in range(width):
            postcard[i].append(" ")
    return postcard


def draw_horizontal_line(postcard, n):
    for i in range(len(postcard[n])):
        postcard[n][i] = '-'


def draw_vertical_line(postcard, n):
    for i in range(len(postcard)):
        postcard[i][n] = '|'


def write_text(postcard, phrase, n):
    width = len(postcard[n])
    c = (width // 2) - (len(phrase) // 2)
    for j in range(len(phrase)):
        postcard[n][c] = phrase[j]
        c += 1


def draw_xmass_tree(postcard, height, interval, line, column):
    the_tree = add_tree(height, interval)
    n = height - 1
    for i in range(0, height+2):
        for j in range(0, height+height-1):
            k = j - n
            if line + i < len(postcard) and column + k < len(postcard[0]) and column + k > 0 and the_tree[i][j] != ' ':
                postcard[line + i][column+k] = the_tree[i][j]


inp = input().split()
if len(inp) == 2:
    h = int(inp[0])
    i = int(inp[1])
    create_tree(h, i)
else:
    pc = create_space_card(50, 30)
    p = 0
    for i in range(len(inp) // 4):
        draw_xmass_tree(pc, int(inp[p]), int(inp[p+1]), int(inp[p+2]), int(inp[p+3]))
        p += 4
    draw_vertical_line(pc, 0)
    draw_vertical_line(pc, 49)
    draw_horizontal_line(pc, 0)
    draw_horizontal_line(pc, 29)
    write_text(pc, 'Merry Xmas', 27)
    for j in pc:
        print(*j, sep = "")
