Merge sort is a type of sorting algorithm that follows the divide-and-conquer paradigm. This algorithm works by dividing an unsorted list into n partitions, each containing one element (a list of one element is considered sorted), then repeatedly merging partitions to produce new sorted lists until there is only 1 sorted list remaining. This resulting list is the fully sorted list. The process of dividing the list is done recursively until it hits the base case of a list with one item. Merge sort has a time complexity of O(n log n) for all cases (best, average and worst), which makes it highly efficient for large data sets.

Notation: O(n log n)

- Divide and Conquer algorithm
    - Typically a recursive algorithm
    - Breaks down problem into multiple sub-problems until they become simple to solve
    - Solutions are combined to solve the original problem