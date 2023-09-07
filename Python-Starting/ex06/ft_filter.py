def ft_filter(func, iterable):
    """
ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    if (func == None):
        return (item for item in iterable)
    return (item for item in iterable if func(item))
    # for item in iterable:
    #     if func(item):
    #         yield item

def main():
    def is_even(x):
        return x % 2 == 0
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_numbers = filter(None, "test")
    test = ft_filter(None, "test")
    print(list(even_numbers), " | ", even_numbers)
    print(list(test), " | ", test)
    print("-----------------------------------------------")
    print(filter.__doc__)
    print("-----------------------------------------------")
    print(ft_filter.__doc__)
    
if __name__ == "__main__":
    main()