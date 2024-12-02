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

print(f"Total Distance: {total_distance}")

# Total Distance: 2164381

#####--- Part Two ---#####

# Step 5: Count occurrences of each number from List 1 in List 2
list_2_counts = df['List 2'].value_counts().to_dict()

# Create the Multiply column
df['Multiply'] = df['List 1'].apply(lambda x: x * list_2_counts.get(x, 0))

# Step 6: Calculate the similarity score (sum of Multiply column)
similarity_score = df['Multiply'].sum()

print(f"Similarity Score: {similarity_score}")

# Similarity Score: 20719933