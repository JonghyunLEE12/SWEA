from itertools import combinations


def solution(relations: list) -> int:
    valid_keys: list = list()
    degree: int = len(relations[0])

    def is_minimal(key: tuple) -> bool:
        for valid_key in valid_keys:
            if all(column in key for column in valid_key):  # key.contains_all(valid_key)
                return False
        return True

    def is_unique(key: tuple) -> bool:
        distinct: set = set(tuple(row[idx] for idx in key) for row in relations)
        return len(distinct) == len(relations)

    def apply_filter(iterable) -> filter:
        return filter(lambda key: is_minimal(key) and is_unique(key), iterable)

    for deg in range(degree):
        combination = combinations(range(degree), deg + 1)
        for key in apply_filter(combination):
            valid_keys.append(key)

    return len(valid_keys)