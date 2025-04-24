import numpy as np

arr = np.array(["ABCD", "PQRS", "WXYZ", "KLMN"])

centered = np.char.center(arr, 15, fillchar='_')
left_justified = np.char.ljust(arr, 15, fillchar='_')
right_justified = np.char.rjust(arr, 15, fillchar='_')

print("Original Array:")
print(arr)

print("\nCentered Strings:")
print(centered)

print("\nLeft-Justified Strings:")
print(left_justified)

print("\nRight-Justified Strings:")
print(right_justified)