

def find_substing(s: str, pattern: str) -> list:
    """
    Find substring in string
    :param s: String
    :param pattern: Pattern
    :return: list of [start, finish] match indexes
    """
    match_storage = []
    for n, c in enumerate(s):
        if c == pattern[0]:
            if s[n:n+len(pattern)] == pattern:
                match_storage.append([n, n + len(pattern)])
    return match_storage