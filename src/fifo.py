# Evict the item that has been in the cache the longest
def fifo_cache(cache_size, requests):
    cache = []
    cache_misses = 0

    for request in requests:
        # if request is not in cache, it's a cache miss
        if request not in cache:
            cache_misses += 1
            # if the length of the cache is less than the cache size, add the request to the cache
            if len(cache) < cache_size:
                cache.append(request)
            # else, evict the oldest item
            else:
                cache.pop(0)
                cache.append(request)

    return cache_misses