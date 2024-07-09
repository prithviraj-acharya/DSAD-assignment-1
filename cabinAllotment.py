"""
A class to manage cabin allotment based on booking IDs.

Author: Group 13
Year: 2024

"""


class CabinAllotment:

    def __init__(self, input_file, output_file):
        """
        Initializes the CabinAllotment class with input and output file paths.

        :param input_file: Path to the input file containing booking IDs.
        :param output_file: Path to the output file for writing the results.

        """
        self.input_file = input_file
        self.output_file = output_file
        self.first_set_ID = []
        self.second_set_ID = []
        self.third_set_ID = []
        self.fourth_set_ID = []

    def read_input(self):
        """
        Reads booking IDs from the input file and stores them in a list.
        """
        try:
            with open(self.input_file, "r") as f:
                self.first_set_ID = list(map(int, f.readline().strip().split(",")))
                self.second_set_ID = list(map(int, f.readline().strip().split(",")))
                self.third_set_ID = list(map(int, f.readline().strip().split(",")))
                self.fourth_set_ID = list(map(int, f.readline().strip().split(",")))
        except FileNotFoundError:
            print(f"Error: File '{self.input_file}' not found.")

    def calculate_median(self, sorted_ids):
        """
        Calculates the median of the sorted booking IDs.

        :param sorted_ids: A list of sorted booking IDs.
        :return: The median value.
        """

        n = len(sorted_ids)
        if n % 2 == 1:
            return sorted_ids[n // 2]
        else:
            # In case of even length, pick either middle element
            return sorted_ids[n // 2]

    def categorize_rooms(self, sorted_ids):
        """
        Categorizes booking IDs into suite, balcony, outside, ocean view, and interior rooms based on medians.

        :param sorted_ids: A list of sorted booking IDs.

        """
        def split_by_median(ids):
            median = self.calculate_median(ids)
            return ids[:ids.index(median) + 1], ids[ids.index(median) + 1:]

        sorted_booking_ids = self.heap_sort(self.first_set_ID)
        suite_ids, balcony_ids = split_by_median(sorted_booking_ids)

        balcony_ids.extend(self.second_set_ID)
        id_list2 = self.heap_sort(balcony_ids)
        balcony_ids, outside_rooms_ids = split_by_median(id_list2)

        outside_rooms_ids.extend(self.third_set_ID)
        id_list3 = self.heap_sort(outside_rooms_ids)
        outside_rooms_ids, ocean_view_ids = split_by_median(id_list3)

        ocean_view_ids.extend(self.fourth_set_ID)
        id_list4 = self.heap_sort(ocean_view_ids)
        ocean_view_ids, interior_ids = split_by_median(id_list4)

        # Output to file
        with open(self.output_file, "w") as f:
            # Write output to file
             f.write(f"Suite rooms were allocated to Ids:  {suite_ids}\n")
             f.write(f"Outside rooms were allocated to Ids:  {outside_rooms_ids}\n")
             f.write(f"Ocean view rooms were allocated to Ids:  {ocean_view_ids}\n")

    def execute(self):
        """
        Executes the main logic of reading input, sorting, and categorizing booking IDs.
        """
        self.read_input()
        if self.first_set_ID:
            sorted_booking_ids = self.heap_sort(self.first_set_ID)
            print("HeapSort --> ", sorted_booking_ids)
            self.categorize_rooms(self.first_set_ID)

    def heapify(self, arr, length, parentIdx):
        largest = parentIdx
        left = 2 * parentIdx + 1
        right = left + 1

        if left < length and arr[left] > arr[largest]:
            largest = left

        if right < length and arr[right] > arr[largest]:
            largest = right

        if largest != parentIdx:
            self.swap(arr, parentIdx, largest)
            self.heapify(arr, length, largest)

    def heap_sort(self, bookingIds):
        """
        Sorts the booking IDs using heap sort algorithm and returns the sorted list.

        :return: A list of sorted booking IDs.
        """
        # arr = self.first_set_ID
        arr = bookingIds
        length = len(arr)
        last_parent_idx = length // 2 - 1
        last_child_idx = length - 1

        # Creating a heap from the given array
        while last_parent_idx >= 0:
            self.heapify(arr, length, last_parent_idx)
            last_parent_idx = last_parent_idx - 1

        while last_child_idx >= 0:
            self.swap(arr, 0, last_child_idx)
            self.heapify(arr, last_child_idx, 0)
            last_child_idx = last_child_idx - 1

        return arr

    def swap(self, arr, i, j):
        """
        Swaps two elements in an array or list using tuple unpacking for a more Pythonic approach.

        :param arr: The array or list where the swap operation will be performed.
        :param i: The index of the first element to be swapped.
        :param j: The index of the second element to be swapped.
        """
        arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    INPUT_FILE = "inputPS05.txt"
    OUTPUT_FILE = "outputPS05.txt"
    cabin_allotment = CabinAllotment(INPUT_FILE, OUTPUT_FILE)
    cabin_allotment.execute()
