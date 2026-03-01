# Least Recently Used (LRU) Cache implementation 
def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # read in the cache size and the number of requests
        cache_size = int(lines[0].strip().split()[0])
        num_requests = int(lines[0].strip().split()[1])
        # read in the requests
        requests = [int(x) for x in lines[1].strip().split()]
    return cache_size, num_requests, requests

# LRU Cache
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
