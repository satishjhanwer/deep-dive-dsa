# Sorting Algorithms Using Queues

## 1. Radix Sort Using Queue

### Overview

- **Radix Sort** uses a queue to distribute elements into buckets based on each digit (starting from the least significant digit to the most significant).
- It processes numbers digit by digit, using **queues** to group numbers based on their current digit position.

### Steps

1. Initialize 10 queues (for digits 0-9).
2. For each digit position (units, tens, hundreds, etc.):
   - **Enqueue** each number into the respective queue based on the current digit.
   - **Dequeue** all elements back into the list from the queues.
3. Repeat this process for each digit until the largest number is processed.

### Time Complexity

- **O(d\*(n + b))**, where:
  - `n` is the number of elements.
  - `b` is the base (10 for decimal numbers).
  - `d` is the number of digits in the largest number.

### Example Implementation

```python
from collections import deque

def get_digit(number, digit_place):
    return (number // digit_place) % 10

def radix_sort_queue(arr):
    max_num = max(arr)
    digit_place = 1  # Starting with the units place

    # Initialize 10 queues for each digit (0-9)
    queues = [deque() for _ in range(10)]

    while max_num // digit_place > 0:
        # Place elements into the respective queue based on the current digit
        for num in arr:
            digit = get_digit(num, digit_place)
            queues[digit].append(num)

        # Collect elements back from the queues
        index = 0
        for queue in queues:
            while queue:
                arr[index] = queue.popleft()
                index += 1

        # Move to the next digit place (tens, hundreds, etc.)
        digit_place *= 10

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", arr)
radix_sort_queue(arr)
print("Sorted array:", arr)
```
