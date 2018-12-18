from redis import Redis

from examples.tasks_example import some_function, get_url
from queue_manager import QManager

redis = Redis()
manager = QManager(redis)
manager.add_to_queue(some_function, 'asd', 'bc', ['s', 'e', 'r', '1'], sourname='Name')
manager.add_to_queue(get_url, 'https://www.jetbrains.com/help/pycharm/code-folding.html')




