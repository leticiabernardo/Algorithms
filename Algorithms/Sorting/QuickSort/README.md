# Quick Sort

Quicksort, invented by [Tony Hoare](https://pt.wikipedia.org/wiki/Charles_Antony_Richard_Hoare) in 1959 and published in 1961, is the most efficient algorithm in comparison sorting, it is a divide-and-conquer algorithm. 
The idea of this algorithm is to choose an element as a pivot, sort the pivot in its place and all elements smaller than it come before it. And the one that is bigger gets after it. After that it is partitioned into two arrays, one with those smaller than it and all the numbers after it that are larger than it.
It then does the same processing, splits its input list into two sub-lists from a pivot, and then performs the same procedure on the two smaller lists to a unit list.

## Step by step

- Chooses an element from the list called pivot.
- Rearranges the list so that elements smaller than the pivot are on one side and larger ones on the other.
- Recursively sort the sublist below and above the pivot.

<p align="center">
   <img src="https://d2m498l008ebpa.cloudfront.net/2016/12/quicksort.gif" /><br/>
   <sub><a href="https://en.wikipedia.org/wiki/File:Sorting_quicksort_anim.gif">[wikipedia]</a></sub>
</p>

## Methods
Three specific partition methods will be mentioned here.


### Hoare Partition

Hoare partitioning was proposed by Tony Hoare when the Quicksort algorithm was originally first published. Instead of working up the array from bottom to top, Hoare uses two indices that start at the ends of the array being partitioned, then move toward each other until he detects an inversion: a pair of elements, one larger than the pivot, one smaller, in the wrong order relative to each other. The inverted elements are then swapped. When the indexes meet, the algorithm stops and returns the final index.
 This means that we have more iterations and more comparisons, but fewer swaps.

This can be important, because often comparing memory values is cheaper than swapping them.

### Lomuto Partition

This algorithm is attributed to Nico Lomuto. 
In most formulations this scheme chooses as pivot the last element of array. It iterates over the input array, swapping elements that are strictly smaller than the pre-selected pivot element to the beginning of the list by swapping with index item. It then places the pivot item at its index and splits the array into two, a group of elements smaller than the pivot and others with elements larger than the pivot. And it is made sequentially the same process all items are sorted, it is merge the smaller and larger elements to return the complete list.


### Naive Partition

This algorithm is intended to maintain the relative order of the elements while sorting them. 
a temporary array is created in which we first store the elements that are less than the pivot, and then the elements that are greater than the pivot. Then a temporary array is created, copying the temporary array to the original array.
It is not widely used because of its performance, it is slower due to the time it takes to scan the input and copy items into a new output matrix.

## Links

- [Wikipedia](https://en.wikipedia.org/wiki/Quicksort)
- [Stackexchange - Hoare vs Lomuto](https://cs.stackexchange.com/questions/11458/quicksort-partitioning-hoare-vs-lomuto)
