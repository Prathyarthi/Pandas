import pandas as pd

df = pd.read_csv('services.csv')

print(type(df))

# To get all column names : 
print(df.columns)

# To convert this dataframe into a list : 
print(list(df.columns))
print(type(list(df.columns)))

# To get first five records : 
print(df.head())
print(df.head(10))  # SPecific number of records

print(df.tail())  # Last five 


# To get the datatypes present in the dataset : 
print(df.dtypes)

# To select only specific columns to be displayed : 
print(df['wait_time']) # this is called series
print(type(df['wait_time']))  

print(df[['wait_time']])
print(type(df[['wait_time']]))  # this is of type dataframe

# Multiple columns cannot be accessed : 
# print(df['wait_time','id'])

# But if we want multiple records, pass it as a list
print(df[['wait_time','id']])


# To save the data in the local system : 
df.to_csv("services_saved.csv")

# df.to_csv("services_saved.csv",index=False)

print("Length of dataframe :",len(df))

print(df.describe())   # It will give description about the dataset, but only numerical data

# To get description about object data : 
df1 = df[df.dtypes[df.dtypes == 'object'].index].describe()
print(df1)

# To get description about int data : 
df2 = df[df.dtypes[df.dtypes == 'int64'].index].describe()
print(df2)

# Display using rows, use list slicing : 
print(df[['wait_time','id']][4:11]) 