def count_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    return char_counts

def sort_on(dict_item):
    return dict_item["count"]

def create_character_list_of_dicts(char_count_dict):

    new_list = []

    for char, count in char_count_dict.items():
        new_list.append({
            'character': char,
            'count': count
        })
    new_list.sort(reverse=True, key=sort_on)

    return new_list

