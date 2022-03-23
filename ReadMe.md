## Front to Back Word Search Algorithm and Linked List
This project contains two files:


**word_search.py**
This file contains a front and back algorithm for searching through an unsorted array of words.
The front and back algorithm is optimal for searching through an unsorted array of word as it implements a linear 
search from the front and the back of the array simultaneously. This algorithm method does not affect the complexity
of the search (which is still O(n)) but reduces the time complexity to theoretically half the time it will take for 
a regular linear search. the space complexity is O(1).
 
I have implemented this search in an OOP paradigm to utilize abstraction, encapsulation, and also to allow possible
polymorphism of the algorithm if need be for the purpose of supercharging or any other reason.
  

To use this for search, first create a variable of the array
```
arr = word_arr = ["Wing", 'Jumbo', "mark", "juke", "james"]
```
create an instance of the WordBank class and initialise it with the array

```
word_bank = WordBank(arr)
```
call the `has_word()` method on the instance and pass in the word to search for as an argument

```
word_exists = word_bank.has_word("jumbo")
print(word_exists)
>>> True
```


**linked_list.py**
This file contains a linked list of several nodes. The nodes are linked together singly to form a linear sequence of
linked elements. There are two classes in the file 
1. Node: This is the class for creating several Node instances
2. LinkedList: This is the class that links the nodes to form a linkedlist.

Several methods have been implemented into the linkedlist that uses the transversal of a linkedlist to traverse through the nodes and 
perform operations where necessary. These methods are:
**view_list()**
prints out the data of all the nodes on the linkedlist

**fetch_head()**
returns the current head of the linkedlist

**next_value(target)**
returns the data of the node after the target node passed into the method

**preceding_value(target)**
returns the data of the node before the target node passed into the method

**add_element(item)**
creates a node with the item at the end of the linkedlist

**add_element_to_start(item)**
creates a node with the item at the beginning of the linkedlist

**remove_node(target)**
removes the node with the target data from the linkedlist



Open and run the main.py file to see a demo of the two files.