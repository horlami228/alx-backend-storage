#!/usr/bin/env python3

"""Writing strings to redis"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counts the number of times a Cache method was called"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function to
        initialize a count on the method

        """
        key = method.__qualname__
        # set a key with a count
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs
        on a particular function
    """
    @wraps(method)
    def wrapper_function(self, *args, **kwargs):
        """wrapper function to create list"""
        list_inputs = f"{method.__qualname__}:inputs"
        list_outputs = f"{method.__qualname__}:outputs"

        self._redis.rpush(list_inputs, str(args))
        key = method(self, *args, *kwargs)
        self._redis.rpush(list_outputs, key)
        return key
    return wrapper_function


def replay(method: Callable):
    """display the history of calls for
    a function"""
    cache = redis.Redis()
    method_name = method.__qualname__

    get_calls = cache.get(method_name).decode("utf-8")
    get_inputs = cache.lrange(f"{method_name}:inputs", 0, -1)
    get_outputs = cache.lrange(f"{method_name}:outputs", 0, -1)

    print(f"{method_name} was called {get_calls} times:")

    for i, o in zip(get_inputs, get_outputs):
        print(f"{method_name}(*{i.decode('utf-8')}) -> {o.decode('utf-8')}")


class Cache():
    """This reperesents a cache class"""

    def __init__(self):
        """Initialize a new cache class"""
        self._redis = redis.Redis()
        # self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method for storing data in cache"""
        random_key = str(uuid.uuid4())

        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Union[str, bytes, int, float]:
        """converting to original data type"""

        value = self._redis.get(key)

        if value is not None:
            if fn:
                return fn(value)
            else:
                return value
        return value

    def get_str(self, key: str) -> str:
        """retrieve a string value from cache"""

        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """return an int value from cache"""

        return self.get(key, fn=lambda x: int(x.decode("utf-8")))
