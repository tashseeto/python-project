import plotly.express as px
from datetime import datetime


DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    temp_in_farenheit = (temp_in_farenheit - 32) / 1.8
    temp_in_farenheit = round(temp_in_farenheit, 1)
    return(temp_in_farenheit)
    

import json
with open("data/forecast_5days_a.json") as json_file:
    forecast = json.load(json_file)

day_data = []
day_data.append(forecast["DailyForecasts"])


date_ISO = []
for days in day_data:
        for dates in days:
            categories = dates["Date"]
            attach = convert_date(categories)
            date_ISO.append(attach) 


min_temps = []
max_temps = []
minrealfeel = []
minrealfeelshade = []
for days in day_data:
    for dates in days:
        for categories in dates:
                if categories == "Temperature":
                    for temp in dates[categories]:
                        if temp == "Minimum":
                            for values in dates[categories][temp]:
                                if values == "Value":
                                    attach = convert_f_to_c(dates[categories][temp][values])
                                    min_temps.append(attach)
                        if temp == "Maximum":
                            for values in dates[categories][temp]:
                                if values == "Value":
                                    attach = convert_f_to_c(dates[categories][temp][values])
                                    max_temps.append(attach)
                if categories == "RealFeelTemperature":
                    for temp in dates[categories]:
                        if temp == "Minimum":
                            for values in dates[categories][temp]:
                                if values == "Value":
                                    attach = convert_f_to_c(dates[categories][temp][values])
                                    minrealfeel.append(attach)
                if categories == "RealFeelTemperatureShade":
                    for temp in dates[categories]:
                        if temp == "Minimum":
                            for values in dates[categories][temp]:
                                if values == "Value":
                                    attach = convert_f_to_c(dates[categories][temp][values])
                                    minrealfeelshade.append(attach)
# print(minrealfeel)


''' 1. need a df
2. in df a need a list of min values
3. get min values - copy code from part 1
4. put min values in df
5. once working add remaining values '''


df = {
"Minimum Temperature": min_temps,
"Maximum Temperature": max_temps,
"Dates": date_ISO
}

fig = px.line(
df,
y=["Minimum Temperature", "Maximum Temperature"],
x="Dates",
title=f"{len(date_ISO)} day forecast minimum and maximum temperatures")

fig.update_layout(
yaxis_title="Temperature (°C)")

fig.show()



df = {
"Minimum Temperature": min_temps,
"Minimum Real Feel": minrealfeel,
"Minimum Real Feel Shade": minrealfeelshade,
"Dates": date_ISO
}

fig = px.line(
df,
y=["Minimum Temperature","Minimum Real Feel","Minimum Real Feel Shade"],
x="Dates",
title=f"{len(date_ISO)} day forecast minimum, minimum real free and minimum real free shade temperatures")

fig.update_layout(
yaxis_title="Temperature (°C)")


fig.show()



# def min_data(data):
#     counter = 0
#     min_data_list = []
#     while counter < (len(data)):
#         min_temp = (data[counter]["Temperature"]["Minimum"]["Value"])
#         min_data_list.append(format_temperature(convert_f_to_c(min_temp)))
#         counter = counter + 1
#     return min_data_list

# print(min_data_list)
# min_list = (min_data(data))



# df = {
#     "Minimum": min_list,
#     "Minimum Real Feel": real_feel,
#     "Minimum Real Feel Shade" : real_feel_shade,
#     "Date": dates
# }



# fig = px.line(
#     df,
#     y="our_data",
#     x="columns", 
#     title="example")

# fig.show()

# fig = px.line(
# df,
# y=["Minimum Temperature","Maxmium Temperature"],
# x="Dates",
# title=f"{len(min_temps)} day forecast minimum and maximum temperatures")

# fig.show()

# fig.write_html("cats.html")
# the above used if fig.show() doesn't work