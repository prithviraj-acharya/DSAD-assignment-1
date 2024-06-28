**Problem Statement**

A cruise ship is ready to move to different islands and to book to the premium rooms in that there is a
huge crowd at the booking counter. As there were few premium rooms available, the crew
members decided to apply median from the confirmed list of unique Booking ID’s. At every
median set performed the types of rooms allotted will be varied.

Crew members ask you to perform these tasks in order to allot rooms accordingly.
1. Sort the unsorted confirmed list of ‘n’ booking IDs in ascending order using Heap sort.

2. Perform median for ordered/sorted confirmed list. (At this level suite rooms were allotted)
Note: While performing the median, if the number of elements is even, then choose either
of the element according to its position (ex: Given ID’s as 1, 6, 9, 11 ---- now select either
6 or 9 as median).

3. If a new set of ID’s were confirmed then include them to the rest of sorted list after the median
element, then again perform sort and median to those set of the elements. (At this Level
Balcony rooms and in the next levels outside rooms, ocean view rooms, interior rooms and
soon were allotted respectively).

4. Print the Booking Ids who got Suite, Outside and Ocean view rooms.

Requirements:
1. Model the problem as a Heap.
2. Read the input from a file inputPS05.txt.
3. You will output your answers to a file outputPS05.txt.
4. Perform an analysis for the features above and give the running time in terms of input
size: n.
5. Make sure proper exception handling is written for the code.
6. Implement the above problem statement using python 3.7 and above.

Sample Input
The input file InputPS05.txt will contain Booking IDs of each person in the form of array as shown
below.
167, 890, 345, 23, 67, 451, 79, 92, 333, 520, 788, 13, 89
New Set of confirmed IDs added for allotting Balcony rooms
(Note: These new values can be prompted to user after performing median)
673, 888, 301, 287, 110, 499
New Set of confirmed IDs added for allotting Out Side rooms
(Note: These new values can be prompted to user after performing median)
75, 812, 200, 45, 15, 99
New Set of confirmed IDs added for allotting Ocean View rooms
(Note: These new values can be prompted to user after performing median)
111, 222, 444, 555, 666, 777
New Set of confirmed IDs added for allotting Interior rooms
(Note: These new values can be prompted to user after performing median)
10, 29, 999, 101, 350, 500
Note that the input/output data shown here is only for understanding and
testing, the actual file used for evaluation will be different.

Sample Output
Sorted ID List: (Suite Rooms)
13, 23, 67, 79, 89, 92, 167, 333, 345, 451, 520, 788, 890
Median element: 167 (up to this ID suite rooms are allocated)
After new set of IDs Added then sorted list: (balcony)
(Note: select elements after median value and the new set of Ids to perform sorting
I.e. 333,345,451,520,788,890, 673,888,301,287,110,499)
110, 287, 301, 333, 345, 451, 499, 520, 673, 788, 888, 890
Median element: 499
(Note: number of elements is 12 which is even so u can choose either 451 or 499 as
median value in this case)
After new set of IDs Added then sorted list: (Out side rooms)
(Note: select elements after median value and the new set of Ids to perform sorting
I.e. 520, 673, 788, 888, 890, 75, 812, 200, 45, 15, 99 )
15, 45, 75, 99, 200, 520, 673, 788, 812, 888, 890
Median element: 520
After new set of IDs Added then sorted list: (673, 788, 812, 888, 890, 111, 222, 444, 555, 666,
777) (ocean View rooms)
111, 222, 444, 555, 666, 673, 777, 788, 812, 888, 890
Median element: 673
After new set of IDs Added then sorted list: (777, 788, 812, 888, 890, 10, 29, 999, 101, 350, 500)
(Interior rooms)
10, 29, 101, 350, 500, 777, 788, 812, 888, 890, 999
Suite rooms were allocated to Ids: 13, 23, 67, 79, 89, 92, 167
Outside rooms were allocated to Ids: 15, 45, 75, 99, 200, 520
Ocean view rooms were allocated to Ids: 111, 222, 444, 555, 666, 673

Note that the input/output data shown here is only for understanding and
testing, the actual file used for evaluation will be different.

Display the output in outputPS05.txt.
