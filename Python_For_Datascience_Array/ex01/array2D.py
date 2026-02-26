def slice_me(family: list, start: int, end: int):
    """Slice a 2D list and print the old and new shapes.

    Takes a 2D list and returns the sliced portion from start to end.
    Prints the original and new shapes of the array.
    """
    if not isinstance(family, list):
        return print("FIRST ARG IS NOT A LIST!")
    elif not isinstance(start, int):
        return print("START IS NOT AN INTEGER!")
    elif not isinstance(end, int):
        return print("END IS NOT AN INTEGER!")
    len_list = len(family)
    if (start < 0 and len_list + start < 0) or (start > len_list - 1):
        return print("INVALID START INTEGER!")
    if (end < 0 and len_list + end < 0) or (end > len_list - 1):
        return print("INVALID END INTEGER!")
    len_item = 0
    if family and family[0] and isinstance(family[0], list):
        len_item = len(family[0])
    for item in family:
        if not isinstance(item, list):
            return print("LIST NOT VALID!")
        if len_item != len(item):
            return print("LIST SIZE NOT VALID!")
    new_family = family[start:end]
    print(f"My shape is : ({len_list}, {len_item})")
    print(f"My new shape is : ({len(new_family)}, {len_item})")
    return (new_family)


# family = [[1.80, 78.4],
# [2.15, 102.7],
# [2.10, 98.5],
# [1.88, 75.2]]
# print(slice_me(family, 0, 2))
# print(slice_me(family, 1, -2))
