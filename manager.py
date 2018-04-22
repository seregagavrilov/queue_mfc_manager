import inspect
from json_tricks import dumps, loads
from storage_helpers import add_to_qvstorage
from redis import Redis


class InstanceForJSON():
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def serialize_to_json(instance_to_json):
    json = dumps(instance_to_json, indent=4)
    return json


def add_to_q(func, kvstorage, **kwargs):
    instance = InstanceForJSON(task=func.__name__, args = kwargs)
    json = serialize_to_json(instance)
    add_to_qvstorage(func.__name__, json, kvstorage)


