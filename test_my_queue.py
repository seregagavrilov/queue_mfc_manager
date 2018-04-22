from tasks import foo
from  manager import add_to_q
from redis import Redis

my_redis = Redis()

add_to_q(foo, my_redis, a=1, b=2, c=3)


