Quicksort, also known as partition-exchange sort, is an efficient, in-place sorting algorithm, which uses divide and conquer principles. It operates by selecting a ‘pivot’ element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted. This process continues until the base case is achieved, which is when the array or sub-array has zero or one element, hence is already sorted. Quicksort can have worst-case performance of O(n^2) if the pivot is the smallest or the largest element in the array, although this scenario is rare if the pivot is chosen randomly. The average case time complexity is O(n log n).

Notation: O(n²) if largest or smallest element chosen; O(n log n) is the average and best case

- Divide and Conquer algorithm
    - Recursive
    - Break down problem into multiple sub-problems and combines the smaller ones into the desired solution

- General Principle
    - Choose pivot element (Usually last or random)
    - Store elements less than pivot in left sub-array, grater than pivot goes into the right sub-array
    - Call quicksort recursively on left and right sub-array until only 1 element remains