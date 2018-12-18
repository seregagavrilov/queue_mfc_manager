import os
import requests

def foo(sec):
    print('a')

def bar(a,b):
    return print(a * b)


def say_name(name, sourname):
    print(name+' '+sourname)


def some_function(a, b, *args, my_dog='flufi', my_cat='kity', **kvargs):
    # time.sleep(1)
    print(os.getpid())
    print(kvargs, a, b, args, my_cat, my_dog)


def get_url(url):
    u = requests.get(url)
    print(u.status_code)
