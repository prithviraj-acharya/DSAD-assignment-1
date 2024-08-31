# Cabin_Allotment_DSAD_A1
DSAD Assignment 1

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
