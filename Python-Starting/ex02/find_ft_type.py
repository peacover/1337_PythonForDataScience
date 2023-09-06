def all_thing_is_obj(obj: any):
    if isinstance(obj, object):
        if type(obj).__name__ == "str":
            print(f"{obj} is in the kitchen : {type(obj)}")
        elif type(obj).__name__ == "int":
            print("Type not found")
        else: 
            print(f"{type(obj).__name__.capitalize()} : {type(obj)}")
    else:
        print("Type not found")
    return 42