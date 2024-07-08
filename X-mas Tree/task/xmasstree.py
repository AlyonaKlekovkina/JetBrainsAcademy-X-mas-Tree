# This is a sample Python script.
# import the required library
height = int(input())
n = 1
space = height - 1
print(' ' * space + 'X' + ' ' * space)
print(' ' * space + '^' + ' ' * space)
for i in range(height - 1):
    print(' ' * (space - 1) + '/' + '*' * n + '\\' + ' ' * (space -1))
    n += 2
    space -= 1
print(' ' * (height - 2) + '|' + ' ' + '|' + ' ' * (height - 2))
