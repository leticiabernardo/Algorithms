# Shell Sort

Shell Sort is essentially a variation of Insertion Sort and can be seen as a generalization of bubble sort. In insertion sorting, we move the elements only one position in front. When an element needs to be moved very much to the front, many moves are necessary. The idea of the Shell Sort is to allow the swapping of remote items. <br />
The method instead of breaking the list into sublists of adjacent items, the shell sort uses an increment i, sometimes called a gap, to create a sublist by picking all items that are i items away from each other.

## How it works?

Let's look at a simple example with the unordered array:
`arr = [7, 4, 15, 10, 9, 2]`. 

The first step is to find out the interval, that is, how the array will be partitioned to create sublists.

In this case, we can always divide with `N/3 = 6/3 = 2` to define the interval between each item in the array for generating the sublist.
See the example below:

<p align="center">
  <img src="https://user-images.githubusercontent.com/13439423/159189855-6d3960ab-5c73-4845-a986-e4de7a39309b.jpg" /><br/>
  <img src="https://user-images.githubusercontent.com/13439423/159190152-703cb4ef-5c97-4b69-b73e-f252977c2126.jpg" />
</p>

So, in next step, we divide again, but with interval `N/6 = 6/6 = 1`. See the next image below:

<p align="center">
  <img src="https://user-images.githubusercontent.com/13439423/159190483-ffee00ba-051e-4969-be8f-8b48732ad3e2.jpg" />
</p>

In Shell Sort, part of the logic of the [Insertion Sort](https://github.com/leticiabernardo/Algorithms/tree/main/Algorithms/Sorting/InsertionSort) is used to sort each sublist.


#### Explaining the range of arrays

Shell Sort partition range can be done using the above example formula.<br />
To get each interval we can start with: `interval = arr_size // 2`
And we divide the interval between itself, as follows: `interval //= 2` or `interval = interval // 2`.<br />
Thus, it will divide until its final range remains **1**.

## Links
- [Wikipedia](https://en.wikipedia.org/wiki/Shellsort)
- [Programiz](https://www.programiz.com/dsa/shell-sort)
- [Javatpoint](https://www.javatpoint.com/shell-sort)
