"""
Get root property name

Given an object of likely nested objects, where the final element is an array containing positive integers, write a function that returns the name of the root property that a particular integer lives in.

E.g
Heres what the object looks like:
object = {
    "one": {
        "nest1": {
            "val1": [9, 34, 92, 100]
         }
    },
    "2f7": {
        "n1": [10, 92, 53, 71],
        "n2": [82, 34, 6, 19]
    }
}

getRootProperty(object, 9); //=> "one"
"""
def get_root_property(dict_, value):
    for key in dict_:
        if (isinstance(dict_[key], list)):
            if(value  in dict_[key]):
                return key
            return None
        else:
            if(get_root_property(dict_[key],value)):
                return key
            return get_root_property(dict_[key],value)

test = {
    "one": {
        "nest1": {
            "val1": [9, 34, 92, 100]
         }
    },
    "2f7": {
        "n1": [10, 92, 53, 71],
        "n2": [82, 34, 6, 19]
    }
}
find = get_root_property(test, 10)
print(find)