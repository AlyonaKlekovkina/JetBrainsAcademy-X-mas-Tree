# This is a sample Python script.
# import the required library
# This is a sample Python script.
# import the required library
height, interval = map(int, input().split())
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
        elif j % 2 != 0:
            if interval == 1 or (count % interval == 1):
                line += 'O'
                count += 1
            else:
                line += '*'
                count += 1
    print(line + '\\' + ' ' * (space - 1))
    n += 2
    space -= 1
print(' ' * (height - 2) + '|' + ' ' + '|' + ' ' * (height - 2))
