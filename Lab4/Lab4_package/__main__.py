# This module is used to process command line arguments and launch the program
from pathlib import Path
import argparse
from lab4 import process_files
from sys import stderr


# Create the parser
arg_parser = argparse.ArgumentParser()

# Add an argument to the parser
arg_parser.add_argument("input_file", type=str, help="Input File Pathname")
arg_parser.add_argument("output_file", type=str, help="Output File Pathname")
arg_parser.add_argument("output_csv", type=str, help="Output CSV file pathname")

# Parse the argument
args = arg_parser.parse_args()

# pathlib.Path
in_path = Path(args.input_file)
out_path = Path(args.output_file)
out_csv = Path(args.output_csv)


# Raises error if the input file's path or name is incorrect
try:
    with in_path.open('r') as input_file, out_path.open('a') as output_file, out_csv.open('a') as out_csv:
        process_files(input_file, output_file, out_csv)
except FileNotFoundError:
    print(f'FILE NAME "{in_path}" NOT FOUND. CHECK INPUT FILE NAME OR PATH.', file=stderr)
