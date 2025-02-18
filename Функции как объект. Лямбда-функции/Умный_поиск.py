def smart_search(*args, func):
    if all(isinstance(arg, int) for arg in args):
        return tuple(filter(func, args))
    elif all(isinstance(arg, str) for arg in args):
        return tuple(word for word in args if word and word[0].isupper())
    return ()
