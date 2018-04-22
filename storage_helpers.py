def add_to_qvstorage(function_name,  json, kvstor):
    kvstor.rpush(function_name, json)


def take_from_qvstorage(function_name,  json, kvstor):
    kvstor.lpop(function_name, json, kvstor)