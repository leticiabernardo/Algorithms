# Hash Table

The Hash Table (hash map) is the most used data structure that aims to store data by associating keys to abstract data, so to find the desired data just do a quick search for the simple key.

## How it works?

In short, to save data in a Hash Table structure you need to create a key and value structure, where the key is transformed into a hash and the stored value can be any abstract data. <br />
Whenever the algorithm does some action, such as a search, the algorithm must take the passed simple key and transform it into a hash to perform the search. In Hash Tables we can think of the same structure as a python dictionary, but the keys are hashes. <br />
See the example in the figure below:

<div align="center">
  <img src="https://user-images.githubusercontent.com/13439423/156956581-df901e6e-5c33-4710-a039-eaadbf2e3508.jpg" />
</div>

## Basic functions

The basic functions of a hash table are:

| Function | Description |
| --- | --- |
| Search | Fetch an element |
| Insert | Insert an element |
| Delete | Delete an element |

## Generating the hash function

A hash function, also known as a spread function is a way to map the keys into the index set of the table. An example of a hash is to use the integer value of its unicode character and return its MOD. <br />
Take a look at this example:

```python
def get_hash(self, key):
 h = 0
 for char in key:
     h += ord(char)
 return h % self.MAX
```

## Handling key collisions

A popular solution for resolving collisions is known as separate chaining.<br />
So for each index **x** in the table there is a linked list that stores all the objects that the distribution function takes into **x**. This linked list can be navigated through to access the item with a unique search key.<br />

<div align="center">
  <img src="https://user-images.githubusercontent.com/13439423/156959571-420ee84d-4586-45a0-afdf-aa558d5d3f5a.jpg" />
</div>

## Examples:

- [Linked List](https://github.com/leticiabernardo/Algorithms/blob/main/DataStructures/05_HashTable/hash_table.py)
- [Linked List with Collision](https://github.com/leticiabernardo/Algorithms/blob/main/DataStructures/05_HashTable/hash_table_with_collision.py)

## Links 

- [wikipedia](https://en.wikipedia.org/wiki/Hash_table)
- [hackerearth](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/)



