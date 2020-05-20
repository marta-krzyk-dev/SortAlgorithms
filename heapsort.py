from typing import List


def heapsort(input: List[int]) -> List[int]:
    max_heap = build_heap(input)

    count = len(max_heap)

    while count > 0:
        # swap max with the next number from back of the list
        max = max_heap[0]
        max_heap[0] = max_heap[count-1]
        max_heap[count-1] = max

        bubble_down(0, max_heap, count-1)

        count -= 1

    return max_heap


def extract_max(heap):
    if len(heap) < 1:
        return int('inf')
    elif len(heap) == 1:
        return heap[0]

    current_max = heap[0]
    bubble_down(0, heap)

    return current_max


def bubble_down(index, input_arr, max_index=None):

    # Find children's indexes
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    # print(f"I got {index} index and: {input_arr}")
    max_index = len(input_arr) if max_index == None else max_index
    if left_index >= max_index:
        # print(f"Node has no children. Returning {input_arr}")
        return input_arr  # The node has no children

    left_child = input_arr[left_index]
    right_child = float('-inf') if right_index >= max_index else input_arr[right_index]

    elem = input_arr[index]
    # print("Elem: " + str(elem))
    # print("Left child: " + str(left_child))
    # print("Right child: " + str(right_child))

    # compare to current element
    maximum = max(left_child, elem, right_child)

    if maximum == elem:
        # print("Element " + str(elem) + " is in the right position.")
        return input_arr  # The element is in the right position
    elif maximum == left_child:
        input_arr[left_index] = elem
        input_arr[index] = left_child
        # print("Switching " + str(elem) + " with " + str(left_child))
        bubble_down(left_index, input_arr, max_index)
    elif maximum == right_child:
        input_arr[right_index] = elem
        input_arr[index] = right_child
        # print("Switching " + str(elem) + " with " + str(right_child))
        bubble_down(right_index, input_arr, max_index)


def build_heap(input_array):

    i = int(len(input_array) / 2) # Set i to middle index

    while i > -1:
        bubble_down(i, input_array)
        i -= 1

    print("Built heap: " + str(input_array))
    return input_array


array_unsorted = [10, 6, 7, 5, 15, 17, 12]  # Not a max heap yet

print('Input: ' + str(array_unsorted))
print(f"Sorted: {heapsort(array_unsorted)}")
