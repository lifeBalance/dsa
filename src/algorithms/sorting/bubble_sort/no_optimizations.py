def bubble_sort(arr):
    """
    Sort a list, in place, in ascending order.
    """
    n = len(arr)
    while n > 0:
        i = 0
        while i < n - 1:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 1
        n -= 1

# Let's use the algorithm!
list = [7, 4, 5, 6, 1, 2, 3]
bubble_sort(list)
print(list)