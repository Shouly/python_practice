def hello(fn):
    def wrapper():
        print('hello fn name', fn.__name__)
        fn()
        print('goodbye', fn.__name__)

    return wrapper


# @hello
# def test():
#     print("test")


# test()
def test():
    print('test')


print(hello(test))

test = hello(test)

test()


def fuck(fn):
    print('fuck %s !' % fn.__name__[::-1].upper())


@fuck
def wfg():
    pass


print(wfg())

