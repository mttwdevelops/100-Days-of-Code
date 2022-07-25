# Created 7/25/2022

# with open ("weather_data_pandas.csv") as file:
#     data = file.readlines()

# print(data)

# now the above is one way to do this, but there is another, more efficient, way

# import csv

# with open("weather_data_pandas.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         # print(row)

# print(temperatures)

# now the above was pretty helpful, but there's quite a bit of faff still. 
# There has to be a more efficient way to do this...

import pandas

data = pandas.read_csv("weather_data_pandas.csv")
print(data)
print(data["temp"])

# Now isn't that a lot more simple?

# let's get some lists

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

mean_list = data["temp"].mean()
print(mean_list)

print(data["temp"].max())

# we can also call column names as:
print(data.condition)

# to get the row instead of column
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# now we create a dataframe from scratch and save them
data_dict = {
    "students": ["Amy", "James"],
    "scores": [76, 56]
}
data = pandas.DataFrame(data_dict)
data.to_csv("newdata.csv")