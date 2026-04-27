import pandas as pd
import numpy as np

# =========================
# LOAD DATASET
# =========================
df = pd.read_csv("Most Popular Programming Languages.csv")
df['Month'] = pd.to_datetime(df['Month'])

# =========================
# ASSIGNED LANGUAGE (EXERCISE 1 & 2)
# =========================
lang = 'PhP Worldwide(%)'

# =========================
# EXERCISE 1: GROWTH ANALYSIS
# =========================
data1 = pd.DataFrame()
data1['Month'] = df['Month']
data1['Popularity'] = df[lang]

# Growth rate
data1['Growth_Rate'] = data1['Popularity'].pct_change() * 100

# Moving stats
data1['Moving_Avg'] = data1['Popularity'].rolling(window=3).mean()
data1['Moving_STD'] = data1['Popularity'].rolling(window=3).std()

# Phase classification
conditions = [
    data1['Growth_Rate'] > 5,
    data1['Growth_Rate'] < -5
]
choices = ['Growth', 'Decline']
data1['Phase'] = np.select(conditions, choices, default='Stable')

print("\n================ EXERCISE 1 ================")
print("Assigned Language:", lang)
print(data1)

print("\nStatistical Summary")
print(data1['Popularity'].describe())

print("\nPhase Counts")
print(data1['Phase'].value_counts())

initial = data1['Popularity'].iloc[0]
final = data1['Popularity'].iloc[-1]
overall_growth = ((final - initial) / initial) * 100

print("\nInitial:", initial)
print("Final:", final)
print("Overall Growth %:", overall_growth)


# =========================
# EXERCISE 2: LIFECYCLE CLASSIFICATION
# =========================
data2 = pd.DataFrame()
data2['Month'] = df['Month']
data2['Popularity'] = df[lang]

data2['Growth_Rate'] = data2['Popularity'].pct_change() * 100
data2['Moving_Avg'] = data2['Popularity'].rolling(window=6).mean()
data2['Moving_STD'] = data2['Popularity'].rolling(window=6).std()

mean_g = np.mean(data2['Growth_Rate'].dropna())
std_g = np.std(data2['Growth_Rate'].dropna())

conditions2 = [
    (data2['Growth_Rate'] > 0) & (data2['Growth_Rate'] < mean_g),
    (data2['Growth_Rate'] > mean_g),
    (abs(data2['Growth_Rate']) <= 1),
    (data2['Growth_Rate'] < 0) & (data2['Growth_Rate'] < -std_g)
]
choices2 = ['Introduction', 'Growth', 'Maturity', 'Decline']

data2['Lifecycle_Phase'] = np.select(conditions2, choices2, default='Maturity')

print("\n================ EXERCISE 2 ================")
print(data2)

print("\nLifecycle Counts")
counts = data2['Lifecycle_Phase'].value_counts()
print(counts)

print("\nLifecycle Percentages")
print((counts / len(data2)) * 100)

dominant = counts.idxmax()
print("\nDominant Stage:", dominant)


# =========================
# EXERCISE 3: COMPARATIVE ANALYSIS
# =========================

lang1 = 'PhP Worldwide(%)'
lang2 = 'Python Worldwide(%)'

a = df[lang1]
b = df[lang2]

# Stats
mean_a = a.mean()
mean_b = b.mean()

median_a = a.median()
median_b = b.median()

std_a = a.std()
std_b = b.std()

# Correlation
corr = np.corrcoef(a, b)[0, 1]

# Dominance ratio
dominance = (a > b).sum()
dom_ratio = (dominance / len(df)) * 100

# Relative Performance Index (RPI)
rpi = ((mean_a - mean_b) / mean_b) * 100

# Cross-over points
crossovers = (a > b) & (a.shift(1) <= b.shift(1))
crossover_count = crossovers.sum()

summary = pd.DataFrame({
    'Mean_A':[mean_a],
    'Mean_B':[mean_b],
    'Median_A':[median_a],
    'Median_B':[median_b],
    'Std_A':[std_a],
    'Std_B':[std_b],
    'Correlation':[corr],
    'Dominance_%':[dom_ratio],
    'RPI':[rpi],
    'Crossovers':[crossover_count]
})

print("\n================ EXERCISE 3 ================")
print(summary)