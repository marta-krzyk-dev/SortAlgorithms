def InsertionSort(array):  # Space complexity: O(1)

    for i, elem in enumerate(array):  # O(n)
        prev_index = i - 1

        while prev_index > -1 and array[prev_index] > array[i]:
            temp = array[i]
            array[i] = array[prev_index]
            array[prev_index] = temp

            i -= 1
            prev_index -= 1

        print(f"Iteration {i + 1}  {array}")

    return array


def swap(left_index, right_index, array):
    while left_index > -1:
        if array[left_index] > array[right_index]:
            temp = array[right_index]
            array[right_index] = array[left_index]
            array[left_index] = temp

            right_index -= 1
            left_index -= 1


input = [2, 8, 5, 3, 9, 4]

print('Input:  ' + str(input))
print('Result: ' + str(InsertionSort(input)))

print('Time complexity:  O(n^2)')
print('Space complexity: O(n)')
