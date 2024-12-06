import pandas as pd

# ADVENT OF CODE DAY 1 | PART 1 | ANSWER = 765748 ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Read the text file into a DataFrame
df = pd.read_csv(r'input.txt', delimiter=r'\s+', header=None, names=['Column1', 'Column2'])

# Sort each column
df = df.apply(sorted, axis=0)

# Find the distance between the two
df['Difference'] = (df['Column1'] - df['Column2']).abs()

# Sum the difference
total_difference = df['Difference'].sum()
# print(total_difference)



# ADVENT OF CODE DAY 1 | PART 2 | ANSWER = 27732508 |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Counting how many times each value is repeated 
df['Repeats'] = df['Column1'].apply(lambda x: (df['Column2'] == x).sum())

# Multiply each value in Column 1 by the number of repeats
df['SimularityScore'] = (df['Column1'] * df['Repeats'])

# Simularity Score
simscore = df['SimularityScore'].sum()
print(simscore)