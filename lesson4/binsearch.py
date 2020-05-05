def binsearch(a, x):
    left, right = 0, len(a)
    while 1:
        pos = (right + left) // 2
        if left+1 == right:
            return pos if a[pos] == x else -1

        if a[pos] > x:
            right = pos
        elif a[pos] < x:
            left = pos
        else:
            return pos


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
a = [9]
a = [-1]

print(binsearch(a, -10))
print(binsearch(a, 9))
print(binsearch(a, 25))
