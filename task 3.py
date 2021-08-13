
list = [2, 5, 12, 14]


def check(N):
    for i in list:

        if i % N == 0:
            print(str(i) + " is divisible by 2")


N = 2
check(N)
