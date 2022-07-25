# Created 7/25/2022

# Primary Fur Color (Gray Cinnamon Black), get count for them

import pandas

data = pandas.read_csv("Squirrel_Data.csv")
print(data)


print(data.columns)
count_list = data["Primary Fur Color"].to_list()
# print(count_list)

# temp_tup = pandas.unique(count_list)
# print(temp_tup)


# now we create a dataframe from scratch and save them
# Output is stored as "newdata.csv"
gray_count = count_list.count("Gray"); cin_count = count_list.count("Cinnamon"); black_count = count_list.count("Black")
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "scores": [gray_count, cin_count, black_count]
}
data = pandas.DataFrame(data_dict)
data.to_csv("newdata.csv")