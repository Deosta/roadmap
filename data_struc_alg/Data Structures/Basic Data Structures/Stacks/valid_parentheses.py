# Given a string of s of only brackets, return true if s is valid and false otherwise
def isValid(s: str) -> bool:

    #empty stack data structure to store and preform work on the passed data
    stack = []

    #If there is a closing object, we expect to see an opening object
    mapping = {
        "}": "{",
        "]": "[",
        ")": "(",

    }
    #iterate through the string
    for c in s:
        #if we see an open object, throw it in the stack
        if c in mapping.values():
            stack.append(c)
        #otherwise, if the stack is NOT EMPTY, and compare mapping[c] to the to top element in the list. If that key:value pair evaluates as true, pop.
        else:
            if stack:
                if mapping[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
    return len(stack) == 0

if __name__ == "__main__":
    print(isValid("{}[]()"))
    print(isValid("{{}"))
    print(isValid("{{"))
    print(isValid("{"))
    print(isValid("({[]})"))