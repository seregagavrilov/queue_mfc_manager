def foo(a,b,c):
    print(a+b+c)
    return a+b+c


def bar(a, b, *args, **kvargs):
    return print(a * b)


def say_name(name, sourname):
    return print(name+' '+sourname)
