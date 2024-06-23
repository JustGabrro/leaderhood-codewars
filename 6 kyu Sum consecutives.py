def sum_consecutives(lst):
    result = []
    sum = lst[0]
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            sum += lst[i]
        else:
            result.append(sum)
            sum = lst[i]
    result.append(sum)
    return result