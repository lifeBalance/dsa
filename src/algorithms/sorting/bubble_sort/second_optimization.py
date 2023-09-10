def ascending_order(a, b):
    """
    Takes a list as an argument and returns True if the list is in ascending order, and False otherwise.
    """
    return a < b


def swap(lst, i):
    """
    Swap its two list item arguments.
    """
    lst[i], lst[i + 1] = lst[i + 1], lst[i]


def bubble_sort(lst, in_order, swap):
    """
    Sort a list, in place, in ascending order.
    """
    n = len(lst) - 1
    while n > 0:
        sorted = True
        i = 0
        while i < n:
            if not in_order(lst[i], lst[i + 1]):
                swap(lst, i)
                sorted = False
            i += 1
        if sorted:
            break
        n -= 1


# Let's try it!
list = [7, 4, 5, 6, 1, 2, 3]
bubble_sort(list, ascending_order, swap)
print(list)