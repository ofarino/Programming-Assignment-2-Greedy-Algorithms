# Programming-Assignment-2-Greedy-Algorithms
Olivia Farino: 91264400

Boglarka Csanadi: 51900580

**How to Run**

From the project root run:

python3 src/main.py
or
python src/main.py


**Output**

Output is displayed in tests/example.out


**To Test Other Files**

in src/main.py adjust file name on the first line of **if __name__ == '__main__':**


**Question 1: Empirical Comparison**
| Input File | k | m | FIFO | LRU | OPTFF |
| --- | --- | --- | --- | --- | --- |
| File 1 | 8 | 50 | 48 | 47 | 29 |
| File 2 | 10 | 75 | 67 | 66 | 39 |
| File 3 | 6 | 60 | 60 | 60 | 48 | 

Does OPTFF have the fewest misses?

Yes, OPTFF has the fewest misses for all of our input files.

How does FIFO compare to LRU?

FIFO typically has slightly more misses than LRU, but the difference depends on the input sequence.

**Question 2: Bad Sequence for LRU or FIFO**

**Question 3: Prove OPTFF is Optimal**
