def SelectionSortWithSwapping(array): # Space complexity: O(1)

    for i, elem in enumerate(array): # O(n)

         min_index = i
         min = elem

         for j, elem2 in enumerate(array[i:]):
            if elem2 < elem:
                min = elem2
                min_index = j + i

         if min_index != i:
             print(f"swap {elem} at {i} with {min} from {min_index}")
             array[min_index] = elem
             array[i] = min

         print(f"Iteration {i+1}  {array}")

    return array

def SelectionSort(array): # O(n^2)

    sorted = []
    elem_count = len(array)
    i = 0

    while i < elem_count: # O(n)
        min, min_index = FindMin(array)
        sorted.append(min)
        del array[min_index]
        print(array)
        i += 1

    return sorted

def FindMin(array):

    min = array[0]          # O(1)
    min_index = 0            # O(1)

    for i, elem in enumerate(array):  # (n-1) + (n-2) + (n-3) + ... 1
        if elem < min:
            min = elem
            min_index = i

    print('Found min ' + str(min) + ' at ' + str(min_index))
    return min, min_index

input = [10,6,7,5,15,17,12]

print('Input:  ' + str(input))
print('Result: ' + str(SelectionSortWithSwapping(input)))

print('Time complexity:  O(n^2)')
print('Space complexity: O(n)')
