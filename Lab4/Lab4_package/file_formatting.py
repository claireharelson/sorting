# Script to write input files in correct format
# Manually updated file names and number ranges each time
import random

# Code to create randomized files
input_ran = open('input_files/ran500.txt', 'w')

nums = []

for i in range(1, 501):
    nums.append(i)

random.shuffle(nums)

for item in nums:
    input_ran.write(f'{item}\n')

input_ran.close()


# Code to create ascending files
input_asc = open('input_files/asc500.txt', 'w')

nums2 = []

for i in range(1, 501):
    nums2.append(i)

for item in nums2:
    input_asc.write(f'{item}\n')

input_asc.close()


# Code to create reverse order files
input_rev = open('input_files/rev500.txt', 'w')

nums3 = []

for i in range(500, 0, -1):
    nums3.append(i)

for item in nums3:
    input_rev.write(f'{item}\n')

input_rev.close()

