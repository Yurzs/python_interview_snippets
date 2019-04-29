

def find_substing(s: str, pattern: str) -> list:
    """
    Find substring in string
    :param s: String
    :param pattern: Pattern to match
    :return: list of match [start, end]
    """
    match_storage = []
    match_counter = 0
    pattern_index = 0
    for n, c in enumerate(s):
        if pattern_index > 0 and c == pattern[0]:
            match_counter = 1
            pattern_index = 1
        else:
            pattern_index +=1
            match_counter +=1
        if match_counter == len(pattern):
            match_storage.append([n-len(pattern), n])
    return match_storage