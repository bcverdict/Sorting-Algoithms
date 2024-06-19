# Sorting Algorithms

## Project Overview

This repository contains implementations of two classic sorting algorithms in Python: Binary Heap operations and Merge Sort. These algorithms are essential for understanding fundamental data structures and sorting techniques in computer science.

## Technologies Used

- **Programming Language:**
  - Python

## Files

### `bin_heap.py`

This file contains functions for working with a binary heap. The binary heap is a complete binary tree where each node is smaller than its children (min-heap) or larger than its children (max-heap). The following operations are implemented:

- **`order(arr)`:** Orders an array to satisfy the heap property.
- **`swap(arr, n, lastLeafInd)`:** Recursively swaps elements to maintain the heap property.
- **`insert_swap(arr, n, lastLeafInd)`:** Recursively swaps elements during insertion to maintain the heap property.
- **`insert(arr, num)`:** Inserts a new element into the heap and reorders the heap to maintain its properties.

#### Example Usage
```python
insert_arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15]
order(insert_arr)
insert(insert_arr, 17)
order(insert_arr)
```

### `merge_sort.py`

This file contains the implementation of the Merge Sort algorithm. Merge Sort is a divide-and-conquer algorithm that splits the array into halves, recursively sorts each half, and then merges the sorted halves back together.

- **`merge_sort(arr)`:** Recursively splits and merges the array to sort it.

#### Example Usage
```python
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)
```

## Features

- **Binary Heap Operations:**
  - Ordering of elements to maintain heap properties.
  - Insertion of new elements while maintaining heap properties.
  
- **Merge Sort:**
  - Efficient sorting of arrays using a divide-and-conquer approach.
