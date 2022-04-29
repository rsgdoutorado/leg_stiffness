import pandas as pd
import Stiffness as stf

df = pd.read_csv('data.csv', sep=';')

result = pd.DataFrame()
for row in df.index:
    item = df.iloc[[row]]
    calc = stf.Stiffness(item)
    df_dict = pd.DataFrame([calc.results()])
    result = pd.concat([result, df_dict], ignore_index=True)
print(result.head())