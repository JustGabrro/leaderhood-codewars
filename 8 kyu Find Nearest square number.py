def nearest_sq(n):
    lower = int(n ** 0.5) ** 2
    upper = (int(n ** 0.5) + 1) ** 2
    return lower if n - lower < upper - n else upper