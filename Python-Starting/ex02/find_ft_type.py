def all_thing_is_obj(obj: any):
    if type(obj) is list:
        print(f"List : {type(obj)}")
    elif type(obj) is tuple:
        print(f"Tuple : {type(obj)}")
    elif type(obj) is set:
        print(f"Set : {type(obj)}")
    elif type(obj) is dict:
        print(f"Dict : {type(obj)}")
    elif type(obj) is str:
        print(f"{obj} is in the kitchen : {type(obj)}")
    else:
        print("Type not found")
    return 42