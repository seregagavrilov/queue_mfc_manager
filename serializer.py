import inspect
from json_tricks import dumps, loads
from redis import Redis

def serialize_task(task, args, kwargs):
    signatrure = inspect.signature(task)
    return '{function_name: name, parameters: paramiters}'


def add_to_queue():
    pass


def grab_task(my_task, *args, **kwargs):
    json_task = serialize_task(my_task, args, kwargs)
    add_to_queue(json_task)


class Serilizator():
        def __init__(self, **kwargs):
                for k, v in kwargs.items():
                        setattr(self, k, v)

cls_instance = Serilizator(name=add_to_queue.__name__, args={'a': 7, 'b':10, 'c':20})
json_of_function = dumps(cls_instance, indent=4)

redis = Redis()

redis.rpush(add_to_queue.__name__, json_of_function)

cls_instance = redis.lpop(add_to_queue.__name__)

desiral = loads(cls_instance.decode())

print(desiral)




