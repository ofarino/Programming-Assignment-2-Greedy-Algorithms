# Among items currently in the cache, evict the one whose next request occurs farthest in the future (or never occurs again)
def optff_cache(cache_size, requests):
    cache = []
    cache_misses = 0

    for i, request in enumerate(requests):
        if request not in cache:
            cache_misses += 1
            if len(cache) < cache_size:
                cache.append(request)
            else:
                # Find the item in the cache that is requested farthest in the future
                farthest_index = -1
                farthest_request = None
                for item in cache:
                    try:
                        index = requests.index(item, i + 1)
                    except ValueError:
                        # Item is not requested again
                        index = float('inf')
                    if index > farthest_index:
                        farthest_index = index
                        farthest_request = item
                # Evict the item that is requested farthest in the future        
                cache.remove(farthest_request)
                cache.append(request)

    return cache_misses