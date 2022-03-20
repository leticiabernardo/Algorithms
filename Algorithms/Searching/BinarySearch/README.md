# Binary Search

Binary search is an algorithm that implements the Divide and Conquer paradigm to find an element in an ordered array.<br />

The binary search looks for a given value by comparing the middle item in the list.<br />
- If it is equal, the index of the item is returned.
- If the item sought is smaller than the middle of the list, the item is searched for in the submatrix to the left of the middle item.
- If the item is greater than the middle of the list, the item is searched for in the submatrix to the right of the middle item.
<br />

This process continues recursively splitting the subarrays until the item is found or until it can no longer subdivides (equals 1), then we conclude that the item has not been found.
The image below shows the algorithm step by step:
<p align="center">
  <img src="https://user-images.githubusercontent.com/13439423/159151524-ab877cfe-5517-4ab5-9b6f-1217f6f32c34.jpg" />
</p>
