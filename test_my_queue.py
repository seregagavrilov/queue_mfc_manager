from tasks import foo, bar, my_func
from manager import QManager
from redis import Redis


my_redis = Redis()
manager = QManager(my_redis)
manager.add_to_queue(foo, ['a', 1, 'b', 2, 'c', 3])
manager.add_to_queue(bar, ['a', 1, 'b', 2], name='Katya')
manager.add_to_queue(my_func, ['name', 'Sergey', 'sourname', 'Gavrilov'])


