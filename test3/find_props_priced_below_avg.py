import pandas as pd

input_file_path = 'assignment_data.csv'
output_file_path = 'props_less_than_average_price.csv'
df = pd.read_csv(input_file_path)
df['price_per_sq_ft'] = df.apply(lambda row: row['price'] / row['sq__ft'] if row['sq__ft'] != 0 else None, axis=1)
print(df.head())
average_price_per_sq_ft = df['price_per_sq_ft'].mean()
print("Average price per sq. foot", average_price_per_sq_ft)
df_new = df[df['price_per_sq_ft'] < average_price_per_sq_ft]

print('New max price per sq. foot', df_new['price_per_sq_ft'].max())
df_new.drop('price_per_sq_ft', axis=1)
df_new.to_csv(output_file_path, index=False)
