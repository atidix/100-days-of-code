# with open("day-25/weather_data.csv") as weather:
#     data = weather.readlines()

# print(data)

# import csv
# temp = []

# with open("day-25/weather_data.csv") as weather:
#     data = csv.reader(weather)
#     for row in data:
#         temperature = row[1]
#         if row[1] != "temp":
#             temp.append(int(row[1]))

# print (temp)

import pandas

data = pandas.read_csv("day-25/weather_data.csv")
#print(data["temp"])
#print(data.temp)

temp = data["temp"]
# avg_temp = sum(temp)/ len(temp)
# print(avg_temp)

# average = temp.mean()
# print(average)

#max = temp.max()
# print(max)

#print(data[data.day == "Monday"])

#print(data[temp == max])

# monday = data[data.day == "Monday"]
# print(monday.temp)