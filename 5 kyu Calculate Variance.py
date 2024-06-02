def variance(numbers): 
    result = sum(numbers) / len(numbers)
    x_diff = []
    for y in numbers:
        diff = y - result
        x_diff.append(diff ** 2)
    sum_x_diff = sum(x_diff)
    last = sum_x_diff / len(numbers)
    return last