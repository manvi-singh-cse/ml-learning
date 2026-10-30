import pandas as pd

# IMPORTING DATA FROM JSON FILE
df_json = pd.read_json("data.json")
print(df_json)
print(df_json.head())                                      # Display the first 5 rows of the DataFrame
print(df_json.tail())                                      # Display the last 5 rows of the DataFrame
print(df_json.to_string())

# IMPORTING DATA FROM CSV FILE
df_csv = pd.read_csv(r"C:\Users\LOQ\Downloads\Water_Quality_Risk_Contamination_Alert_System\water_potability.csv")
df_csv = pd.read_csv(r"C:\Users\LOQ\Downloads\Water_Quality_Risk_Contamination_Alert_System\water_potability.csv", index_col="ph")  # Setting a column as the index
print(df_csv)
print(df_csv.to_string())
print(df_csv.head())                                      # Display the first 5 rows of the DataFrame
print(df_csv.tail())                                      # Display the last 5 rows of the DataFrame

# ACCESSING ROW
print(df_csv["ph"])                                       # single column
print(df_csv[["ph", "Hardness"]])                         # multiple columns
print(df_csv.loc[0])                                      # using index label
print(df_csv.iloc[0])                                     # using integer position
print(df_csv.loc[3.71608007538699, ["Hardness","Solids"]])                    # using index label and column labels

print(df_csv.loc[3.71608007538699:5.584086638456089, ["Hardness","Solids"]])  
print(df_csv.loc[0:5, 0:3]) 

# FILTERING ROWS
print(f"Potable water : ", df_csv[df_csv["Potability"]==1].shape)
