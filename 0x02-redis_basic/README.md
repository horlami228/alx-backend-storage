# Redis Basic

Redis is an in memory data storage system

```py
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

        return self.get(key, fn=lambda x:
```
