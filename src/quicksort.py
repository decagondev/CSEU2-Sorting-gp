# Why are recursive sorting algorithms useful?



# Divide a problem in to subproblems (of the same type)
# Solve the subproblems
# Combine the results of the subproblems 
# to get the solution to the original problem

# Quicksort

# Divide and conquer sorting algorithm

    # start with a pivot point
     # (first or last element)
     # (middle, mean, median, or even a 
     # random element can get better performance)
    # move all elements smaller than the pivot point to the left hand side of the pivot. 
     # move all larger elements to the right of the pivot
    # (recursive case) recursively Quick Sort LHS and RHS until (base case) a side only contains a single element


# partition data
def partition(data):
    left = []
    pivot = data[0]
    right = []

    for v in data[1:]:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)
    
    return left, pivot, right

def quick_sort(data):
    # base case
    if data == []:
        return data
    
    left, pivot, right = partition(data)

    return quick_sort(left) + [pivot] + quick_sort(right)


# l = [20, 30, 10, 5, 70, 100, 8, 1, 12, 4, 6, 2]

# sl = quick_sort(l)

# print(l)
# print("------")
# print(sl)

from time import time
import random
l = [random.randint(0, 1000) for i in range(0, 100)]

input_sizes = [i * 100 for i in range(1, 50)]

times = []

for input_size in input_sizes:
    l = [random.randint(0, 1000) for i in range(0, input_size)]
    # Store start time
    start_time = time()
    # Run some code
    quick_sort(l)
    # Store end time
    end_time = time()
    # print out end time - start time
    times.append(end_time - start_time)

print("LENGTHS")
for elem in input_sizes:
    print(elem)

print("TIMES")
for t in times:
    print(t)