# Stack

The stack is a LIFO (Last In First Out) linear data structure. So, the stack only allows access to one item - the last item. In order to process the second-to-last item, the last item must be removed.

<p align="center">
  <img src="https://user-images.githubusercontent.com/13439423/157058935-726977ba-6515-4c5c-9c21-39b3f0662e69.jpg"/>  
</p>

## Basic functions

| Function | Description |
| --- | --- |
| Create stack | Create the stack, must inform the capacity in case of sequential implementation (vector) |
| Stack (push) | Insert an element in top |
| Unstack (pop) | Delete an element in top |
| Show top (peek) | Show the top element without removing it |
| Is Stack empty? (isEmpty) | check if the stack is empty |
| Is Stack full? (isFull) | check if the stack is full |

## Big O

- Pop / push element: O(1);
- Search element by value: O(n).

## Examples of stack are:

- Recursive functions in compilers;
- Undo/redo mechanism in text editors;
- Navigation between web pages.
