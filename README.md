# Minimum-Number-Of-Racks

solution to minimum rack problem
Find the minimum number of racks required for servers of various height.
Constraints:
  each rack can only have a maximum of 2 servers
  the sum of the servers on the rack must not exceed the Height, below example being 5.
  the server height cannot be taller than the rack height(below example being 5)

**************************************************************************************

Example run below:


python main.py
Input Height
5
Input Number Of Servers
10
Input Servers
2 3 4 1 2 2 3 1 5 2
[5, 4, 3, 3, 2, 2, 2, 2, 1, 1]
racks are  [[5], [4, 1], [3, 2], [3, 2], [2, 2], [1]]
rackOfInterest 5
The minimum number of racks required are  6
