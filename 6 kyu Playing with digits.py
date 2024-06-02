def dig_pow(n, p):
    x = str(n)
    x_sum = sum(int(x[i]) ** (p + i) for i in range(len(x)))
    if x_sum % n == 0:
        return x_sum // n
    else:
        return -1