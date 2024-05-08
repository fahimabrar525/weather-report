# import  csv
#
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data['temp'].to_list()
# #
# # print(data["temp"].mean())
# # print(data["temp"].max())
# #
# # print(data[data.day == "Monday"])
# #
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# celsius = monday.temp
# fahrenheit = (celsius * 1.8) + 32
# print(fahrenheit)

import pandas

data = pandas.read_csv("./228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("count.csv")



