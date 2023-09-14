def ft_tqdm(lst: range):
    len_lst = len(lst)
    for elem in lst:
        el = elem + 1
        yield(elem)
        per = int((el * 100) / len_lst)
        LEN_PROGRESS_BAR = 153
        len_str = int(per * LEN_PROGRESS_BAR / 100)
        str = '█' * len_str + ' ' * (LEN_PROGRESS_BAR - len_str)
        print(f"{per}%|{str}| {el}/{len_lst}", end='\r')
    return None