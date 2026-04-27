# Step 1: Import NumPy 
import numpy as np 

# Step 2: Create a 1D array representing years of experience 
years_exp = np.array([1, 3, 5, 7, 10, 30, 40]) 
print("Years of Experience:", years_exp) 

# Step 3: Create a 2D array representing sample salaries (in thousands) 
salaries = np.array([[50, 60, 70], [80, 90, 100], [101, 102, 103]])     
print("Salary Matrix:\n", salaries) 

# Step 4: Create an array of zeros and ones for placeholder analysis 
zeros_array = np.zeros((2, 2))  # 2x2 zeros 
ones_array = np.ones((2, 3))    # 2x3 ones 
identify_matrix = np.eye(3) 

print("Zeros Array:\n", zeros_array) 
print("Ones Array:\n", ones_array)
print("Identity Matrix:\n", identify_matrix)



# Step 1: Element-wise addition 
exp_plus_5 = years_exp + 5  
print("Years + 5:", exp_plus_5) 

# Step 2: Element-wise multiplication 
exp_times_2 = years_exp * 2  
print("Years * 2:", exp_times_2) 

# Step 3: Dot product 
sample1 = np.array([1, 2, 3]) 
sample2 = np.array([4, 5, 6]) 
dot_result = np.dot(sample1, sample2) 
print("Dot Product:", dot_result)

print("Years - 1:", years_exp - 1)
print("Years / 3:", years_exp / 3)
print("Exp:", np.exp(years_exp))
print("Log:", np.log(years_exp))



# Step 1: Access individual element 
print("First year of experience:", years_exp[0]) 

# Step 2: Slice arrays 
print("First two salaries:", salaries[0, :2])  

# Step 3: Access all rows for a specific column 
print("Second column salaries:", salaries[:, 1]) 

# Step 4: Negative indexing 
print("Last year of experience:", years_exp[-1]) 

# Reverse array
print("Reversed years:", years_exp[::-1])

# Slice 2D subgroup
print("First 2 rows, first 2 columns:\n", salaries[:2, :2])

reshaped_exp = np.reshape(np.arange(1, 7), (2, 3)) 
print("Reshaped Experience Array:\n", reshaped_exp) 

flattened_exp = reshaped_exp.flatten() 
print("Flattened Array:", flattened_exp) 

print("Transposed Array:\n", reshaped_exp.T)

# Different reshape
reshaped_3x2 = np.reshape(np.arange(1, 7), (3, 2))
print("3x2 Reshape:\n", reshaped_3x2)


bonus = np.array([5, 10, 15]) 
salaries_with_bonus = salaries + bonus  
print("Salaries after bonus:\n", salaries_with_bonus) 

# Scaling salaries
scaled = salaries * 1.1
print("Scaled Salaries:\n", scaled)


print("Mean experience:", np.mean(years_exp)) 
print("Std deviation of experience:", np.std(years_exp)) 
print("Max salary:", np.max(salaries), "Min salary:", np.min(salaries)) 
print("Sum of all salaries:", np.sum(salaries)) 

print("Median:", np.median(years_exp))
print("Percentiles:", np.percentile(years_exp, [25, 50, 75]))



angles = np.array([0, np.pi/4, np.pi/2]) 
print("Sine of angles:", np.sin(angles)) 
print("Cosine of angles:", np.cos(angles)) 

salary_sums = np.apply_along_axis(np.sum, 1, salaries) 
print("Sum of Salaries per person:", salary_sums) 

print("Square root:", np.sqrt(years_exp))
print("Log:", np.log(years_exp))



import pandas as pd 

data = np.random.randint(1, 50, size=(5, 3)) 
df_data = pd.DataFrame(data, columns=['X', 'Y', 'Z']) 
print("Generated Data:\n", df_data) 

df_data['Log_X'] = np.log(df_data['X']) 
df_data['Sqrt_Y'] = np.sqrt(df_data['Y']) 
print("DataFrame with NumPy Transformations:\n", df_data) 

print("Correlation Matrix:\n", df_data.corr()) 

print("Mean:\n", np.mean(df_data))
print("Median:\n", np.median(df_data))



df_data.to_csv('sample_data.csv', index=False) 
print("Data saved to 'sample_data.csv'.") 

df_imported = pd.read_csv('sample_data.csv') 
print("Imported DataFrame:\n", df_imported) 

summary_stats = df_imported.describe() 
print("Summary Statistics:\n", summary_stats) 

print("Column Means:\n", df_imported.mean()) 
print("Column Standard Deviations:\n", df_imported.std()) 

df_imported['Sum_XY'] = df_imported['X'] + df_imported['Y']
print(df_imported)

df_imported.to_csv('modified_data.csv', index=False)



import numpy as np
import pandas as pd

# Step 1: Load the Stack Overflow 2023 Developer Survey dataset
df_kaggle = pd.read_csv('survey_results_public.csv')
print("Loaded Dataset:\n", df_kaggle.head())

# Step 2: Select relevant columns
df_subset = df_kaggle[['Country', 'EdLevel', 'YearsCodePro', 'ConvertedComp']]
print("Subset of Data:\n", df_subset.head())

# Step 3: Clean the data by dropping rows with missing values
df_clean = df_subset.dropna()
print("Cleaned Data:\n", df_clean.head())

# Step 4: Categorize experience into groups
df_clean['ExperienceLevel'] = np.where(
    df_clean['YearsCodePro'] >= 10,
    'Senior',
    'Junior'
)
print("With Experience Level:\n", df_clean.head())

# Step 5: Group data by Country and ExperienceLevel, compute average salary
grouped_data = df_clean.groupby(
    ['Country', 'ExperienceLevel']
)['ConvertedComp'].mean()

print("Grouped Average Salary:\n", grouped_data.head())

# Step 6: Reset index for readability
grouped_data = grouped_data.reset_index()
print("Formatted Grouped Data:\n", grouped_data.head())







# %%

import numpy as np

STUDENT_NAME = "Robert Gabriel A. Gamas"
STUDENT_ID = 20250925

np.random.seed(STUDENT_ID)
data = np.random.randint(1, STUDENT_ID % 100 + 50, size=10)

print(f"{STUDENT_NAME}'s Array:", data)

mean_val = np.mean(data)
std_val = np.std(data)

print("Mean:", mean_val, "Std Dev:", std_val)   
# %%
import numpy as np 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
data = np.random.randint(1, STUDENT_ID % 100 + 50, size=10) 
print(f"{STUDENT_NAME}'s Array:", data) 
 
mean_val = np.mean(data) 
std_val = np.std(data) 
print("Mean:", mean_val, "Std Dev:", std_val) 
# %%
import numpy as np 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
matrix = np.random.randint(1, STUDENT_ID % 50 + 20, size=(3,4)) 
print(f"{STUDENT_NAME}'s Matrix:\n", matrix) 
 
row_sums = np.sum(matrix, axis=1) 
col_sums = np.sum(matrix, axis=0) 
print("Row sums:", row_sums) 
print("Column sums:", col_sums)
# %%
import numpy as np 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
arr3d = np.random.randint(0, STUDENT_ID % 20 + 10, size=(3,3,3)) 
print(f"{STUDENT_NAME}'s 3D Array:\n", arr3d) 
 
slice_mid = arr3d[:,1,:] 
print("Slice[:,1,:]:\n", slice_mid) 
# %%
import numpy as np 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
x = np.random.randint(1, STUDENT_ID % 100 + 50, size=10) 
filtered = x[(x>STUDENT_ID%50) & (x<STUDENT_ID%100)] 
print(f"{STUDENT_NAME}'s Original:", x) 
print("Filtered subset:", filtered) 
# %%
import numpy as np 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925
 
np.random.seed(STUDENT_ID) 
A = np.random.randint(1, STUDENT_ID % 50 + 20, size=(2,2)) 
B = np.random.randint(1, STUDENT_ID % 50 + 20, size=(2,2)) 
print("Matrix A:\n", A) 
print("Matrix B:\n", B) 
 
product = A @ B 
det_A = np.linalg.det(A) 
print("A @ B:\n", product) 
print("Determinant of A:", det_A)
# %%
import numpy as np 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
angles = np.linspace(0, 2*np.pi, 8) 
sine_vals = np.sin(angles) 
cos_vals = np.cos(angles) 
print(f"{STUDENT_NAME}'s Angles:", angles) 
print("Sine:", sine_vals) 
print("Cosine:", cos_vals)
# %%
import numpy as np 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
arr = np.random.randint(1, STUDENT_ID % 50 + 20, size=(4,4)) 
arr[::2, ::2] = 0 
print(f"{STUDENT_NAME}'s Modified 4x4 Array:\n", arr)
# %%
import numpy as np 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925
 
np.random.seed(STUDENT_ID) 
scores = np.random.randint(0, STUDENT_ID % 100 + 50, 10) 
grades = np.where(scores>=STUDENT_ID%70,'Pass','Fail') 
print(f"{STUDENT_NAME}'s Scores:", scores) 
print("Grades:", grades) 
# %%
import numpy as np 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
arr = np.random.randint(1, STUDENT_ID % 50 + 20, size=(3,4)) 
flat_arr = arr.flatten() 
transposed_arr = arr.T 
print("Original array:\n", arr) 
print("Flattened:", flat_arr) 
print("Transposed:\n", transposed_arr)
# %%
import numpy as np 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
arr = np.random.randint(1, STUDENT_ID % 50 + 20, (3,3)) 
mask = arr % 2 == 0 
arr[mask] = -1 
print("Array with conditional replacements:\n", arr)
# %%
import numpy as np 
import pandas as pd 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
df = pd.DataFrame({ 
    'Name': [STUDENT_NAME]*5, 
    'Score': np.random.randint(STUDENT_ID%50, 
STUDENT_ID%100+50,5), 
    'YearsCodePro': np.random.randint(0, STUDENT_ID%20+10,5) 
}) 
print(df)
# %%
import numpy as np 
import pandas as pd 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
df = pd.DataFrame({ 
    'EdLevel': ['Bachelor','Master','PhD','Bachelor','Master'], 
    # Corrected to use a functional salary range, e.g., 40000 to 150000 
    'ConvertedComp': np.random.randint(40000, 150000, 5)  
}) 
avg_salary = df.groupby('EdLevel')['ConvertedComp'].mean() 
print(avg_salary)
# %%
import numpy as np 
import pandas as pd 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
 
df = pd.DataFrame({ 
    'Country': ['Philippines','USA','UK','Canada','Germany'], 
    'ConvertedComp': np.random.randint(40000, 150000, 5)  
}) 
 
top5 = df.sort_values(by='ConvertedComp', ascending=False) 
print(top5)
# %%
import numpy as np 
import pandas as pd 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
df = pd.DataFrame({ 
    'Name':[STUDENT_NAME]*5, 
    'YearsCodePro': np.random.randint(0, STUDENT_ID%20+10,5) 
}) 
high_exp = df[df['YearsCodePro']>STUDENT_ID%10] 
print(high_exp)
# %%
import numpy as np 
import pandas as pd 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
 
df = pd.DataFrame({'ConvertedComp': np.random.randint(40000, 
150000, 5)}) 
 
bins = [0, 50000, 100000, 150000, 200000] 
labels = ['0-50k', '50-100k', '100-150k', '>150k'] 
 
df['Bracket'] = pd.cut(df['ConvertedComp'], bins=bins, labels=labels) 
print(df)
# %%
import numpy as np 
import pandas as pd 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
 
# Original Code Issue:  
# np.random.randint(STUDENT_ID%40000, STUDENT_ID%150000, 5)  
# -> np.random.randint(12345, 12345, 5) which is a zero-length range. 
 
# Corrected Code: Using a functional salary range (40000 to 150000) 
df = pd.DataFrame({'ConvertedComp': np.random.randint(40000, 
150000, 5)}) 
 
df['LogComp'] = np.log(df['ConvertedComp']) 
print(df)
# %%
import numpy as np 
import pandas as pd 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
 
df = pd.DataFrame({ 
    'YearsCodePro': np.random.randint(0, STUDENT_ID%20+10, 5), 
    'ConvertedComp': np.random.randint(40000, 150000, 5)  
}) 
 
corr_matrix = df.corr() 
print(corr_matrix)
# %%
import numpy as np 
import pandas as pd 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
 
df = pd.DataFrame({ 
    'EdLevel':['Bachelor','Master','PhD','Bachelor','Master'], 
    'ConvertedComp': np.random.randint(40000, 150000, 5)  
}) 
 
# Calculate mean, median, and standard deviation for each 'EdLevel' 
summary = df.groupby('EdLevel')['ConvertedComp'].agg(['mean','median','std']).reset_index() 
print(summary)
# %%import numpy as np 
import pandas as pd 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
 
# Generate salaries: [100727, 136195, 130612, 100727, 95233] 
df = pd.DataFrame({'ConvertedComp': np.random.randint(40000, 
150000, 5)}) 
 
threshold = 110000 
 
# Create the 'HighPay' column using np.where() 
df['HighPay'] = np.where(df['ConvertedComp'] > threshold, 'Yes', 'No') 
 
print(df)

# %%
import numpy as np 
import pandas as pd 
STUDENT_NAME = "Robert Gabriel A. Gamas" 
STUDENT_ID = 20250925 
 
np.random.seed(STUDENT_ID) 
 
df = pd.DataFrame({ 
    'Country': ['Philippines','USA','UK','Canada','Germany'], 
    'ConvertedComp': np.random.randint(40000, 150000, 5) 
}) 
 
# Group by 'Country' and calculate the mean and max 'ConvertedComp' 
top_countries = df.groupby('Country')['ConvertedComp'].agg(['mean','max']) 
print(top_countries)
# %%
