# Python script: file_processing.py

# Open the input file and read all lines
with open("input.txt", "r") as infile:
    lines = infile.readlines()

# Count total number of lines
total_lines = len(lines)
print("Total number of lines in input file:", total_lines)

# Extract the first two lines
first_two = lines[:2]

print("\nFirst two lines are:")
for line in first_two:
    print(line, end="")

# Write the extracted lines into a new file
with open("output.txt", "w") as outfile:
    outfile.writelines(first_two)

print("\n\nThe first two lines have been saved into output.txt")
