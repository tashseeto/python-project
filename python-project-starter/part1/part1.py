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
    with open(forecast_file) as json_file:
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


        daytime = []             
        for days in day_data:
            for dates in days:
                for categories in dates:
                        if categories == "Day":
                            for key in dates[categories]:
                                if key == "LongPhrase":
                                    attach = dates[categories][key]
                                    daytime.append(attach)


        daytime_rain = []             
        for days in day_data:
            for dates in days:
                for categories in dates:
                        if categories == "Day":
                            for key in dates[categories]:
                                if key == "RainProbability":
                                    attach = dates[categories][key]
                                    daytime_rain.append(attach)


        nighttime = []             
        for days in day_data:
            for dates in days:
                for categories in dates:
                        if categories == "Night":
                            for key in dates[categories]:
                                if key == "LongPhrase":
                                    attach = dates[categories][key]
                                    nighttime.append(attach)


        nighttime_rain = []             
        for days in day_data:
            for dates in days:
                for categories in dates:
                        if categories == "Night":
                            for key in dates[categories]:
                                if key == "RainProbability":
                                    attach = dates[categories][key]
                                    nighttime_rain.append(attach)


        summary = (f"{len(min_temps)} Day Overview\n    The lowest temperature will be {format_temperature(convert_f_to_c(min(min_temps)))}, and will occur on xx.\n    The highest temperature will be {format_temperature(convert_f_to_c(max(max_temps)))}, and will occur on xx.\n    The average low this week is {format_temperature(convert_f_to_c(calculate_mean(sum(min_temps),len(min_temps))))}.\n    The average high this week is {format_temperature(convert_f_to_c(calculate_mean(sum(max_temps),len(max_temps))))}.\n\n")

        day1 = (f"-------- {convert_date(date_ISO[0])} --------\nMinimum Temperature: {format_temperature(convert_f_to_c(min_temps[0]))}\nMaximum Temperature: {format_temperature(convert_f_to_c(max_temps[0]))}\nDaytime: {daytime[0]}\n    Chance of rain:  {daytime_rain[0]}%\nNighttime: {nighttime[0]}\n    Chance of rain:  {nighttime_rain[0]}%\n\n")

        day2 = (f"-------- {convert_date(date_ISO[1])} --------\nMinimum Temperature: {format_temperature(convert_f_to_c(min_temps[1]))}\nMaximum Temperature: {format_temperature(convert_f_to_c(max_temps[1]))}\nDaytime: {daytime[1]}\n    Chance of rain:  {daytime_rain[1]}%\nNighttime: {nighttime[1]}\n    Chance of rain:  {nighttime_rain[1]}%\n\n")

        day3 = (f"-------- {convert_date(date_ISO[2])} --------\nMinimum Temperature: {format_temperature(convert_f_to_c(min_temps[2]))}\nMaximum Temperature: {format_temperature(convert_f_to_c(max_temps[2]))}\nDaytime: {daytime[2]}\n    Chance of rain:  {daytime_rain[2]}%\nNighttime: {nighttime[2]}\n    Chance of rain:  {nighttime_rain[2]}%\n\n")

        day4 = (f"-------- {convert_date(date_ISO[3])} --------\nMinimum Temperature: {format_temperature(convert_f_to_c(min_temps[3]))}\nMaximum Temperature: {format_temperature(convert_f_to_c(max_temps[3]))}\nDaytime: {daytime[3]}\n    Chance of rain:  {daytime_rain[3]}%\nNighttime: {nighttime[3]}\n    Chance of rain:  {nighttime_rain[3]}%\n\n")

        day5 = (f"-------- {convert_date(date_ISO[4])} --------\nMinimum Temperature: {format_temperature(convert_f_to_c(min_temps[4]))}\nMaximum Temperature: {format_temperature(convert_f_to_c(max_temps[4]))}\nDaytime: {daytime[4]}\n    Chance of rain:  {daytime_rain[4]}%\nNighttime: {nighttime[4]}\n    Chance of rain:  {nighttime_rain[4]}%\n\n")
    
        
        #  """Converts raw weather data into meaningful text.

        # Args:
        #     forecast_file: A string representing the file path to a file
        #         containing raw weather data.
        # Returns:∫
        #     A string containing the processed and formatted weather data.
        # """

        alldays = summary + day1 + day2 + day3 + day4 + day5

        return alldays

        if __name__ == "__main__":
            print(process_weather("data/forecast_5days_a.json"))





