def boyer_moor_search(text, pattern, dictionary_displace):
    i = len(pattern)-1
    while i < len(text):
        for j in range(len(pattern)-1, -1, -1):
            if text[i-(len(pattern)-1-j)] == pattern[j]:
                if j == 0:
                    return True
                continue
            else:
                try:
                    i += dictionary_displace[text[i-(len(pattern)-1-j)]]
                except KeyError:
                    i += dictionary_displace["else"]
                break
    return False


def generate_shift_table(pattern):
    shift_char = dict()
    set_of_letters = set()
    place_of_last_char = len(pattern)-1

    for i in range(place_of_last_char-1, -1, -1):
        if pattern[i] not in set_of_letters:
            shift_char[pattern[i]] = place_of_last_char-i
            set_of_letters.add(pattern[i])

    if pattern[place_of_last_char] not in set_of_letters:
        shift_char[pattern[place_of_last_char]] = len(pattern)

    shift_char["else"] = len(pattern)
    print(shift_char)
    return shift_char


def main(text, search_pattern):
    dict_displacement = generate_shift_table(search_pattern)
    answer = boyer_moor_search(text, search_pattern, dict_displacement)
    if answer:
        print(f"Search pattern is : {search_pattern}")
    else:
        print("Not found")


