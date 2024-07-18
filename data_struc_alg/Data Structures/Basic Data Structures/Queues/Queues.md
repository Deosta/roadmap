Data structure that follows the FIFO (First in, First out) principal. Python has no true queue data structure. It uses lists instead. An example of how queues work in C# is as follows:

```
// C# code to create a Queue 
using System; 
using System.Collections; 
  
class MainProgram { 
  
    // Driver code 
    public static void Main() 
    { 
  
        // Creating a Queue  
        Queue myQueue = new Queue(); 
  
        // Inserting the elements into the Queue 
        myQueue.Enqueue("one"); 
  
        // Displaying the count of elements 
        // contained in the Queue 
        Console.Write("Total number of elements in the Queue are : "); 
  
        Console.WriteLine(myQueue.Count); 
  
        myQueue.Enqueue("two"); 
  
        // Displaying the count of elements 
        // contained in the Queue 
        Console.Write("Total number of elements in the Queue are : "); 
  
        Console.WriteLine(myQueue.Count); 
  
        myQueue.Enqueue("three"); 
  
        // Displaying the count of elements 
        // contained in the Queue 
        Console.Write("Total number of elements in the Queue are : "); 
  
        Console.WriteLine(myQueue.Count); 
  
        myQueue.Enqueue("four"); 
  
        // Displaying the count of elements 
        // contained in the Queue 
        Console.Write("Total number of elements in the Queue are : "); 
  
        Console.WriteLine(myQueue.Count); 
  
        myQueue.Enqueue("five"); 
  
        // Displaying the count of elements 
        // contained in the Queue 
        Console.Write("Total number of elements in the Queue are : "); 
  
        Console.WriteLine(myQueue.Count); 
  
        myQueue.Enqueue("six"); 
  
        // Displaying the count of elements 
        // contained in the Queue 
        Console.Write("Total number of elements in the Queue are : "); 
  
        Console.WriteLine(myQueue.Count); 
    } 
} 
```

Output:
```
Total number of elements in the Queue are : 1
Total number of elements in the Queue are : 2
Total number of elements in the Queue are : 3
Total number of elements in the Queue are : 4
Total number of elements in the Queue are : 5
Total number of elements in the Queue are : 6
```