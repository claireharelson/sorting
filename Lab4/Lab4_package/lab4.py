# This script takes input and output files in to process
from sys import stderr
from time import time_ns
from typing import TextIO

from runtime_metrics import RuntimeMetric
import merge_sort
import quicksort1
import quicksort2
import quicksort3
import quicksort4


def merge_sort_list(values: list) -> (list, RuntimeMetric, int, int):
    """
    Calls to the merge sort function to sort an unsorted list
    :param values: the unsorted list
    :return: metrics on algorithm performance, the sorted list, and number of swaps and comparisons
    """
    start_time = time_ns()
    head = merge_sort.make_list(values)
    assert merge_sort.to_list(head) == values
    head = merge_sort.merge_sort(head)
    assert merge_sort.to_list(head) == sorted(values)
    end_time = time_ns()
    metric = RuntimeMetric(len(values), end_time - start_time)
    merge_swaps = merge_sort.swaps
    merge_comparisons = merge_sort.comparisons

    return merge_sort.to_list(head), metric, merge_swaps, merge_comparisons


def quicksort_list1(values: list) -> (list, RuntimeMetric, int, int):
    """
    Calls to the quicksort function to sort an unsorted list
    :param values: the unsorted list
    :return: metrics on algorithm performance, the sorted list, and number of swaps and comparisons
    """
    start_time = time_ns()
    sorted_list = quicksort1.quick_sort(values, len(values) - 1)
    end_time = time_ns()
    metric = RuntimeMetric(len(values), end_time - start_time)
    quick_swaps = quicksort1.swaps
    quick_comparisons = quicksort1.comparisons

    return sorted_list, metric, quick_swaps, quick_comparisons


def quicksort_list2(values: list) -> (list, RuntimeMetric, int, int):
    """
    Calls to the quicksort function to sort an unsorted list
    :param values: the unsorted list
    :return: metrics on algorithm performance, the sorted list, and number of swaps and comparisons
    """
    start_time = time_ns()
    sorted_list = quicksort2.hybrid_sort(values, len(values) - 1)
    end_time = time_ns()
    metric = RuntimeMetric(len(values), end_time - start_time)
    quick_swaps = quicksort2.swaps
    quick_comparisons = quicksort2.comparisons

    return sorted_list, metric, quick_swaps, quick_comparisons


def quicksort_list3(values: list) -> (list, RuntimeMetric, int, int):
    """
    Calls to the quicksort function to sort an unsorted list
    :param values: the unsorted list
    :return: metrics on algorithm performance, the sorted list, and number of swaps and comparisons
    """
    start_time = time_ns()
    sorted_list = quicksort3.hybrid_sort(values, len(values) - 1)
    end_time = time_ns()
    metric = RuntimeMetric(len(values), end_time - start_time)
    quick_swaps = quicksort3.swaps
    quick_comparisons = quicksort3.comparisons

    return sorted_list, metric, quick_swaps, quick_comparisons


def quicksort_list4(values: list) -> (list, RuntimeMetric, int, int):
    """
    Calls to the quicksort function to sort an unsorted list
    :param values: the unsorted list
    :return: metrics on algorithm performance, the sorted list, and number of swaps and comparisons
    """
    start_time = time_ns()
    sorted_list = quicksort4.quick_sort(values, len(values) - 1)
    end_time = time_ns()
    metric = RuntimeMetric(len(values), end_time - start_time)
    quick_swaps = quicksort4.swaps
    quick_comparisons = quicksort4.comparisons

    return sorted_list, metric, quick_swaps, quick_comparisons


def process_files(input_file: TextIO, output_file: TextIO, output_csv: TextIO) -> None:
    """
    Reads integer values from an input file into a list, sorts the values, then writes them to an output file
    :param output_csv: an opened text file set to write mode
    :param input_file: an opened text file set to read mode
    :param output_file: an opened text file set to write mode
    """
    next_line = input_file.readline()
    list_to_merge_sort = []
    list_to_quicksort1 = []
    list_to_quicksort2 = []
    list_to_quicksort3 = []
    list_to_quicksort4 = []

    while next_line is not None and next_line != "":
        try:
            value = int(next_line)
            list_to_merge_sort.append(value)
            list_to_quicksort1.append(value)
            list_to_quicksort2.append(value)
            list_to_quicksort3.append(value)
            list_to_quicksort4.append(value)
        except ValueError:
            print(f'Error parsing {next_line} for integer value', file=stderr)
            continue
        finally:
            next_line = input_file.readline()

    # Calling to the merge sort and quick sort functions for the five copies of each list
    merge_sorted_list, merge_runtime_metric, merge_swaps, merge_comparisons = merge_sort_list(list_to_merge_sort)
    final_merge = merge_sorted_list

    quicksorted_list1, quick1_runtime_metric, quick1_swaps, quick1_comparisons = quicksort_list1(list_to_quicksort1)
    final_quick1 = quicksorted_list1

    quicksorted_list2, quick2_runtime_metric, quick2_swaps, quick2_comparisons = quicksort_list2(list_to_quicksort2)
    final_quick2 = quicksorted_list2

    quicksorted_list3, quick3_runtime_metric, quick3_swaps, quick3_comparisons = quicksort_list3(list_to_quicksort3)
    final_quick3 = quicksorted_list3

    quicksorted_list4, quick4_runtime_metric, quick4_swaps, quick4_comparisons = quicksort_list4(list_to_quicksort4)
    final_quick4 = quicksorted_list4

    # writing results of merge sort
    if len(list_to_merge_sort) == 50:
        output_file.write(f'\nMerge sort data for file of size 50:\nThe sorted list: {final_merge}\n')
        output_file.write(f'Number of comparisons: {merge_comparisons}\nNumber of swaps: {merge_swaps}\n')
        output_file.write(
            f"File of size {len(list_to_merge_sort)} took {merge_runtime_metric.get_runtime()}ns to sort\n")
        output_csv.write(f'merge sort,{input_file},{len(list_to_merge_sort)},{merge_comparisons},{merge_swaps}\n')
    else:
        output_csv.write(f'merge sort,{input_file},{len(list_to_merge_sort)},{merge_comparisons},{merge_swaps}\n')

    # writing results of quicksort1
    if len(list_to_quicksort1) == 50:
        output_file.write(f'\nQuick sort type 1 data for file size of 50:\nThe sorted list: {final_quick1}\n')
        output_file.write(f'Number of comparisons: {quick1_comparisons}\nNumber of swaps: {quick1_swaps}\n')
        output_file.write(
            f'File of size {len(list_to_quicksort1)} took {quick1_runtime_metric.get_runtime()}ns to sort\n')
        output_csv.write(f'quick sort1,{input_file},{len(list_to_quicksort1)},{quick1_comparisons},{quick1_swaps}\n')
    else:
        output_csv.write(f'quick sort1,{input_file},{len(list_to_quicksort1)},{quick1_comparisons},{quick1_swaps}\n')

    # writing results of quicksort2
    if len(list_to_quicksort2) == 50:
        output_file.write(f'\nQuick sort type 2 data for file size of 50:\nThe sorted list: {final_quick2}\n')
        output_file.write(f'Number of comparisons: {quick2_comparisons}\nNumber of swaps: {quick2_swaps}\n')
        output_file.write(
            f'File of size {len(list_to_quicksort2)} took {quick2_runtime_metric.get_runtime()}ns to sort\n')
        output_csv.write(f'quick sort2,{input_file},{len(list_to_quicksort2)},{quick2_comparisons},{quick2_swaps}\n')
    else:
        output_csv.write(f'quick sort2,{input_file},{len(list_to_quicksort2)},{quick2_comparisons},{quick2_swaps}\n')

    # writing results of quicksort3
    if len(list_to_quicksort3) == 50:
        output_file.write(f'\nQuick sort type 3 data for file size of 50:\nThe sorted list: {final_quick3}\n')
        output_file.write(f'Number of comparisons: {quick3_comparisons}\nNumber of swaps: {quick3_swaps}\n')
        output_file.write(
            f'File of size {len(list_to_quicksort3)} took {quick3_runtime_metric.get_runtime()}ns to sort\n')
        output_csv.write(f'quick sort3,{input_file},{len(list_to_quicksort3)},{quick3_comparisons},{quick3_swaps}\n')
    else:
        output_csv.write(f'quick sort3,{input_file},{len(list_to_quicksort3)},{quick3_comparisons},{quick3_swaps}\n')

    # writing results of quicksort4
    if len(list_to_quicksort4) == 50:
        output_file.write(f'\nQuick sort type 4 data for file size of 50:\nThe sorted list: {final_quick4}\n')
        output_file.write(f'Number of comparisons: {quick4_comparisons}\nNumber of swaps: {quick4_swaps}\n')
        output_file.write(
            f'File of size {len(list_to_quicksort4)} took {quick4_runtime_metric.get_runtime()}ns to sort\n')
        output_csv.write(f'quick sort4,{input_file},{len(list_to_quicksort4)},{quick4_comparisons},{quick4_swaps}\n')
    else:
        output_csv.write(f'quick sort4,{input_file},{len(list_to_quicksort4)},{quick4_comparisons},{quick4_swaps}\n')

