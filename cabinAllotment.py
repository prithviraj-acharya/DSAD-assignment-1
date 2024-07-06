import heapq

input_file = "inputPS05.txt"
output_file = "outputPS05.txt"

# Read input from file
try:
    with open(input_file, 'r') as f:
        booking_ids = list(map(int, f.read().strip().split(",")))
        print("Booking IDs --> " , booking_ids)
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")



# Heapify the array
def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr

# Sort using heap sort
try:
    sorted_booking_ids = heap_sort(booking_ids)
    print("HeapSort --> " , sorted_booking_ids)
except Exception as e:
    print(f"Error: {e}")

# Median Calculation
def calculate_median(sorted_ids):
    n = len(sorted_ids)
    if n % 2 == 1:
        return sorted_ids[n // 2]
    else:
        # In case of even length, pick either middle element
        return sorted_ids[n // 2 - 1]

# Categorize rooms
def categorize_rooms(sorted_ids):
    n = len(sorted_ids)
    median = calculate_median(sorted_ids)
    
    suite_ids = sorted_ids[:sorted_ids.index(median) + 1]
    balcony_ids = sorted_ids[sorted_ids.index(median) + 1:]
    
    # Dummy print for testing
    print("Suite Rooms --> ", suite_ids)
    print("Balcony Rooms --> ", balcony_ids)

    # Output to file
    with open(output_file, 'w') as f:
    # Write output to file
        f.write(f"Suite Rooms :  {suite_ids}\n")
        f.write(f"Balcony Rooms :  {balcony_ids}\n")

# Categorize rooms based on sorted list
try:
    categorize_rooms(sorted_booking_ids)
except Exception as e:
    print(f"Error: {e}")


