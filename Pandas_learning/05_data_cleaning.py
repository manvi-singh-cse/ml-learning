import pandas as pd

df_csv = pd.read_csv(r"C:\Users\LOQ\Downloads\Water_Quality_Risk_Contamination_Alert_System\water_potability.csv")  # Setting a column as the index
print(df_csv)

# DROPPING COLUMNS AND ROWS
df_csv = df_csv.drop(columns=["Sulfate", "Trihalomethanes"])     # column(s)
df_csv = df_csv.dropna(subset=["ph"])                            # null values of column
df_csv = df_csv.drop_duplicates()                                # duplicate rows 

# FILLING MISSING VALUES
df_csv = df_csv.fillna(df_csv.mean(numeric_only=True))           # with the mean of each column
df_csv = df_csv.fillna({"ph": df_csv["ph"].mean()})              # with the mean of that column

# REPLACING SPECIFIC VALUES IN A COLUMN OR DATAFRAME
df_csv["ph"] = df_csv["ph"].replace({0: 7.0})
df_csv = df_csv.replace({"ph": {0: 7.0}})  
print(df_csv)

# CHANGING DATA TYPES OF COLUMNS
df_csv["Potability"] = df_csv["Potability"].astype("bool")
df_csv["ph"] = df_csv["ph"].str.lower()                          # Converting string values in a column to lowercase
