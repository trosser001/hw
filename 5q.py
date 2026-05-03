#!/usr/local/bin/python3
import sys, re

files = open(sys.argv[1])
file = files.read()

num = r"[0-9]+"
nums = re.findall(num, file)
nums = [int(i) for i in nums]
print(max(nums))

# print(max_list)
