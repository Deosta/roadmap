Heap Sort is an efficient, comparison-based sorting algorithm. It utilizes a datastructure known as a ‘binary heap’, and works by dividing its input into a sorted and an unsorted region, and iteratively shrinking the unsorted region by extracting the largest element and moving that to the sorted region. It’s an in-place algorithm but not a stable sort. It involves building a Max-Heap, which is a specialized tree-based data structure, and then swapping the root node (maximum element) with the last node, reducing the size of heap by one and heapifying the root node. The maximum element is now at the end of the list and this step is repeated until all nodes are sorted. Heap Sort offers a good worst-case runtime of O(n log n), irrespective of the input data.

Can be used to sort ascending or descending depending on the use of minheap or maxheap

Notation: O(n log n)

