# This script defines functions to carry out natural merge sort using a linked list implementation

# Initialize empty list, set exchange and comparison counts to 0
empty = None
swaps = 0
comparisons = 0


class LinkedList(object):
    """
    Initializes a Linked List class for use in implementing the sort
    """
    __slots__ = "value", "next"

    def __init__(self, value, next=empty):
        self.value = value
        self.next = next

    def __le__(self, other):
        return self.value <= other.value

    def __lt__(self, other):
        return self.value < other.value


def reverse(head, size=-1):
    """
    Reverses the order of a subsection of a list that is already sorted descending
    :param head: the current head of the list
    :param size: size of the sublist to be reordered, default param of -1
    :return: new head value of the linked list
    """
    new_head = None
    while head:
        temp = head
        head = temp.next
        temp.next = new_head
        new_head = temp

        size -= 1

        if not size:
            tail = new_head
            while tail.next:
                tail = tail.next
            tail.next = head
            break

    return new_head


def find_next_stop(head):
    """
    Function to determine the next stopping point in the list through comparisons
    :param head: current head of the linked list
    :return: the head value, the head's index location in the list, the value following the head
    """
    # returns empty or head value if list size is 0 or 1
    if head is empty:
        return head, 0, empty
    next_node = head.next
    if next_node is empty:
        return head, 1, empty

    # if at least 2(+) values in list, continues through list
    size = 2
    global comparisons
    global swaps
    if head <= next_node:
        comparisons += 1
        # iterates through list checking if any values are smaller than the current value
        while next_node.next and next_node <= next_node.next:
            size += 1
            comparisons += 1
            next_node = next_node.next
        next_node = next_node.next
    else:    # if head > next value
        while next_node.next and next_node > next_node.next:
            size += 1
            comparisons += 1
            next_node = next_node.next
            swaps += 1
        next_node = next_node.next
        head = reverse(head, size)

    return head, size, next_node


def merge_sort(head):
    """
    Function to carry out the natural merge sort
    :param head: list to be sorted
    :return: the sorted list
    """
    global swaps
    global comparisons

    item1 = item2 = head
    item1_size = 0
    tail = empty

    while item2 is not empty:
        tail = empty
        item2, item2_size, next_item = find_next_stop(item2)
        new_size = item1_size + item2_size

        while item2_size > 0 or item1_size > 0:
            if item1_size == 0:
                new_tail, item2 = item2, item2.next
                item2_size -= 1
            elif item2_size == 0:
                new_tail, item1 = item1, item1.next
                item1_size -= 1
            elif item1 <= item2:
                new_tail, item1 = item1, item1.next
                item1_size -= 1
                swaps += 1
                comparisons += 1
            else:
                new_tail, item2 = item2, item2.next
                item2_size -= 1
                swaps += 1
                comparisons += 1

            if tail is empty:
                head = new_tail
            else:
                tail.next = new_tail
            tail = new_tail

        item1_size = new_size
        item2 = next_item
        item1 = head

    if tail is not empty:
        tail.next = empty

    return head


def make_list(initializer):
    """
    Function to initialize a linked list
    :param initializer: items in the list that need to be sorted
    :return: head value of the list
    """
    iteration = reversed(initializer)
    try:
        next_iter = next(iteration)
    except StopIteration:
        return empty
        # Empty list
    else:
        head = LinkedList(next_iter)
        for value in iteration:
            head = LinkedList(value, head)
        return head


def walk(head, size=-1):
    """
    Function to walk through the list one item at a time
    :param head: head value of list
    :param size: size of list
    :return: yields the head value
    """
    while head is not empty:
        if size:
            size -= 1
        else:
            break
        yield head.value
        head = head.next


def to_list(head, size=-1):
    """
    Returns the sorted list
    :param head: head value of list
    :param size: size of list
    :return: sorted list
    """
    return list(walk(head, size))
