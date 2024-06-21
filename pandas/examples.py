
import pandas as pd


# df = pd.read_csv('exercise03_car_sales_data.csv')
#
# data = [1, 4, 4, 5]
#
# s = pd.Series(data)
#
# print(s.nunique())

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [17, 30, 35, 18],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago'],
}

df = pd.DataFrame(data)
print(df.iloc[0:3])


# to slice data by row and index we use the row label as first arg and column label as second one

# x = df.loc[0 , 'Name']
#
# print(x)

# df2 = df
#
# df2=df2.set_index("Name")
# print(df2.loc['Charlie', 'City'])

# print(df['Name'])

# print(df.iloc[2])  accessing row by index
# print(df.loc[1])   accessing row by label (similar to index by default)

# slicing

# print(df[['Name', 'Age']]) accessing specific columns of data

# print(df[1:3])    slicing by row

# print(df['Age'].unique())

# over_age = df[df['Age'] > 18]
# #
# # print(over_age)
#
#
# # save DataFrame as csv
#
# over_age.to_csv('over_age.csv', index=False)