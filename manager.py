from tasks_example import foo, bar, say_name, some_function, get_url
from queue_manager import QManager
from redis import Redis


redis = Redis()
manager = QManager(redis)
# manager.add_to_queue(foo,  1,  2, 3)
manager.add_to_queue(some_function, 'asd', 'bc', ['s', 'e', 'r', '1'], sourname='Name')
manager.add_to_queue(some_function, 'asd', 'bc', ['s', 'e', 'r', '2'], sourname='Name')
manager.add_to_queue(some_function, 'asd', 'bc', ['s', 'e', 'r', '3'], sourname='Name')
manager.add_to_queue(some_function, 'asd', 'bc', ['s', 'e', 'r', '4'], sourname='Name')
manager.add_to_queue(some_function, 'asd', 'bc', ['s', 'e', 'r', '5'], sourname='Name')
manager.add_to_queue(some_function, 'asd', 'bc', ['s', 'e', 'r', '6'], sourname='Name')
manager.add_to_queue(some_function, 'asd', 'bc', ['s', 'e', 'r', '7'], sourname='Name')
manager.add_to_queue(some_function, 'asd', 'bc', ['s', 'e', 'r', '8'], sourname='Name')
manager.add_to_queue(say_name, 'Sergey', 'Gavrilov')
manager.add_to_queue(get_url, 'https://www.jetbrains.com/help/pycharm/code-folding.html')

# some_function()



