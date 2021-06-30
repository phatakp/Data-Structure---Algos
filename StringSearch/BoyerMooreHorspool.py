def search(text, find, replace=None):
    occurences = 0
    compares = 0
    if not find or not text:
        return 'Invalid Input'

    if len(find) > len(text):
        return 'Not found'

    # Build the Bad Match Dictionary
    search_len = len(find)-1
    bad_match_table = {}
    for i, char in enumerate(find[:-1]):
        bad_match_table[char] = search_len-i

    offset = 0
    while offset <= len(text)-len(find):

        chars_left_to_match = len(find) - 1

        while (chars_left_to_match >= 0 and find[chars_left_to_match] == text[offset+chars_left_to_match]):
            compares += 1
            chars_left_to_match -= 1

        if chars_left_to_match < 0:
            occurences += 1
            if replace:
                if len(replace) > len(find):
                    text = text[:offset] + replace + text[offset+len(find):]
                elif len(find) > len(replace):
                    diff = len(find) - len(replace)
                    text = text[:offset] + replace + \
                        text[offset+len(replace)+diff:]
                else:
                    text = text[:offset] + replace + text[offset+len(replace):]

            offset += len(find)
        else:
            offset += bad_match_table.get(text[offset +
                                               len(find)-1], len(find))

    if replace:
        return text

    return f'Pattern found {occurences} times with {compares} comparisons'


if __name__ == '__main__':
    find = 'T'
    replace = 't'
    text = 'THE TRUTH IS OUT THERE IN THIS TRUTHFUL AREA'
    print(search(text, find))
