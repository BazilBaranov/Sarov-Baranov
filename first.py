def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    for i in range(1, int(input())+1):
        print(f"Число Фиб №{i}, ", fib(i))


if __name__ == '__main__':
    main()
