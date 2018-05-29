from functools import wraps


def feature(f):

    @wraps(f)
    def wrapper(*args, **kwargs):
        if args[1].get(f.__name__) is None:
            return f(*args, **kwargs)

    return wrapper
