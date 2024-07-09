import heapq

input_file = "inputPS05.txt"
output_file = "outputPS05.txt"

# Read input from file
try:
    with open(input_file, 'r') as f:
        first_set_ID = list(map(int, f.readline().strip().split(",")))
        second_set_ID = list(map(int, f.readline().strip().split(",")))
        third_set_ID = list(map(int, f.readline().strip().split(",")))
        fourth_set_ID = list(map(int, f.readline().strip().split(",")))
        fifth_set_ID = list(map(int, f.readline().strip().split(",")))
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")

# Heapify the array
def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr

# Median Calculation
def calculate_median(sorted_ids):
    n = len(sorted_ids)
    if n % 2 == 1:
        return sorted_ids[n // 2]
    else:
        # In case of even length, pick either middle element
        return sorted_ids[n // 2]

# Categorize rooms
def categorize_rooms(first_set_ID):
    
        #First Sorted List
        sorted_booking_ids = heap_sort(first_set_ID)
        median = calculate_median(sorted_booking_ids)
        #Categorize rooms on First set of IDs
        suite_ids = sorted_booking_ids[:sorted_booking_ids.index(median) + 1]
        balcony_ids = sorted_booking_ids[sorted_booking_ids.index(median) + 1:]

        # Merge Second set of IDs with First set after Median IDs
        balcony_ids.extend(second_set_ID)
        id_list2 = heap_sort(balcony_ids)
        median = calculate_median(id_list2)
        #Categorize rooms on Second set of IDs
        balcony_ids = id_list2[:id_list2.index(median) + 1]
        Outside_rooms_ids = id_list2[id_list2.index(median) + 1:]

        # Merge Third set of IDs with Second set after Median IDs
        Outside_rooms_ids.extend(third_set_ID)
        id_list3 = heap_sort(Outside_rooms_ids)
        median = calculate_median(id_list3)
        #Categorize rooms on Third set of IDs
        Outside_rooms_ids = id_list3[:id_list3.index(median) + 1]
        Ocean_view_ids = id_list3[id_list3.index(median) + 1:]

         # Merge Fourth set of IDs with Third set after Median IDs
        Ocean_view_ids.extend(fourth_set_ID)
        id_list4 = heap_sort(Ocean_view_ids)
        median = calculate_median(id_list4)
        #Categorize rooms on Fourth set of IDs
        Ocean_view_ids = id_list4[:id_list4.index(median) + 1]
        Interior_ids = id_list4[id_list4.index(median) + 1:]


    # Output to file
        with open(output_file, 'w') as f:
    # Write output to file
          f.write(f"Suite rooms were allocated to Ids:  {suite_ids}\n")
          f.write(f"Outside rooms were allocated to Ids:  {Outside_rooms_ids}\n")
          f.write(f"Ocean view rooms were allocated to Ids:  {Ocean_view_ids}\n")

# Categorize rooms based on sorted list
try:
    categorize_rooms(first_set_ID)
except Exception as e:
    print(f"Error: {e}")


f.close()   