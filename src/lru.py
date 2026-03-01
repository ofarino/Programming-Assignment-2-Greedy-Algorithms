from collections import OrderedDict
# Least Recently Used (LRU) Cache implementation 
def lru_cache(cache_size, requests):
    cache = OrderedDict()  # use an ordered dictionary to maintain the order of items in the cache
    cache_misses = 0
    for request in requests:
        if request in cache:
            # if the request is already in the cache, move it to the end to show that it was recently used
            cache.move_to_end(request)
        else:
            # if the request is not in the cache, it's a cache miss
            cache_misses += 1
            # if the cache is full, remove the least recently used item (the first item in the ordered dictionary)
            if len(cache) >= cache_size:
                cache.popitem(last=False)
            # add the new request to the cache
            cache[request] = True
    return cache_misses
