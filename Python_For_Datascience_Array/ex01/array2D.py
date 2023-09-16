def slice_me(family: list, start: int, end: int):
    if not isinstance(family, list):
        return print("FIRST ARG IS NOT A LIST!")
    elif not isinstance(start, int):
        return print("START IS NOT AN INTEGER!")
    elif not isinstance(end, int):
        return print("END IS NOT AN INTEGER!")
    for item in family:
        if not isinstance(item, list):
            return print("LIST NOT VALID!")
