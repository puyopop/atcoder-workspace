X = int(input())

def f(x):
    i = 0
    while x < X:
        i += 1
        x = int(x * 1.01)
    return i

print(f(100))
