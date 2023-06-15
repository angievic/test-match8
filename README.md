## Task
​
The task is to write a function that finds pairs of integers from a list that
sum to a given value. The function will take as input the list of numbers as
well as the target sum.
​
Sample output is shown below.
```
> app 1,9,5,0,20,-4,12,16,7 12
​
+ 12,0
+ 5,7
+ 16,-4
​
```
​
In the example, there is an executable named `app`. It takes as command line
arguments a comma separated list of integers, and the target integer. Your app
doesn't need to have identical input/output mechanisms. For example, you could
read from a file instead of the command line.
​
You can assume that all input values are integers. You can assume that there aren't
any repeat values in the list.
​
The algorithm to find the pairs must be faster than O(n^2). All edge cases
should be handled appropriately. This is _not_ a closed book test. You are
encouraged to reach out with any questions that you come across.
​
## Run Solution
```python
python pairsnumbers.py ./numbers2.txt 8
```
expected_output:
+ -2 , 10
+ 5 , 3
+ 8 , 0
```python
python pairsnumbers.py ./numbers.txt 12
```
expected_output:
+ 12 , 0
+ 16 , -4
+ 7 , 5

You can create your own txt file and run:
```python
python pairsnumbers.py <txt path> <target sum>
```

## Solution is O(n)

I use the way that each number only appear one time to obtain complement and save this value in a dict to compare and return result.
