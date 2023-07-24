import pandas as pd

# Step 1: Read data from CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Step 2: Display the DataFrame
print("Original DataFrame:")
print(df)

# Step 3: Basic Data Manipulation

# Add a new column 'Grade' based on the 'Score' column
def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

df['Grade'] = df['Score'].apply(assign_grade)

# Calculate the average age of males and females separately
avg_age_male = df[df['Gender'] == 'M']['Age'].mean()
avg_age_female = df[df['Gender'] == 'F']['Age'].mean()

# Display the DataFrame after manipulation
print("\nDataFrame after manipulation:")
print(df)

# Step 4: Save the manipulated DataFrame to a new CSV file
df.to_csv('manipulated_data.csv', index=False)
