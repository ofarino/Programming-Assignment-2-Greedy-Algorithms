# Programming-Assignment-2-Greedy-Algorithms
Olivia Farino: 91264400

Boglarka Csanadi: 51900580

<h2>How to Run</h2>

From the project root run:

python3 src/main.py
or
python src/main.py


<h2>Output</h2>

Output is displayed in tests/example.out


<h2>To Test Other Files</h2>

in src/main.py adjust file name on the first line after **if __name__ == '__main__':**

• Current input is ./data/example.in


• All input files used located in data folder

<h2>Written Component</h2>

<h3>Question 1: Empirical Comparison</h3>

| Input File | k | m | FIFO | LRU | OPTFF |
| --- | --- | --- | --- | --- | --- |
| File 1 | 8 | 50 | 45 | 42 | 25 |
| File 2 | 10 | 75 | 67 | 66 | 39 |
| File 3 | 6 | 60 | 60 | 60 | 48 | 

**Does OPTFF have the fewest misses?**

Yes, OPTFF has the fewest misses for all of our input files.

**How does FIFO compare to LRU?**

FIFO typically has slightly more misses than LRU, but the difference depends on the input sequence.


<h3>Question 2: Bad Sequence for LRU or FIFO</h3>


There does exist a request sequence for which OPTFF incurs strictly fewer misses than LRU (or FIFO), below is an example of such as sequence:


k = 3; m = 6


1 2 3 4 1 2


FIFO: 6 misses


LRU: 6 misses


OPTFF: 4 misses

<h4>Reasoning:</h4>

Both FIFO and LRU do not account for future requests in the sequence. When the cache is full FIFO evicts items based on their insertion order and LRU evicts based on recent usage. OPTFF knows the future sequence and is able to evict an item whose next use is the farthest in the future, or not part of the sequence, which minimizes cache misses.


In this sequence, when the 4th request occurs (4), it doesn't exist in the cache. Both LRU and FIFO evict the 1st item in the cache (1) because the first three items are distinct, so 1 is the least recently used and the first in. However, the 5th request is also 1. Because OPTFF knows the future sequence, it sees that both 1 and 2 are accessed again, so it evicts 3 instead, resulting in 2 less misses than both FIFO and LRU.


<h3>Question 3: Prove OPTFF is Optimal</h3>

<h4>Initial state:</h4>


Let OPTFF be Belady’s Farthest-in-Future algorithm.
Let A be any offline algorithm that knows the full request sequence.
Prove that the number of misses of OPTFF is no larger than that of A on any fixed sequence.


<h4>Proof:</h4>


• Suppose for contradiction that A has less misses then OPTFF for some sequence S.


• There is a time when A and OPTFF have a different eviction.


• Lets say OPTFF evicts x and A evicts some value y that doesnt equal x.


• Therefore we know either x is further in the future than y or x is never requested again because OPTFF always evicts the furthest value in the future.


• This means there are two cases for y:


      - y is requested before x, then A will miss before OPTFF.

   
      - y and x are never requested again.

    
In either case A cannot have less misses then OPTFF.


Therefore the number of misses of OPTFF is no larger than that of A on any fixed sequence.

