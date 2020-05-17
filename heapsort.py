from typing import List


def heapsort(input : List[int]) -> List[int]:

    max_heap = build_heap(input)

    return max_heap

def bubble_up(value, index, list):
    pass

def bubble_down(value, index, list):
    #look at children
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    max_index = len(input)
    if left_index >= max_index:
        return list

    left_child = input[left_index]
    right_child = -1 if right_index >= max_index else input[right_index]

    print("Elem: " + str(value))
    print("Left child: " + str(left_child))
    print("Right child: " + str(right_child))
    elem = input[index]
    #compare to elem
    maximum = max(left_child, elem, right_child)

    #if not in order
    if maximum == elem:
        print("Element " + str(elem) + " is in the right position.")
        return list # The element is in the right position
    elif maximum == left_child:
        input[left_index] = elem
        input[index] = left_child
        print("Switching " + str(elem) + " with " + str(left_child))
        bubble_down(elem, left_index, input)
    elif maximum == right_child:
        input[right_index] = elem
        input[index] = right_child
        print("Switching " + str(elem) + " with " + str(right_child))
        bubble_down(elem, right_index, input)


def build_heap(input : List[int]) -> List[int]:

    i = 1
    max_index = len(input)
    middle_index = int(max_index/2)
    i = middle_index

    while i > -1:
        bubble_down(input[i], i, input)
        i -= 1

    return input

input = [10,6,7,5,15,17,12] #Not a max heap yet

print('Input: ' + str(input))
print(heapsort(input))