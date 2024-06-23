def valid_ISBN10(isbn): 
    if len(isbn) != 10:
        return False
    if not isbn[:-1].isdigit():
        return False
    if isbn[-1] != "X" and not isbn[-1].isdigit():
        return False
    
    digits = [int(isbn[i]) if isbn[i] != "X" else 10 for i in range(10)]
    return sum((i + 1) * digits[i] for i in range(10)) % 11 == 0