def NULL_not_found(object: any):
    if (not object) or (isinstance(object, float) and object != float('nan')):
        str = ''
        if object == None:
            str = "Nothing"
        elif isinstance(object, bool) and object == False:
            str = "Fake"
        elif object == 0:
            str = "Zero"
        elif object == '':
            str = "Empty"
        elif object != float('nan'):
            str = "Cheese"
        print (f"{str}: {object} {type(object)}")
        return 0
    else:
        print ("Type not Found")
        return 1