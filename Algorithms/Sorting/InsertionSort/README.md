# Insertion Sort

Insertion sort is a simple sorting algorithm on several websites I've researched says that it works similar to how you sort cards in your hands.<br />
Where the set is pretty much divided into an ordered part and an unordered part. The values from the unordered part are chosen and placed in the correct position in the ordered part.<br />

## How it works 
If the element is the first element, assume it is already sorted. Keep and move on to the next, or start from the next item.<br />
When choosing the next element, you need to sort on an auxiliary variable.<br />
Now iterate through the array and compare each item with the auxiliary.<br />
If the element of the array is smaller than the auxiliary, then place the element at the index of the element where the auxiliary variable's value used to be, and iterate left and move the elements to the right as long as the auxiliary is smaller. If the auxiliary is larger than the previous element, its new index will be the current element, set the auxiliary's value at the current index.
And do this consecutively until the last item in the array.<br />

The image below shows how the algorithm works step by step:

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif" /><br />
  <sub><a href="https://en.wikipedia.org/wiki/Insertion_sort">[wikipedia]</a></sub>
</p>

## Links
- [Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort)
