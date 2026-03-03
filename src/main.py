import lru
import fifo
import optff

#read the input file
def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # read in the cache size and the number of requests
        cache_size = int(lines[0].strip().split()[0])
        num_requests = int(lines[0].strip().split()[1])
        # read in the requests
        requests = [int(x) for x in lines[1].strip().split()]
    return cache_size, num_requests, requests

if __name__ == "__main__":
    cache_size, num_requests, requests = read_input_file("./data/file3.in")
    lru_cache_misses = lru.lru_cache(cache_size, requests)
    fifo_cache_misses = fifo.fifo_cache(cache_size, requests)
    optff_cache_misses = optff.optff_cache(cache_size, requests)
    # output the number of cache misses to example.out
    with open("./tests/example.out", 'w') as file:
        file.write('FIFO : ' + str(fifo_cache_misses) + '\n')
        file.write('LRU : ' + str(lru_cache_misses) + '\n')
        file.write('OPTFF : ' + str(optff_cache_misses) + '\n')