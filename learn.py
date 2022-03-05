# working with csv data in python
with open("weather_data.csv") as weather_data:
    data = weather_data.readlines()#converting the lines of the file into an item in a list
    print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)#takes the file in question and reads it and outputs the data as a csv reader object
    temperatures = []
    for row in data:
        if row[1] == 'temp':
            pass
        else:
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data) #prints it in a tabular form
# getting hold of a single column in pandas
print(data["temp"])


# dataframes and working with rows and columns
print(type(data)) #<class 'pandas.core.frame.DataFrame'>

data_dict = data.to_dict() #creates a dictionary from the data
print(data_dict)#converting a column/(series) to list
avg = sum(data["temp"].to_list())/len(data["temp"].to_list())
print(f"Average of temps {avg}") 
# getting the max
print(data["temp"].max())

# another way of working with colums
print(data.condition)

# getting data that are in the rows of our data frame
print(data[data.day == "Monday"]) #returns the day that you want

# getting the day that had the highest temperature in the week
print(data[data.temp == data.temp.max()])

# creating a dataframe from scratch
data_dict = {
    "students": ["anny", "James", "angela"],
    "scores": [76, 56, 65]
}
# how do we create a dataframe from the table above
data = pandas.DataFrame(data_dict)
print(data)

# we can save it to a file
data.to_csv("new_data.csv")