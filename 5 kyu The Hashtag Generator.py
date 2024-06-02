def generate_hashtag(s):
    if s == "":
        return False
    else:
        word = ""
        split_s = s.split()
        for i in split_s:
            a = i.capitalize()
            word += a
        if len(word) >= 140:
            return False
        else:
            return f"#{word}"