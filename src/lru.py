# Least Recently Used (LRU) Cache implementation 
def lru_cache(cache_size, requests):
    cache = {}
    cache_misses = 0
    for request in requests:
        if request in cache:
            # update the last used time
            cache[request] = 0
        else:
            cache_misses += 1
            if len(cache) < cache_size:
                cache[request] = 0
            else:
                # find the least recently used item and remove it
                lru_item = min(cache, key=cache.get)
                del cache[lru_item]
                cache[request] = 0
        # update the last used time for all items in the cache
        for key in cache:
            if key != request:
                cache[key] += 1
    # return the number of cache misses
    return cache_misses
