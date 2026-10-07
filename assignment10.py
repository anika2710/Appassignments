import numpy as np

# 1. Create a one-dimensional array from 1 to 10
arr = np.arange(1, 11)
print("Original Array:", arr)

# 2. Perform slicing operations
print("First 5 elements:", arr[:5])
print("Last 3 elements:", arr[-3:])
print("Elements from index 2 to 7:", arr[2:8])

# 3. Compute statistical measures
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 4. Apply broadcasting to modify array elements
arr_modified = arr * 2   # Multiply each element by 2
print("Array after broadcasting (×2):", arr_modified)




