import pandas
# we are targetting a table with fur color and total count, grey, cinammon(red) or black
# total grey, cinammon and black
# take that data and build a dataframe for it

# print(data[data.day == "Monday"])
# Gray Cinnamon Black
data = pandas.read_csv("central_park_squirell_census.csv")

gray = data[data["Primary Fur Color"] == "Gray"]
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
black = data[data["Primary Fur Color"] == "Black"]

total_gray = len(gray["Hectare Squirrel Number"].to_list())
total_cinnamon = len(cinnamon["Hectare Squirrel Number"].to_list())
total_black = len(black["Hectare Squirrel Number"].to_list())

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "totals": [total_gray, total_cinnamon, total_black]
}
minified = pandas.DataFrame(data_dict)
minified.to_csv("Squirell_census_summary.csv")