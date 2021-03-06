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
        day_data.append(forecast["DailyForecasts"])


        date_ISO = []
        for days in day_data:
            for dates in days:
                categories = dates["Date"]
                attach = convert_date(categories)
                date_ISO.append(attach) 


        min_temps = []
        max_temps = []
        daytime = []
        daytime_rain = []
        nighttime = []
        nighttime_rain = [] 
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
                                if temp == "Maximum":
                                        for values in dates[categories][temp]:
                                            if values == "Value":
                                                attach = dates[categories][temp][values]
                                                max_temps.append(attach)
                        if categories == "Day":
                            for key in dates[categories]:
                                if key == "LongPhrase":
                                    attach = dates[categories][key]
                                    daytime.append(attach)
                                if key == "RainProbability":
                                    attach = dates[categories][key]
                                    daytime_rain.append(attach)
                        if categories == "Night":
                            for key in dates[categories]:
                                if key == "LongPhrase":
                                    attach = dates[categories][key]
                                    nighttime.append(attach)
                                if key == "RainProbability":
                                    attach = dates[categories][key]
                                    nighttime_rain.append(attach)
        
        lowtempdic = {}         
        keys = date_ISO
        values = min_temps
        zip_obj = zip(keys, values)
        lowtempdic = dict(zip_obj)
        MinDictVal = min(lowtempdic, key=lowtempdic.get)


        hightempdic = {}
        keys = date_ISO
        values = max_temps
        zip_obj = zip(keys, values)
        hightempdic = dict(zip_obj)
        MaxDictVal = max(hightempdic, key=hightempdic.get)


        formatted_mintemps = []
        for temps in min_temps:
            convert = format_temperature(convert_f_to_c(temps))
            formatted_mintemps.append(convert)


        formatted_maxtemps = []
        for temps in max_temps:
            convert = format_temperature(convert_f_to_c(temps))
            formatted_maxtemps.append(convert)


        summary = f"{len(date_ISO)} Day Overview\n    The lowest temperature will be {format_temperature(convert_f_to_c(min(min_temps)))}, and will occur on {MinDictVal}.\n    The highest temperature will be {format_temperature(convert_f_to_c(max(max_temps)))}, and will occur on {MaxDictVal}.\n    The average low this week is {format_temperature(convert_f_to_c(calculate_mean(sum(min_temps),len(min_temps))))}.\n    The average high this week is {format_temperature(convert_f_to_c(calculate_mean(sum(max_temps),len(max_temps))))}.\n\n"
        # print(summary)


        dailysummary = []
        for x in range(len(date_ISO)): 
            l1 = f"-------- {date_ISO[x]} --------\n"
            dailysummary.append(l1)
            l2 = f"Minimum Temperature: {formatted_mintemps[x]}\n"
            dailysummary.append(l2)
            l3 = f"Maximum Temperature: {formatted_maxtemps[x]}\n"
            dailysummary.append(l3)
            l4 = f"Daytime: {daytime[x]}\n"
            dailysummary.append(l4)
            l5 = f"    Chance of rain:  {daytime_rain[x]}%\n"
            dailysummary.append(l5)
            l6 = f"Nighttime: {nighttime[x]}\n"
            dailysummary.append(l6)
            l7 = f"    Chance of rain:  {nighttime_rain[x]}%\n"
            dailysummary.append(l7)
            l8 = f"\n"
            dailysummary.append(l8)
        # print(dailysummary)

        dailyoutput = "".join(dailysummary)
        finaloutput = summary + dailyoutput

        return finaloutput


if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))


        # """Converts raw weather data into meaningful text.

        # Args:
        #     forecast_file: A string representing the file path to a file
        #         containing raw weather data.
        # Returns:∫
        #     A string containing the processed and formatted weather data.
        # """

    

