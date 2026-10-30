# DATAFRAME - A tabular data structure 

import pandas as pd

# CREATING A DATAFRAME FROM A DICTIONARY
data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
df = pd.DataFrame(data)
df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])       # giving custom index

# ACCESSING ROW
print(df.loc["Employee 2"])                                                     # using index label
print(df.iloc[1])                                                               # using integer position

# ADDING A NEW COLUMN
df["City"] = ["New York", "Los Angeles", "Chicago"]

# ADDING A NEW ROW
new_row = pd.DataFrame({"Name": ["David"], "Age": [40], "City": ["Houston"]}, index=["Employee 4"])
df = pd.concat([df, new_row])                                                   

new_rows = pd.DataFrame([{"Name": "Patrick", "Age": 30, "City": "Houston"},
                        {"Name": "Sandy", "Age": 28, "City": "New York"}],
                        index=["Employee 5", "Employee 6"])
df = pd.concat([df, new_rows])
