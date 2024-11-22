# Lab 4

This python package is designed to utilize five types of sorts to sort a collection of data in ascending order


* Pycharm IDE was used for running this package, information as follows:

PyCharm 2022.3.2 (Community Edition)
Build #PC-223.8617.48, built on January 24, 2023
Runtime version: 17.0.5+1-b653.25 x86_64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
macOS 13.2
GC: G1 Young Generation, G1 Old Generation
Memory: 1024M
Cores: 8
Metal Rendering is ON
Non-Bundled Plugins:
    com.leinardi.pycharm.pylint (0.14.0)

* A Macintosh operating system Ventura 13.2 was used.


## Running Lab4

1. Download and install python on your computer
2. Run the program in the terminal as a module: python -m Lab4_package <input_file> <output_file1> <output_file2>


### Lab4 Usage:

usage: python -m Lab4 [-h] input_file output_file1 output_file2

positional arguments:
  input_file                Input File Pathname
  output_file1              Output File1 Pathname
  output_file2              Output File2 Pathname

* make sure input file paths are correct to successfully run the program: ~/Lab4/Lab4_package/input_files/<input>

optional arguments:
  -h, --help  show this help message and exit


## Project Layout:

- Lab4: The parent folder holding all the project files
  - README: This guide the user is currently reading. Explains package usage
  - Lab4_package: The main module within the package
    - __init__.py: Used to show what functions, variables, classes, etc. are exposed when scripts import this module
    - __main__.py: The entrypoint to the program when ran as a program
    - file_formatting.py: Used to create the input files
    - runtime_metrics.py: Creates a class to measure runtime metrics
    - lab4.py: Defines functions to take input and output files to process as well as call to the sorting algorithms
    - merge_sort.py: Defines functions to sort an array via natural merge sort using a linked list implementation
    - quicksort1.py: Defines functions to sort an array via quicksort
    - quicksort2.py: Defines functions to sort an array via quicksort, using insertion sort on partitions of size <= 50
    - quicksort3.py: Defines functions to sort an array via quicksort, using insertion sort on partitions of size <= 100
    - quicksort4.py: Defines functions to sort an array via quicksort with a pivot selection of median of three
