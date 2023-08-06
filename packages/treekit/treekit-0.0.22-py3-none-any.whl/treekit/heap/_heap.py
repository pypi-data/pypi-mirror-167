# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: MIT


from typing import List, Union
from ..binarytree import binarytree


class heap(object):
    def __init__(self, array: List[Union[float, int]] = [], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.treetype = 'Heap'
        self.array = array.copy()
        if self.array:
          self.construct_max_heap(self.array)

    def heapify(self, array, array_size, subtree_root_index):
        # find the largest value index among (1) subtree root index, (2) left child index, (3) right child index
        largest_value_index = subtree_root_index
        left_child_index = 2*subtree_root_index + 1
        right_child_index = 2*subtree_root_index + 2
        if left_child_index < array_size and array[left_child_index] > array[largest_value_index]:
            largest_value_index = left_child_index
        if right_child_index < array_size and array[right_child_index] > array[largest_value_index]:
            largest_value_index = right_child_index
        # if one of the two children has larger value than the subtree root, swap that child with subtree root
        # so that the subtree root has the max. among the three nodes
        if largest_value_index != subtree_root_index:
            array[subtree_root_index], array[largest_value_index] = array[largest_value_index], array[subtree_root_index]
            self.heapify(array, array_size, largest_value_index) # continue to sift down the original value of subtree_root_index

    def construct_max_heap(self, array, array_size = None):
        if not array_size:
            array_size = len(array)
        last_non_leaf_node = (array_size // 2) - 1
        for subtree_root_index in range(last_non_leaf_node, -1, -1):
            self.heapify(array, array_size, subtree_root_index)
        # importantly, the array represents a level-order traversal of the tree (if we want to visualize the heap)

    def heapsort(self, array):
        self.construct_max_heap(array) # here, the array[0], will be the max element due to the array being a max heap now
        for array_size in range(len(array)-1, 0, -1):
            array[array_size], array[0] = array[0], array[array_size] # move the max. element, array[0], to the end of the array
            self.heapify(array, array_size, 0) # sift down the 0-th element to its appropriate index in the heap

    def show(self, filename: str = 'output.html'):
        if self.array:
          bt = binarytree(self.array)
          bt.show(filename=filename)