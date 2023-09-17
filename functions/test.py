import pandas as pd
from calculations import Calculations

data = {
    "Value": [155, 200, 350, 400, 570],
    "CO": ["0", "1", "0.2", "0.6", "0"],
    "CU": ["1", "0", "0.7", "0", "0.6"],
}
df = pd.DataFrame(data)

calculation = Calculations(df)
result = calculation.add_new_columns("Value", "CO", "CU", "new_CO", "new_CU")
print(result)
