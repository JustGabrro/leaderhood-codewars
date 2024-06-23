def parts_sums(ls):
    result = []
    x_sum = sum(ls)
    
    for num in ls:
        result.append(x_sum)
        x_sum -= num
    result.append(0)
    return result