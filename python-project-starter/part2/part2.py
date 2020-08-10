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


    date_ISO = []
    for days in day_data:
        for dates in days:
            for categories in dates:
                if categories == "Date":
                    attach = dates[categories]
                    date_ISO.append(attach)
    
    dates = []
    for days in date_ISO:
        attach = convert_date(days)
        dates.append(attach)
        # print(dates)


    min_temps = []
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


    max_temps = []
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



df = {
    "Minimum Temperature": [format_temperature(convert_f_to_c(min_temps[0])), format_temperature(convert_f_to_c(min_temps[1])), format_temperature(convert_f_to_c(min_temps[2])), format_temperature(convert_f_to_c(min_temps[3])), format_temperature(convert_f_to_c(min_temps[4]))],
    "Maxmium Temperature": [format_temperature(convert_f_to_c(max_temps[0])), format_temperature(convert_f_to_c(max_temps[1])), format_temperature(convert_f_to_c(max_temps[2])), format_temperature(convert_f_to_c(max_temps[3])), format_temperature(convert_f_to_c(max_temps[4]))],
    "Dates": [convert_date(date_ISO[0]), convert_date(date_ISO[1]), convert_date(date_ISO[2]), convert_date(date_ISO[3]), convert_date(date_ISO[4])]
}



# date_ISO[1], date_ISO[2], date_ISO[3], date_ISO[4]]

# dates[1], dates[2], dates[3], dates[4]]

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