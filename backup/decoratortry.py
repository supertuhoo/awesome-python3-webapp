def log(func):
    def wrap(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrap


@log
def now():
    print("this is now.")


now()
