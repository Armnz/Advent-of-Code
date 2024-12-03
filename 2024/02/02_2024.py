import pandas as pd

# Read the input CSV file
input_file = "input.csv"
df = pd.read_csv(input_file, header=None)


# Function to check if a report is safe
def is_safe_report(row):
    # Remove NaN values if rows have unequal lengths
    numbers = row.dropna().to_list()
    if len(numbers) < 2:
        return "Unsafe"  # Less than 2 numbers can't satisfy the conditions

    differences = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]

    # Check if all differences are either increasing or decreasing
    increasing = all(diff > 0 for diff in differences)
    decreasing = all(diff < 0 for diff in differences)

    # Check if all differences are between 1 and 3 (inclusive)
    within_range = all(1 <= abs(diff) <= 3 for diff in differences)

    # Both conditions must be true
    if (increasing or decreasing) and within_range:
        return "Safe"
    else:
        return "Unsafe"

# Apply the safety check to each row
df['Report Status'] = df.apply(is_safe_report, axis=1)

# Count the number of safe reports
safe_reports_count = (df['Report Status'] == "Safe").sum()

# Output the number of safe reports
print(f"Number of Safe Reports: {safe_reports_count}")

# Number of Safe Reports: 479

#####--- Part Two ---#####

import pandas as pd

# Read the input CSV file
input_file = "input.csv"
df = pd.read_csv(input_file, header=None)

# Preprocess: Convert all values to numeric, coercing errors to NaN
df = df.apply(pd.to_numeric, errors='coerce')


# Function to check if a report is safe
def is_safe_report(row):
    # Remove NaN values to focus on actual numbers
    numbers = row.dropna().to_list()
    if len(numbers) < 2:
        return False  # Less than 2 numbers can't satisfy the conditions

    differences = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]

    # Check if all differences are either increasing or decreasing
    increasing = all(diff > 0 for diff in differences)
    decreasing = all(diff < 0 for diff in differences)

    # Check if all differences are between 1 and 3 (inclusive)
    within_range = all(1 <= abs(diff) <= 3 for diff in differences)

    # Both conditions must be true
    return (increasing or decreasing) and within_range


# Function to check if removing one number makes the report safe
def apply_problem_dampener(row):
    numbers = row.dropna().to_list()
    if len(numbers) < 3:  # Removing one number must leave at least two
        return "Unsafe"

    # Try removing each number
    for i in range(len(numbers)):
        modified_numbers = numbers[:i] + numbers[i + 1:]
        if is_safe_report(pd.Series(modified_numbers)):
            return "Safe"

    return "Unsafe"


# Apply the Problem Dampener to each row
df['Report Status with Dampener'] = df.apply(apply_problem_dampener, axis=1)

# Count the number of safe reports with the dampener applied
safe_reports_with_dampener = (df['Report Status with Dampener'] == "Safe").sum()
print(f"Number of Safe Reports (with Problem Dampener): {safe_reports_with_dampener}")
