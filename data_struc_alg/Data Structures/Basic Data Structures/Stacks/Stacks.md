Data structure that follows the FILO (First in, Last out) principal.Python has no true stack data structure. It uses lists instead. An example of how stacks work in C# is as follows:

```
// C# program to illustrate how to
// create a stack
using System;
using System.Collections;
 
class MainProgram {
 
    // Main Method
    static public void Main()
    {
 
        // Create a stack
        // Using Stack class
        Stack my_stack = new Stack();
 
        // Adding elements in the Stack
        // Using Push method
        my_stack.Push("Geeks");
        my_stack.Push("geeksforgeeks");
        my_stack.Push('G');
        my_stack.Push(null);
        my_stack.Push(1234);
        my_stack.Push(490.98);
 
        // Accessing the elements
        // of my_stack Stack
        // Using foreach loop
        foreach(var elem in my_stack)
        {
            Console.WriteLine(elem);
        }
    }
}
```