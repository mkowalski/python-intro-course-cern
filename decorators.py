from functools import wraps


def my_wraps(original_fn):
    def decorator(proxy):
        proxy.__name__ = original_fn.__name__
        proxy.__doc__ = original_fn.__doc__
        proxy.__module__ = original_fn.__module__

        return proxy
    return decorator


def inc_result_by(N):
    def decorator(fn):
        @wraps(fn)
        def proxy(*args, **kwargs):
            return fn(*args, **kwargs) + N
        return proxy
    return decorator


def report_args(fun):
    @wraps(fun)
    def proxy(*args, **kwargs):
        print args, kwargs
        return fun(*args, **kwargs)

    # proxy.__name__ = fun.__name__
    # proxy.__doc__ = fun.__doc__
    # proxy.__module__ = fun.__module__

    return proxy


def report_result(fun):
    @my_wraps(fun)
    def proxy(*args, **kwargs):
        r = fun(*args, **kwargs)
        print r
        return r
    return proxy


@inc_result_by(10)
@report_result
@report_args
def badd(a, b):
    """
    This is a wrong function
    :param a:
    :param b:
    :return:
    """
    return a * b
# badd = report_args(badd)


print badd(2, 3)
