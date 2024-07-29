Binary Search is a type of search algorithm that follows the divide and conquer strategy. It works on a sorted array by repeatedly dividing the search interval in half. Initially, the search space is the entire array and the target is compared with the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target, and repeating this until the target is found. If the search ends with the remaining half being empty, the target is not in the array. Binary Search is log(n) as it cuts down the search space by half each step.

**Binary Search is much faster than Linear Search, but requires a sorted array to work.**

Notation: O(log n)

-General operation:
    
    - Check the value in the center of the array.
    - If the target value is lower, search the left half of the array. If the target value is higher, search the right half.
    - Continue step 1 and 2 for the new reduced part of the array until the target value is found or until the search area is empty.
    - If the value is found, return the target value index. If the target value is not found, return -1.
