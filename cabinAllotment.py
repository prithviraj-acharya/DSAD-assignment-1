"""
A class to manage cabin allotment based on booking IDs.

Author: Group 13
Year: 2024

"""

import sys


class CabinAllotment:

    def __init__(self, input_file, output_file):
        """
        Initializes the CabinAllotment class with input and output file paths.

        :param input_file: Path to the input file containing booking IDs.
        :param output_file: Path to the output file for writing the results.

        """
        self.input_file = input_file
        self.output_file = output_file
        self.bookingIds = []

    def process_booking_ids(self, ids_str):
        """
        Processes a string of comma-separated booking IDs, ensuring they are unique positive integers.

        :param ids_str: A string of comma-separated booking IDs.
        :return: A list of unique, positive integer booking IDs.
        """
        booking_ids = []
        try:
            for id_str in ids_str.split(","):
                id_int = int(id_str.strip())
                if id_int <= 0:
                    raise ValueError("ID must be a positive integer.")
                if id_int not in booking_ids:
                    booking_ids.append(id_int)
        except ValueError as e:
            print(f"Error: ID must be a positive integer.")
            sys.exit(1)
        return booking_ids

    def read_input(self):
        """
        Reads booking IDs from the input file and returns an array of unique IDs.
        """
        try:
            with open(self.input_file, "r") as f:
                content = f.read().strip()
                if not content:
                    raise ValueError("The input file is empty.")
                return self.process_booking_ids(content)
        except FileNotFoundError:
            print(f"Error: File '{self.input_file}' not found.")
            sys.exit(1)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

    def get_booking_ids(self):
        """
        Takes user input as a comma-separated string of booking IDs.
        """
        input_str = input("Enter booking IDs, separated by commas: ")
        return self.process_booking_ids(input_str)

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

    def split_at_median(self):
        """
        Splits the booking IDs at the median value.

        This method calculates the median of the booking IDs, then splits the list of booking IDs into two parts:
        one part containing IDs up to and including the median, and the other part containing the remaining IDs.
        The original list of booking IDs is updated to only contain the IDs after the median.

        Returns:
            list: The list of booking IDs up to and including the median.
        """
        median = self.calculate_median(self.bookingIds)
        median_index = self.bookingIds.index(median)
        up_to_median = self.bookingIds[: median_index + 1]
        self.bookingIds = self.bookingIds[median_index + 1 :]
        return up_to_median

    def heapify(self, arr, length, parentIdx):
        """
        Ensures the subtree rooted at parentIdx in the array 'arr' satisfies the heap property.

        This function compares the parent node with its left and right children and swaps the parent with the larger of the two children if the parent is not the largest. It recursively ensures that the subtree rooted at the index where the swap occurred satisfies the heap property.

        Parameters:
            arr (list): The list representation of the heap.
            length (int): The number of elements in the heap that need to be heapified.
            parentIdx (int): The index of the parent node in the array that might violate the heap property.

        Returns:
            None: The function modifies the array in place to ensure it satisfies the heap property.
        """
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

    def heap_sort(
        self,
    ):
        """
        Sorts the booking IDs using heap sort algorithm and returns the sorted list.

        :return: A list of sorted booking IDs.
        """
        arr = self.bookingIds
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

    def swap(self, arr, i, j):
        """
        Swaps two elements in an array or list using tuple unpacking for a more Pythonic approach.

        :param arr: The array or list where the swap operation will be performed.
        :param i: The index of the first element to be swapped.
        :param j: The index of the second element to be swapped.
        """
        arr[i], arr[j] = arr[j], arr[i]

    def categorize_rooms(self):
        """
        Categorizes booking IDs into suite, balcony, outside rooms, ocean view, and interior rooms based on the median.
        """
        room_categories = ["Suite", "Balcony", "Outside", "Ocean view", "Interior"]
        room_allocations = {}

        for category in room_categories:
            try:
                if category == "Suite":
                    self.bookingIds.extend(self.read_input())
                else:
                    self.bookingIds.extend(self.get_booking_ids())
                self.heap_sort()
                room_allocations[category] = self.split_at_median()
            except Exception as e:
                print(f"An error occurred while processing {category} rooms: {e}")
                return

        # Output to file
        try:
            with open(self.output_file, "w") as f:
                for category, ids in room_allocations.items():
                    if category in ["Suite", "Outside", "Ocean view"]:
                        ids_str = ", ".join(
                            map(str, ids)
                        )  # Convert ids to strings and join with commas
                        f.write(f"{category} rooms were allocated to Ids: {ids_str}\n")
        except Exception as e:
            print(f"An error occurred while writing to file: {e}")


if __name__ == "__main__":
    INPUT_FILE = "inputPS05.txt"
    OUTPUT_FILE = "outputPS05.txt"
    cabin_allotment = CabinAllotment(INPUT_FILE, OUTPUT_FILE)
    cabin_allotment.categorize_rooms()
