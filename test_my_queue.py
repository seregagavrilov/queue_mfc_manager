from tasks import foo, bar, say_name
from manager import QManager
from redis import Redis


my_redis = Redis()
manager = QManager(my_redis)
manager.add_to_queue(foo, ['a', 1, 'b', 2, 'c', 3])
manager.add_to_queue(bar, ['a', 1, 'b', 2], name='Name')
manager.add_to_queue(say_name, ['name', 'Sergey', 'sourname', 'Gavrilov'])



