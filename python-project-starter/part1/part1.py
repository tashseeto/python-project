import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"

    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """


def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")

    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """


def convert_f_to_c(temp_in_farenheit):
    temp_in_farenheit = (temp_in_farenheit - 32) / 1.8
    temp_in_farenheit = round(temp_in_farenheit, 1)
    return(temp_in_farenheit)
    
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    

def calculate_mean(total, num_items):
    return round(total / num_items, 1)
    
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    


def process_weather(forecast_file):
    with open("data/forecast_5days_a.json") as json_file:
        forecast = json.load(json_file)

    pass


day_data = []
for category, categorydata in forecast.items():
    if category == "DailyForecasts":
        day_data.append(categorydata)
# print(day_data)

 
date_ISO = []
for days in day_data:
    for dates in days:
        for categories in dates:
            if categories == "Date":
                attach = dates[categories]
# print(date_ISO)


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
# print(min_temps)


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
# print(max_temps)


daytime = []             
for days in day_data:
    for dates in days:
        for categories in dates:
                if categories == "Day":
                    for key in dates[categories]:
                        if key == "LongPhrase":
                            attach = dates[categories][key]
                            daytime.append(attach)
# print(daytime)


daytime_rain = []             
for days in day_data:
    for dates in days:
        for categories in dates:
                if categories == "Day":
                    for key in dates[categories]:
                        if key == "RainProbability":
                            attach = dates[categories][key]
                            daytime_rain.append(attach)
# print(daytime_rain)


nighttime = []             
for days in day_data:
    for dates in days:
        for categories in dates:
                if categories == "Night":
                    for key in dates[categories]:
                        if key == "LongPhrase":
                            attach = dates[categories][key]
                            nighttime.append(attach)
# print(nighttime)


nighttime_rain = []             
for days in day_data:
    for dates in days:
        for categories in dates:
                if categories == "Night":
                    for key in dates[categories]:
                        if key == "RainProbability":
                            attach = dates[categories][key]
                            nighttime_rain.append(attach)
# print(nighttime_rain)

 

  





    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """


if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))





