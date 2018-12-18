import requests

def some_function(a, b, *args, my_dog='flufi', my_cat='kity', **kvargs):
    print(kvargs, a, b, args, my_cat, my_dog)


def get_url(url):
    u = requests.get(url)
    print(u.status_code)
