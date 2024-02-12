#Importing the necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading the csv as a dataframe
data = pd.read_csv('Popular_Baby_Names.csv')
print(data)

#identify the data types
print(data.dtypes)

#check for null values in the dataset
null = data.isnull()
print(null)

any_null = null.any().any()
print(any_null)

#capitalise every row and column in the dataframe
#data_cap = data.applymap(lambda x: x.capitalize() if isinstance(x, str) else x)

string_columns = data.select_dtypes(include='object').columns
data[string_columns] = data[string_columns].apply(lambda x: x.str.capitalize() if x.dtype == 'object' else x)

print(data)

data['Ethnicity'] = data['Ethnicity'].replace(
    {
        'Black non hisp'            : 'Black non hispanic',
        'White non hisp'            : 'White non hispanic',
        'Asian and paci'            : 'Asian and pacific islanders',
        'Asian and pacific islander': 'Asian and pacific islanders'
    }
)

#remove duplicates
# Remove duplicate rows based on all columns
datad = data.drop_duplicates()
print(datad)

# Save the DataFrame without duplicates to a CSV file
datad.to_csv('df_no_duplicates.csv', index=False)

# Assuming 'datad' is the DataFrame containing the dataset
summary_stats = datad.describe()

# Display summary statistics
print(summary_stats)

# Count the number of occurrences for each gender
gender_counts = datad['Gender'].value_counts()

# Display the counts
print(gender_counts)

# Filter only numeric columns
numeric_columns = datad.select_dtypes(include='number')
print(numeric_columns)

column = numeric_columns.columns[0]
plt.figure(figsize=(6, 4))
plt.boxplot(datad[column].dropna())
plt.title(f'Boxplot of {column}')
plt.xlabel(column)
plt.ylabel('Value')
plt.tight_layout()
plt.show()

#

plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='Year of Birth', hue='Ethnicity')
plt.title('Count Plot of Year of Birth by Ethnicity')
plt.xlabel('Year of Birth')
plt.ylabel('Count')
plt.legend(title='Ethnicity', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Group names alphabetically and calculate counts for each gender
datad['FirstNameGroup'] = datad["Child's First Name"].str[0]  # Extract first letter of the names
grouped = datad.groupby(['FirstNameGroup', 'Gender']).size().unstack().fillna(0)

# Plotting
grouped.plot(kind='bar', stacked=True)
plt.title('Count of Names Grouped Alphabetically by Gender')
plt.xlabel('Alphabets')
plt.ylabel('Count')
plt.legend(title='Gender')
plt.show()

