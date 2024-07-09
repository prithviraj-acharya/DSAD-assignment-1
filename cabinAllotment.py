import heapq


class CabinAllotment:
    """
    A class to manage cabin allotment based on booking IDs.
    """

    def __init__(self, input_file, output_file):
        """
        Initializes the CabinAllotment class with input and output file paths.

        :param input_file: Path to the input file containing booking IDs.
        :param output_file: Path to the output file for writing the results.
        """
        self.input_file = input_file
        self.output_file = output_file
        self.booking_ids = []

    def read_input(self):
        """
        Reads booking IDs from the input file and stores them in a list.
        """
        try:
            with open(self.input_file, "r") as f:
                self.booking_ids = list(map(int, f.read().strip().split(",")))
                print("Booking IDs --> ", self.booking_ids)
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
            return (sorted_ids[n // 2 - 1] + sorted_ids[n // 2]) / 2

    def categorize_rooms(self, sorted_ids):
        """
        Categorizes booking IDs into suite and balcony rooms based on the median.

        :param sorted_ids: A list of sorted booking IDs.
        """
        median = self.calculate_median(sorted_ids)
        suite_ids = [id for id in sorted_ids if id <= median]
        balcony_ids = [id for id in sorted_ids if id > median]

        print("Suite Rooms --> ", suite_ids)
        print("Balcony Rooms --> ", balcony_ids)

        with open(self.output_file, "w") as f:
            f.write(f"Suite Rooms :  {suite_ids}\n")
            f.write(f"Balcony Rooms :  {balcony_ids}\n")

    def execute(self):
        """
        Executes the main logic of reading input, sorting, and categorizing booking IDs.
        """
        self.read_input()
        if self.booking_ids:
            sorted_booking_ids = self.heap_sort()
            print("HeapSort --> ", sorted_booking_ids)
            self.categorize_rooms(sorted_booking_ids)

    def heapify(self, arr, length, parentIdx):
        largest = parentIdx
        left = 2 * parentIdx + 1
        right = left + 1

        if left < length & arr[left] > arr[largest]:
            largest = left

        if right < length & arr[right] > arr[largest]:
            largest = right

        if largest != parentIdx:
            self.swap(arr, parentIdx, largest)
            self.heapify(arr, largest)

    def heap_sort(self):
        """
        Sorts the booking IDs using heap sort algorithm and returns the sorted list.

        :return: A list of sorted booking IDs.
        """
        arr = self.booking_ids.copy()
        length = len(arr)
        last_parent_idx = length // 2 - 1
        last_child_idx = length - 1

        while last_parent_idx >= 0:
            self.heapify(arr, length, last_parent_idx)
            last_parent_idx = last_parent_idx - 1

        while last_child_idx >= 0:
            self.swap(arr, 0, last_child_idx)
            self.heapify(arr, last_child_idx, 0)
            last_child_idx = last_child_idx - 1

        return arr
        # heapq.heapify(arr)
        # sorted_arr = []
        # while arr:
        #     sorted_arr.append(heapq.heappop(arr))
        # return sorted_arr

    def swap(self, arr, i, j):
        """
        Swaps two elements in an array or list.

        :param arr: The array or list where the swap operation will be performed.
        :param i: The index of the first element to be swapped.
        :param j: The index of the second element to be swapped.
        """
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


if __name__ == "__main__":
    INPUT_FILE = "inputPS05.txt"
    OUTPUT_FILE = "outputPS05.txt"
    cabin_allotment = CabinAllotment(INPUT_FILE, OUTPUT_FILE)
    cabin_allotment.execute()
