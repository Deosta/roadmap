In the context of algorithmic complexity, “time” refers to the amount of computational time that the algorithm takes to execute usually measured in ms, while “space” refers to the amount of memory that the algorithm needs to complete its operation. The time complexity of an algorithm quantifies the amount of time taken by an algorithm to run, as a function of the size of the input to the program. The space complexity of an algorithm quantifies the amount of space or memory taken by an algorithm to run, as a function of the size of the input to the program. It’s important to note that time and space are often at odds with each other; optimizing an algorithm to be quicker often requires taking up more memory, and decreasing memory usage can often make the algorithm slower. This is known as the space-time tradeoff.

https://www.bigocheatsheet.com/

Three notations used to represent algorithmic notation:
Big-O - Worst Case
Big-Omega - Best Case
Big-Theta - Average Case

Big-O is the most commonly seen notation as it represents the worst case for the algorithm, hence, the better Big-O is, better the algorithm is at it's worst.

Big-O follows an order of growth. In terms of time, from most efficient to least:

O(1)      : Constant
O(log n)  : Logarithmic
O(n)      : Linear
O(n log n): Linearithmic
O(n^2)    : Quadratic
O(n^3)    : Cubic
O(2^n)    : Exponential
O(n!)     : Factorial

------------------------------------------------------------------------------------
O(1): Constant

To calculate Big-O simply count the number of statements the code has to execute. 
Let's figure the Big-O notation of the following function:

def ask_info(arry):
    x = input('Enter your name:') #1
    print('Hello, ' + x)          #2

This function takes no arguments and executes two statements. The complexity for this function is O(2) it's also called constant complexity because no matter what, this function will always execute those two lines and does not depend on the number of inputs the user gives. Due to this, the complexity O(2) can be simplified to O(1).

Keep in mind, a constant is any step that doesn't scale with the input to the function.

------------------------------------------------------------------------------------
O(n): Linear

Let's look at an example that does depend on the number of inputs provided by the user:

def print_items(items: str):
    for item in items: #this line is linear O(n), based on the length of items
        a = 1 + 2      #this line is constant O(1)
        print(item)    #this line is constant O(1), it will always take x amount of time to print the item to the console.

This function is of complexity O(2) + O(n). Since Big-O is only concerned with the WORST case, in terms of time, we can simplify this notation. We drop the more efficient notations, in this case O(2). We are left with O(n), which is the notation for this function. No matter what, this function's time will scale linearly with the amount of inputs provided by `items`

------------------------------------------------------------------------------------
O(n^2): Quadratic

def square(n: int) -> None:
    for x in range(n):         #O(n)
        for y in range(n):     #O(n)
            do.something(x, y)

This function is of complexity O(1) + O(n^2) . We can drop the O(1) since we are only concerned with the worst case. This leaves us with O(n^2) for every iteration of the top loop, the nested loop needs to execute n number of times before the outer loop increments by one in range of n. It is easy to see why this is a Quadratic complexity.

------------------------------------------------------------------------------------
O(n^3): Cubic

def cube(n: int) ->  None:
    for x in range(n):               #O(n)
        for y in range(n):           #O(n)
            for z in range(n):       #O(n)
                do.something(x, y, z)#O(1)

This function is of complexity O(n) * O(n) * O(n) * O(1) = 0(n^3) * O(1) = O(n^3). Much like the previous example, nested for loops exponentially increase the time it takes for a function to execute completely. This is a Cubic complexity.

------------------------------------------------------------------------------------
O(log n): Logarithmic

Logarithm is the power that a number needs to be raised to to get another number. In CS, unless specified otherwise, we can always assume the number we want to raise by some power is 2. Example: ?^? = 8 can be rewritten as 2^? = 8 which can be rewritten as Log base 2 of 8 = 3.

Let's use a recursive function to visualize O(log n):

n=8

def logFunc(n):
    if n = 0:
        return "Done"
    n = n//2
    return logFunc(n)

------------------------------------------------------------------------------------
O(n log n): Linearithmic

n=4

def n_log_n_func(n):
    y = n
    while n > 1:              #O(log n)
        n = n//2
        for i in range(1, y): #O(n)
            print(i)

This function's while loop has a complexity of O(log n), we can prove this by rewriting this as O(log base 2 of 4) -> Log base 2 of 4 = 2. We can see that this function's while loop only executes 2 times, proving that it is, in fact, of O(log n) complexity.

The nested for loop is a Linear complexity. Since it executes y number of times, we can say that O(n * log n) -> O(4 * 2) where 4 is the number of times the for loop executes per the number of times the while loop executes. We can express this complexity as O(n log n) for the function as a whole.

------------------------------------------------------------------------------------
O(2^n): Exponential

def fib(n):
    if n = 0:
        return 0
    if n = 1:
        return 1
    return fib(n-1) + fib(n-2)

This function's complexity is O(2^n). Let `n = 4`. By the time this function is done executing we will have gone three "levels" deep in the recursive calls with each "level" increasing in it's call to `fib()`. Level 1 will call `fib` twice, level 2 will call `fib()` four times, and level 3 executes twice, but for the sake of the example, let's imagine that three of the four calls to `fib()` were not returned and continued to execute. That would have level 3 executing 8 times. If there were a level 4 of this function, it would call `fib()` 16 times. This shows that the calls to `fib()` are growing exponentially depending on what we assign to `n`. 

In actuality, the notation for this function is O(2^n-1). Using our example; O(2^4-1) -> O(2^3). When we have an exponent, in Big-O, we can just substitute that exponent for `n`. This makes the final form of this notation O(2^n) or Exponential.

------------------------------------------------------------------------------------
O(n!): Factorial

def f(n):
    if n = 0:
        print("*****")
        return
    
    for i in range(n)
        f(n-1)

Let's say `n=3` for each index up until `n` starting at 0, we will recursively call `f(n-1)`. This will result in three calls to `f(2)` in our example, totalling in 3 calls to `f(2)`. And each of those three `f(2)` will call `f(1)` twice, totalling in 6 calls to `f(1)`. Finally, with `f(1)`, it will recursively call `f(1-1)`, or `f(0)` six more times before finally executing the print statement six times and returning. Passing `n=3` resulted in the need to recursively call our function six times. Therefore, the complexity of this function is O(3!). Which can be simplified to O(n!).
