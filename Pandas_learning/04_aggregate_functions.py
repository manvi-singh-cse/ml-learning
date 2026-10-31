import pandas as pd

df_csv = pd.read_csv(r"C:\Users\LOQ\Downloads\Water_Quality_Risk_Contamination_Alert_System\water_potability.csv")  # Setting a column as the index

# AGGREGATE FUNCTIONS ON DATAFRAME
print(df_csv.mean())
print(df_csv.mean(numeric_only=True))
print(df_csv.sum())
print(df_csv.count())
print(df_csv.min())
print(df_csv.max())

# AGGREGATE FUNCTIONS ON A SPECIFIC COLUMN
print(df_csv["ph"].mean())
print(df_csv["ph"].sum())
print(df_csv["ph"].count())
print(df_csv["ph"].min())
print(df_csv["ph"].max())

# GROUPING THE DATA
print(df_csv.groupby("Potability").count()) 
