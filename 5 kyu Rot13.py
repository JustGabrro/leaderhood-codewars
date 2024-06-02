def rot13(message):
    result = ""
    for x in message:
        if x.isalpha():
            rot = 13
        elif x.islower():
            rot = -13
        else:
            result += x
        return result
    
# ვერ დავასრულე