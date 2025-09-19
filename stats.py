def word_counter(text):
    split_text = text.split()
    return len(split_text)

def character_dict(text):
    chars = {}
    for char in list(text.lower()):
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    
    return chars