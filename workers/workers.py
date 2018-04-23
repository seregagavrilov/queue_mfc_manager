import click
from json_tricks import loads
from inspect import signature

from test_my_queue import manager, my_redis


@click.command()
def start_workers():
    for name, function in manager.jobs_for_workers.items():
        json_from_redis = loads(manager.take_from_qvstorage(name, my_redis).decode())
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