import re

# Read the input string from the input.txt file
with open('input.txt', 'r') as file:
    input_string = file.read()

# Find all cases of mul(X,Y) where X and Y are 1-3 digit numbers
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, input_string)

# Perform the multiplications
multiples = [int(x) * int(y) for x, y in matches]

# Calculate the sum of all multiples
result_sum = sum(multiples)

print(f"The sum is: {result_sum}")
# The sum is: 187825547

#####--- Part Two ---#####


import re

# Read the input string from the input.txt file
with open('input.txt', 'r') as file:
    input_string = file.read()

# Define the patterns for mul, do, and don't instructions
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
control_pattern = r"(do\(\)|don't\(\))"

# Find all mul instructions and control instructions in the order they appear
matches = re.finditer(f"{mul_pattern}|{control_pattern}", input_string)

# Initialize variables
multiples = []
enabled = True  # Multiplications are enabled by default

# Process matches in order
for match in matches:
    if match.group(1) and match.group(2):  # It's a mul instruction
        if enabled:
            x, y = int(match.group(1)), int(match.group(2))
            multiples.append(x * y)
    elif match.group(3) == "do()":  # Enable future mul instructions
        enabled = True
    elif match.group(3) == "don't()":  # Disable future mul instructions
        enabled = False

# Calculate the sum of all enabled multiples
result_sum = sum(multiples)

print(f"The sum is: {result_sum}")

# The sum is: 85508223
