def solution(x, y):
    count = 0
    m = int(x)
    n = int(y)

    while m != 1 or n != 1:
        if m == 1 or n == 1:
            if m == 1:
                count += n - 1
            if n == 1:
                count += m - 1
            break

        if m < n:
            if m == 0:
                return "impossible"
            count += n / m
            n %= m
        else:
            if n == 0:
                return "impossible"
            count += m / n
            m %= n

    return str(count)
