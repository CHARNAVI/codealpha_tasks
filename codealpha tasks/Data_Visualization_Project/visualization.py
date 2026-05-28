import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")
df = pd.read_csv("train.csv")
plt.figure(figsize=(6,4))
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.figure(figsize=(7,5))
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.figure(figsize=(7,5))
sns.countplot(x='Pclass', data=df)
plt.title("Passenger Class Distribution")
plt.figure(figsize=(8,5))
df['Age'].hist(bins=20)
plt.title("Age Distribution")
plt.figure(figsize=(8,5))
sns.histplot(df['Fare'], bins=30, kde=True)
plt.title("Fare Distribution")
plt.figure(figsize=(10,6))
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.figure(figsize=(8,5))
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df)
plt.title("Age vs Fare")
survival_counts = df['Survived'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(
    survival_counts,
    labels=['Not Survived', 'Survived'],
    autopct='%1.1f%%'
)
plt.title("Survival Percentage")
plt.show()