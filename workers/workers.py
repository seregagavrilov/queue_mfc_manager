import click
from json_tricks import loads
from inspect import signature
import threading
condition = threading.Condition()

from test_my_queue import manager, my_redis
keys_from_redis = [key.decode() for key in my_redis.keys()]


@click.command()
def start_workers(count_workers=1):
    for i in range(count_workers):
        thread = threading.Thread(target=process_tasks, args=(condition,))
        thread.start()

def take_task_from_manager():
    try:
        condition.acquire()
        task = keys_from_redis.pop()
        condition.notifyAll()
        condition.release()
        return task
    except IndexError:
        condition.release()
        return None


def process_tasks(cond):
    while True:
        task_name = take_task_from_manager()
        if task_name is None:
            break
        function = manager.tasks_for_workers[task_name]
        json_from_redis = loads(manager.take_from_qvstorage(task_name, my_redis).decode())
        launch_function_with_arguments(function, json_from_redis)


def launch_function_with_arguments(function, arguments):
    dict_position_args = argument_list_to_dict(arguments.positional_args)
    dict_keyword_args = dict(arguments.named_arguments)
    sign_obj = signature(function)
    bind = sign_obj.bind_partial()
    bind.arguments =dict_position_args
    function(*bind.args, **dict_keyword_args)


def argument_list_to_dict(list_args):
    i = iter(list_args)
    return dict(zip(i, i))



if __name__  == '__main__':
    start_workers()