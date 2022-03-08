# Tree

The tree data structure is a non-linear and dynamic structure, i.e. the elements in the tree are not stored sequentially, nor are they linked together like a list. 
<br />
In this structure there are a finite number of elements, each of which is called a node.<br />
A tree stores its data in a hierarchical way, where there is an element at the top of the tree, called the **root**, and there are subordinate elements to it that are called **child nodes**. Each child can contain zero, one or more child nodes. Child nodes that have no other child nodes are called **leaf nodes**.
<br />
See the representation below:

<p align="center">
  <img src="https://user-images.githubusercontent.com/13439423/157177330-a9228f8c-6693-48c5-b5ef-e373f41001e6.jpg" />
</p>

Each child node stores a data type and pointers to the left and right elements, which allows insertion of values into the tree recursively.<br />
In short, the representation of a tree is a graph without cycles.

## Elements of a Tree

- **Node (vertex)**: Element that contains the information
- **Edge**: Connects two nodes
- **Parent**: top node of an edge
- **Child**: bottom node of an edge
- **Root**: top node - does not have a parent node
- **Leaf**: lower end node - which have no children
- **Level or Depth**: Represents the distance between the root and a specific node
- **Height of the tree**: the maximum level of nodes in a tree
- **Forest**: is a set of zero or more trees, in the example of the picture below, there are 2 trees that make up a forest


<p align="center">
  <img src="https://user-images.githubusercontent.com/13439423/157181828-ae39b516-e187-4d7a-be50-280b3fc2389c.jpg" />
</p>

- **Complete tree**: when all children have exactly `d` children except leaves and all leaves are the same height. In the example below, the tree of degree `d=3` is complete.


<p align="center">
  <img src="https://user-images.githubusercontent.com/13439423/157183981-91bbb7d6-2415-48df-b763-a2dd83e332d2.jpg" />
</p>

- **Path**: is composed from the root to the desired node. In the example below, A, C, H is a path between A and H.

<p align="center">
  <img src="https://user-images.githubusercontent.com/13439423/157184797-4952dbda-df64-4b9f-87bf-c227e1c2d75f.jpg" />
</p>

## Operations of a tree

| Function | Description |
| --- | --- |
| Root operation | returns the root of the tree. In the case of an empty tree, returns the null value |
| Parent operation of a node | returns the parent of that node. If the node is the root, returns an error |
| Child operation of a node | receives the node and must return the set of child nodes belonging to it |
| Test operation if a node is a leaf | checks if the node is a leaf, i.e. it has no children |
| Operation to test if a node is internal | checks if the node is internal to the tree, that is, if it has children |
| Operation size | returns the number of nodes in the tree |
| Operation to test if it is empty | checks if a tree is empty, i.e. it has no nodes |

## Examples of use

Some practical examples of using a tree are:
- Folder structure
- Hierarchy representations: family tree, university hierarchy, etc.
- Arithmetic expression solution
- Algorithm modeling
- Numbering by levels
- Bar diagram
