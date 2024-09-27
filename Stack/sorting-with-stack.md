# Sorting Algorithms Using Stack

## 1. Sorting a Stack (Using an Auxiliary Stack)

This algorithm sorts the elements of a stack in **ascending order** by using an additional (auxiliary) stack. It follows a simple process:

### Steps

1. Create an auxiliary stack.
2. Pop elements one by one from the original stack.
3. If the top of the auxiliary stack is smaller than the popped element, keep popping from the auxiliary stack and push them back to the original stack until the correct place is found.
4. Push the popped element into the auxiliary stack.
5. Repeat until the original stack is empty and the auxiliary stack contains the sorted elements.

**Time Complexity:** O(n²) We are using two stacks and each element may be moved multiple times.

### Example

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)

# Function to sort a stack using an auxiliary stack
def sort_stack(stack):
    aux_stack = Stack()

    # Process all elements in the original stack
    while not stack.is_empty():
        temp = stack.pop()

        # Move elements from aux_stack back to stack if they are greater than temp
        while not aux_stack.is_empty() and aux_stack.peek() > temp:
            stack.push(aux_stack.pop())

        # Push temp into aux_stack
        aux_stack.push(temp)

    # Transfer back sorted elements from aux_stack to the original stack
    while not aux_stack.is_empty():
        stack.push(aux_stack.pop())

# Example usage
stack = Stack()
stack.push(3)
stack.push(1)
stack.push(4)
stack.push(2)

print("Original stack:")
stack.display()

sort_stack(stack)

print("Sorted stack:")
stack.display()
```

## 2. Sorting an Array using Stack (Simulating Insertion Sort)

**Approach:**
We can simulate the Insertion Sort algorithm using a stack:

- Push elements from the array onto the stack one by one.
- For each element, pop elements from the stack and re-push them into the correct position to maintain the sorted order.

**Time Complexity:** O(n²), We are using single stack though we are using two for-loop.

```python
def insertion_sort_stack(arr):
    stack = []

    for num in arr:
        # Pop elements greater than current element and hold them in temporary stack
        temp_stack = []
        while stack and stack[-1] > num:
            temp_stack.append(stack.pop())

        # Push the current number into the correct position
        stack.append(num)

        # Push back the larger elements
        while temp_stack:
            stack.append(temp_stack.pop())

    # Copy back the sorted stack elements to the array
    for i in range(len(arr)):
        arr[i] = stack.pop()

# Example usage
arr = [3, 1, 4, 2]
print("Original array:", arr)

insertion_sort_stack(arr)
print("Sorted array:", arr)
```

## 3. Sorting an Array Using Two Stacks (Simulating Quick Sort)

You can implement `Quick Sort` using two stacks. Instead of recursive calls, stacks are used to store the low and high indices for sorting the sub-arrays. The stack simulates the call stack of the recursive quick sort.

**Steps:**

- Push the initial low and high indices of the array onto the stack.
- Pop the indices and perform the partitioning step.
- Push the indices of the left and right sub-arrays to the stack.
- Repeat until the stack is empty.

**Time Complexity:** O(n log n) (Average case)

```python
def quick_sort_stack(arr):
    # Initialize a stack
    stack = []

    # Push initial low and high indices
    stack.append((0, len(arr) - 1))

    # Iterate while stack is not empty
    while stack:
        low, high = stack.pop()

        if low < high:
            # Partition the array
            pivot_index = partition(arr, low, high)

            # Push sub-arrays indices to sort
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

# Partition function (same as quicksort partition)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
print("Original array:", arr)

quick_sort_stack(arr)
print("Sorted array:", arr)
```

## 4. Sorting Using Stack to Implement Merge Sort (Simulated Recursion)

**Approach**

- Merge Sort is a **divide and conquer** algorithm that recursively splits the array into two halves until each half has only one element, then merges them back in sorted order.
- Instead of using recursion, we can use a **stack** to simulate the recursion.

**Steps:**

1. Use a **stack** to simulate recursive calls for the **divide** phase.
2. Divide the array into halves until you have sub-arrays of size 1.
3. Use the stack to handle the **merge** step and combine the sub-arrays back into a sorted order.

**Pseudo code:**

1. Push the left and right bounds of the array into the stack for the first call.
2. Pop the bounds and continue dividing until you reach the base case (single element arrays).
3. Once the base case is reached, start merging the divided sections back together in sorted order.

**Time Complexity:** O(n log n), similar to the recursive version of Merge Sort.

### Example (Simulated Recursion)

Unfortunately, Merge Sort's stack-based simulation can be tricky and is best achieved through simulating recursive calls. You would divide the array and simulate the merging process using the stack to hold ranges.

The code below simulates the division using a stack, then merges the divided subarrays.

```python
def merge(arr, l, m, r):
    # Create temporary arrays
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:m+1]
    R = arr[m+1:r+1]

    # Merge the temporary arrays back into arr[l..r]
    i = 0  # Initial index of the first sub-array
    j = 0  # Initial index of the second sub-array
    k = l  # Initial index of merged sub-array

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[]
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[]
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort_stack(arr):
    # Stack will store the left and right indices
    stack = [(0, len(arr) - 1)]

    # Simulate recursion using stack
    while stack:
        l, r = stack.pop()
        if l < r:
            m = (l + r) // 2
            # First push right half then left half
            stack.append((m + 1, r))  # Push right half
            stack.append((l, m))      # Push left half
            merge(arr, l, m, r)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)

merge_sort_stack(arr)
print("Sorted array:", arr)
```

## 5. Sorting a Stack without Extra Space (Recursive Approach)

**Approach**

- This algorithm sorts a stack without using any additional space (i.e., no auxiliary stack or array), just the stack itself.
- The approach uses recursion to remove elements from the stack one by one, and then inserts them back in the correct order.

**Steps:**

- Recursively pop elements from the stack until the stack is empty.
- Once the stack is empty, insert the popped elements back into the stack in the sorted order.
- Use a helper function sorted_insert to place each element in the correct position in the stack.

**Time Complexity:** O(n²) – Since each element needs to be inserted in sorted order, each insertion takes O(n) time.

```python
# Helper function to insert an element into a sorted stack
def sorted_insert(stack, element):
    # Base case: If the stack is empty or the element is greater than the top element
    if not stack or stack[-1] <= element:
        stack.append(element)
        return

    # Pop the top element
    temp = stack.pop()

    # Recursively insert the element into the sorted stack
    sorted_insert(stack, element)

    # Push the top element back
    stack.append(temp)

# Function to sort the stack using recursion
def sort_stack_recursive(stack):
    # Base case: If the stack is empty
    if not stack:
        return

    # Pop the top element
    temp = stack.pop()

    # Recursively sort the remaining stack
    sort_stack_recursive(stack)

    # Insert the top element back in sorted order
    sorted_insert(stack, temp)

# Example usage
stack = [3, 1, 4, 2]
print("Original stack:", stack)

sort_stack_recursive(stack)
print("Sorted stack:", stack)
```
