import pandas as pd

# Step 1: Read the input CSV file
input_file = "input.csv"
df = pd.read_csv(input_file)

# Step 2: Sort numbers in both columns in increasing order
df['List 1'] = sorted(df['List 1'])
df['List 2'] = sorted(df['List 2'])

# Step 3: Create a 3rd column 'Difference' with absolute value differences
df['Difference'] = abs(df['List 1'] - df['List 2'])

# Step 4: Calculate the sum of numbers in 'Difference' (Total Distance)
total_distance = df['Difference'].sum()

# Output the total distance
print(f"Total Distance: {total_distance}")


#####--- Part Two ---#####