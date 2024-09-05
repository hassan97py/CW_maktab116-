class Cache:
    def __init__(self):
        self.cache = {}
        print("Cache created.")

    def __del__(self):
        print("Cache cleared.")
        del self.cache

# Test the lifecycle of the Cache object
def test_cache():
    print("Test started.")
    cache = Cache()
    print("Cache object created.")
    # You can use the cache here
    print("Cache is being used.")
    del cache
    print("Cache object deleted.")
    print("Test completed.")

test_cache()
