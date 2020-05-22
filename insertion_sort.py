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

print('Time complexity:  O(n^2), Best: O(n)')
print('Space complexity: O(n)')

'''
The primary advantage of insertion sort over selection sort is that selection sort 
must always scan all remaining elements to find the absolute smallest element in the 
unsorted portion of the list, while insertion sort requires only a single comparison 
when the (k + 1)-st element is greater than the k-th element; when this is frequently 
true (such as if the input array is already sorted or partially sorted), insertion sort is 
distinctly more efficient compared to selection sort. 

- LESS COMPARISONS than Selection sort :)
- MORE WRITES than Selection sort :( . Will write O(n^2) times, whereas Selection sort O(n) times
'''