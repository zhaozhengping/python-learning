# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。


def reduceNum(n):
    print("{} = ".format(n))
    if not isinstance(n, int) or n <= 0:
        print("input an integer:")
        exit(0)
    elif n in[1]:
        print("{}".format(n))
    while n not in [1]:
        for index in range(2, int(n+1)):
            if n % index == 0:
                n /= index
                if n == 1:
                    print(index)
                else:
                    print("{} *".format(index)),
                break
reduceNum(90)
reduceNum(100)