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
    for category, categorydata in forecast.items():
        if category == "DailyForecasts":
            day_data.append(categorydata)
    # print(day_data)


    counter = 0 
    date_ISO = []
    while counter < len(day_data):
        counter += 1
        for days in day_data:
            # print(days) prints all days
            for dates in days:
                # print(dates) prints days separately
                for categories in dates:
                    # relates to key in date dictionary
                    if categories == "Date":
                        attach = convert_date(dates[categories])
                        date_ISO.append(attach)   
    # print(date_ISO)


    counter = 0
    min_temps = []
    while counter < len(day_data):
        counter += 1 
        for days in day_data:
            for dates in days:
                for categories in dates:
                        if categories == "Temperature":
                            for temp in dates[categories]:
                                if temp == "Minimum":
                                    for values in dates[categories][temp]:
                                        if values == "Value":
                                            attach = dates[categories][temp][values]
                                            min_temps.append(attach)


    counter = 0
    formatted_mintemps = []
    while counter < len(day_data):
        counter += 1
        for temps in min_temps:
            convert = format_temperature(convert_f_to_c(temps))
            formatted_mintemps.append(convert)


    counter = 0
    max_temps = []
    while counter < len(day_data):
        counter += 1
        for days in day_data:
            for dates in days:
                for categories in dates:
                        if categories == "Temperature":
                            for temp in dates[categories]:
                                if temp == "Maximum":
                                    for values in dates[categories][temp]:
                                        if values == "Value":
                                            attach = dates[categories][temp][values]
                                            max_temps.append(attach)


    counter = 0
    formatted_maxtemps = []
    while counter < len(day_data):
        counter += 1
        for temps in max_temps:
            convert = format_temperature(convert_f_to_c(temps))
            formatted_maxtemps.append(convert)


    counter = 0
    minrealfeel = []
    while counter < len(day_data):
        counter += 1
        for days in day_data:
            for dates in days:
                for categories in dates:
                        if categories == "RealFeelTemperature":
                            for temp in dates[categories]:
                                if temp == "Minimum":
                                    for values in dates[categories][temp]:
                                        if values == "Value":
                                            attach = dates[categories][temp][values]
                                            minrealfeel.append(attach)
    # print(minrealfeel)


    counter = 0
    minrealfeelshade = []
    while counter < len(day_data):
        counter += 1
        for days in day_data:
            for dates in days:
                for categories in dates:
                        if categories == "RealFeelTemperatureShade":
                            for temp in dates[categories]:
                                if temp == "Minimum":
                                    for values in dates[categories][temp]:
                                        if values == "Value":
                                            attach = dates[categories][temp][values]
                                            minrealfeelshade.append(attach)
    # print(minrealfeelshade)


def min_data(data):
    counter = 0
    min_data_list = []
    while counter < (len(data)):
        min_temp = (data[counter]["Temperature"]["Minimum"]["Value"])
        min_data_list.append(format_temperature(convert_f_to_c(min_temp)))
        counter = counter + 1
    return min_data_list

print(min_data_list)
min_list = (min_data(data))



df = {
    "Minimum": min_list,
    "Minimum Real Feel": real_feel,
    "Minimum Real Feel Shade" : real_feel_shade,
    "Date": dates
}

# df = {
#     "Minimum Temperature": [formatted_mintemps[x]],
#     "Maxmium Temperature": [formatted_maxtemps[x]],
#     "Dates": [date_ISO[x]]
# }

# fig = px.line(
#     df,
#     y="our_data",
#     x="columns", 
#     title="example")

# fig.show()

fig = px.line(
    df,
    y=["Minimum Temperature","Maxmium Temperature"],
    x="Dates",
    title=f"{len(min_temps)} day forecast minimum and maximum temperatures")

fig.show()

# fig.write_html("cats.html")
# the above used if fig.show() doesn't work