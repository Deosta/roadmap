# Given a path, the canonical path should have the following format:
# 1. starts with '/'
# 2. Any two directories are separated by a single slash '/'
# 3. Does not end with a trailing '/'
# 4. Only contains the directories on the path from the root directory to the target file or directory

path = "/home/../../tmp//./"
stack = []
path_to_return = ""

for directory in path.split("/"):
    #return with empty string, nothing to do
    if directory == "":
        pass
    #the single period, in this case, means to stay in the current directory, so pass if the current element in the string is a .
    elif directory == ".":
        pass
    #the double period means to go back one, in this case we would pop the element containing the .. effectively going back to the previous location in the directory. If there is nothing in the stack except a double period, pass
    elif directory == "..":
        if stack:
            stack.pop()
        else:
            pass
    #otherwise, append the current element of the split string to the stack
    else:
        stack.append(directory)
path_to_return = "/" + "/".join(stack)

#given the path, should return /tmp
print(path_to_return)