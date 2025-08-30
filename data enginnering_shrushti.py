# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from Google Drive
file_path = "C:\\Users\\SAMARTH KALE\\Downloads\\healthcare_dataset_1000.csv"
df = pd.read_csv(file_path)

# -------------------------------
# 1. BASIC INFO
# -------------------------------
print("Original Dataset Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("\nMissing values per column:\n", df.isnull().sum())

# -------------------------------
# 2. DATA CLEANING
# -------------------------------
# Remove duplicates
df = df.drop_duplicates()

# Handle missing values (customize according to your dataset columns)
if "Age" in df.columns:
    df["Age"] = df["Age"].fillna(df["Age"].median())

if "Gender" in df.columns:
    df["Gender"] = df["Gender"].fillna("Unknown")

if "Disease" in df.columns:
    df["Disease"] = df["Disease"].fillna("Not Specified")

if "TreatmentCost" in df.columns:
    df["TreatmentCost"] = df["TreatmentCost"].fillna(df["TreatmentCost"].mean())

# Save cleaned dataset
cleaned_path = "C:\\Users\\SAMARTH KALE\\Downloads\\healthcare_dataset_1000.csv"
df.to_csv(cleaned_path, index=False)
print(f"\n Cleaned dataset saved at: {cleaned_path}")
print("New Shape:", df.shape)

# -------------------------------
# 3. VISUALIZATIONS
# -------------------------------
plt.style.use("seaborn-v0_8")

# (A) Disease frequency
if "Disease" in df.columns:
    plt.figure(figsize=(10, 5))
    sns.countplot(y=df["Disease"], order=df["Disease"].value_counts().index)
    plt.title("Most Common Diseases")
    plt.xlabel("Number of Patients")
    plt.ylabel("Disease")
    plt.tight_layout()
    plt.show()

# (B) Average Treatment Cost by Disease
if "TreatmentCost" in df.columns and "Disease" in df.columns:
    plt.figure(figsize=(10, 5))
    df.groupby("Disease")["TreatmentCost"].mean().sort_values().plot(kind="barh")
    plt.title("Average Treatment Cost by Disease")
    plt.xlabel("Average Cost")
    plt.ylabel("Disease")
    plt.tight_layout()
    plt.show()

# (C) Gender distribution
if "Gender" in df.columns:
    plt.figure(figsize=(6, 6))
    df["Gender"].value_counts().plot(kind="pie", autopct='%1.1f%%')
    plt.title("Patient Gender Distribution")
    plt.ylabel("")
    plt.show()

# (D) Age distribution
if "Age" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Age"], bins=20, kde=True)
    plt.title("Age Distribution of Patients")
    plt.xlabel("Age")
    plt.ylabel("Number of Patients")
    plt.tight_layout()
    plt.show()

# -------------------------------
# 4. DISPLAY CLEANED DATA
# -------------------------------

# Show first 10 rows
print("\nSample of Cleaned Dataset:\n")
print(df.head(10))

# Show summary statistics
print("\nSummary Statistics:\n")
print(df.describe(include="all"))

# If dataset is large, display in Colab as a scrollable table
import IPython.display as display

display.display(df.head(50))  # show first 50 rows nicely