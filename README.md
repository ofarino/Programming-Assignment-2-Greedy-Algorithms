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
| File 1 | 8 | 50 | 48 | 47 | 29 |
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


<h3>Question 3: Prove OPTFF is Optimal</h3>
