def fifo_cache(cache_size, requests):
    cache = []
    cache_misses = 0

    for request in requests:
        if request not in cache:
            cache_misses += 1
            if len(cache) < cache_size:
                cache.append(request)
            else:
                cache.pop(0)  # Evict the oldest item
                cache.append(request)

    return cache_misses