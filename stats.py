def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_on(item):
    return item["num"]

def get_sorted_char_list(count):
    list = []

    for char in count:
        list.append({
            "char": char,
            "num": count[char]
        })

    list.sort(reverse = True, key = sort_on)

    return list
