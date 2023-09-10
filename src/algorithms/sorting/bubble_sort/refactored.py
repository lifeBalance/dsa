def ascending_order(a, b):
    """
    Takes a list as an argument and returns True if the list is in ascending order; False otherwise.
    """
    return a < b

def swap(lst, i):
    """
    Swap its two list item arguments.
    """
    lst[i], lst[i+1] = lst[i+1], lst[i]

def bubble_sort(lst, in_order, swap):
    """
    Sort a list, in place, in ascending order.
    """
    n = len(lst)
    while n > 0:
        i = 0
        while i < n - 1:
            if not in_order(lst[i], lst[i+1]):
                swap(lst, i)
            i += 1
        n -= 1

# Let's use the algorithm!
list = [7, 4, 5, 6, 1, 2, 3]
bubble_sort(list, ascending_order, swap)
print(list)