#This example is VERY overly commented on purpose.

#Class used to instantiate Node objects used in the linked list. 
#These Node objects will have two properties: data (can be int, str, complex objects, ect..) next which serves as the pointer to the next Node object in the list. 
#If there is no next, it will be None.
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


#Class used to instantiate LinkedList objects.
#The only property of a LinkedList object will be head to indicate the start of the linked list.
#This class will have many methods used to preform work on the data in the linked list object
class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        position = self.head
        linked_list_str = ""
        while position:
            linked_list_str += str(position.data) + ' --> '
            position = position.next
        print(linked_list_str)


    def get_length(self):
        count = 0
        position = self.head
        while position:
            count += 1
            position = position.next
        return count
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        #if nothing is in the list, set the head equal to the new Node object using the data passed and None for next to ensure it's put at the end of the linked list.
        if self.head is None:
            self.head = Node(data, None)
            return

        #Otherwise create a positional variable and set it equal to the head (the start of the linked list)
        position = self.head

        #While position.next is NOT None, we iterate through the linked list to get to the last position. Once at the last position, we will create a new Node object with the passed data and None for next to ensure the new object is placed at the END of the list.
        while position.next:
            position = position.next
        position.next = Node(data, None)
    
    def insert_values(self, data_list):
        #setting the head to None to remove/overwrite any existing Node objects.
        self.head = None
        #iterate through the passed data_list and call the insert_at_end to create new Node objects and insert them at the end of the linked list
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        #check for out of index occurrences
        if index < 0 or index > self.get_length():
            raise Exception("Out of index")
        
        #if at 0 index, insert at the beginning
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        #otherwise, set a count variable to 0 and a positional variable to head(start of list)
        #Then while position is not None find where the count is equal to index -1(we want to insert at the position before the passed index to maintain list order)
        count = 0
        position = self.head
        while position:
            if count == index - 1:
                node = Node(data, position.next)
                position.next = node
                break
            position = position.next
            count += 1

    def remove_at(self, index):
        #check for out of index occurrences
        if index < 0 or index > self.get_length():
            raise Exception("Out of index")

        #if at the 0 index, we want to set the head(start of list) to the next element in the linked list
        if index == 0:
            self.head = self.head.next
            return
        
        #Otherwise, set a count variable to 0, a positional variable to head, and while the positional variable is not None, we compare count to index - 1 (again, we want to stop at the index before the one we want to do work on). Where these are equal, we set the next position to next -> next effectively overwriting the desired Node object, finally break out of the loop.
        count = 0
        position = self.head
        while position:
            if count == index - 1:
                position.next = position.next.next
                break
            position = position.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):

        if self.head is None:
            print('you got to None')
            return
        
        if self.head.data == data_after:
                print("You got to the head.data")
                self.head.next = Node(data_to_insert, self.head.next)
                return
        
        position = self.head
        while position:
            if position.data == data_after:
                position.next = Node(data_to_insert, position.next)
                break            
            position = position.next

    def remove_by_value(self, data):

        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        position = self.head
        while position.next:
            if position.next.data == data:
                position.next = position.next.next
                break
            position = position.next

if __name__ == '__main__':
    ll = LinkedList()
    #do work here