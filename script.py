def to_weird_case(string):
    words = string.split()
    result = []

    for word in words:
        weird_word = ""
        for i, char in enumerate(word):
            if i % 2 == 0:
                weird_word += char.upper()
            else:
                weird_word += char.lower()
        result.append(weird_word)

    return " ".join(result)
