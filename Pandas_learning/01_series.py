# SERIES - 1-D labelled array 

import pandas as pd
print(pd.__version__)

#CREATING A SERIES FROM A LIST
data = [10, 20, 30]
unindexed_series = pd.Series(data)
print(unindexed_series)
series = pd.Series(data, index=['a', 'b', 'c'])    # using custom index labels
print(series)

# ACCESSING & MODIFYING VALUE
print(series.loc['b'])                             # using index label
print(series.iloc[0])                              # using integer position
series.loc['b'] = 25                               # using index label
print(series)

# FILTERING VALUES
print(series[series>=20])

# CREATING A SERIES FROM A DICTIONARY
calories = {"day 1": 1750, "day 2": 2000, "day 3": 1500}   
series = pd.Series(calories)
print(series)
print(series.loc['day 1']) 
series.loc['day 3'] += 500
print(series)
print(series[series>=1800])
