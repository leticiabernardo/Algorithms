# Linked List

A Linked List is a linear and dynamic data structure. It consists of a sequence of nodes that are connected through pointers, i.e., a node points to the next neighboring node.<br />
The nodes don't have to be close to each other, so you can create a new node using any computer's RAM space, making it dynamic.<br />
In essence, each node is composed of a piece of data and a reference (in a more basic way a link) to the next element.<br />
Below is an example of this data structure model.

<p align="center">
  <img src="https://user-images.githubusercontent.com/13439423/156976326-9822f52a-26fe-4544-9c99-a8f796621f2f.jpg"/>
</p>

This type of structure allows you to insert and delete nodes efficiently, but one of the disadvantages of this structure is that it performs linear searches.<br />
Anyway, the Linked List is one of the simplest and most common data structures.

## Comparing algorithm complexity with arrays

| | Array | Linked List |
| --- | --- | --- |
| Indexing | O(1) | O(n)|
| Insert/Delete element at start | O(n) | O(1)|
| Insert/Delete element at end | O(1) - amortized | O(n) |
| Insert element in middle | O(n) | O(n) |



