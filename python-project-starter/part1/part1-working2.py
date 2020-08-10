import json
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

def calculate_mean(total, num_items):
    return round(total / num_items, 1)


import json 
with open("data/forecast_5days_a.json") as json_file:
    forecast = json.load(json_file)
# print(forecast)


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
            # print(days) prints all days
            for dates in days:
                # print(dates) prints days separately
                for categories in dates:
                    # relates to key in date dictionary
                        if categories == "Temperature":
                            # print(dates[categories])
                            # prints both min and max dics
                                # for temp in dates[categories]:
                                # print(dates[categories][temp])
                                # prints the inner dict with values
                            for temp in dates[categories]:
                                if temp == "Minimum":
                                    # print(dates[categories][temp])
                                    # print the min : inner dict values
                                    for values in dates[categories][temp]:
                                        # print(dates[categories][temp][values])
                                        # prints only the values of the mini inner dic
                                        if values == "Value":
                                            # print(dates[categories][temp][values])
                                            # prints only the first value
                                            attach = dates[categories][temp][values]
                                            min_temps.append(attach)
    # print(min_temps)

    avemin = []
    average = convert_f_to_c(calculate_mean(sum(min_temps),len(min_temps)))
    avemin.append(average)
    # print(avemin)

    # average = format_temperature(convert_f_to_c(calculate_mean(sum(min_temps),len(min_temps))))

    lowtempdic = {}         
    keys = date_ISO
    values = min_temps
    zip_obj = zip(keys, values)
    lowtempdic = dict(zip_obj)
    # print(lowtempdic)
    MinDictVal = min(lowtempdic, key=lowtempdic.get)
    # print(MinDictVal)
    

    counter = 0
    formatted_mintemps = []
    while counter < len(day_data):
        counter += 1
        for temps in min_temps:
            convert = format_temperature(convert_f_to_c(temps))
            formatted_mintemps.append(convert)
    # print(formatted_mintemps)


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
    # print(max_temps)
    
    avemax = []
    average = format_temperature(convert_f_to_c(calculate_mean(sum(max_temps),len(max_temps))))
    avemax.append(average)
    # print(avemax)

    
    hightempdic = {}
    keys = date_ISO
    values = max_temps
    zip_obj = zip(keys, values)
    hightempdic = dict(zip_obj)
    # print(hightempdic)
    MaxDictVal = max(hightempdic, key=hightempdic.get)
    # print(MaxDictVal)
 
    
    counter = 0
    formatted_maxtemps = []
    while counter < len(day_data):
        counter += 1
        for temps in max_temps:
            convert = format_temperature(convert_f_to_c(temps))
            formatted_maxtemps.append(convert)
    # print(formatted_maxtemps)

    counter = 0
    daytime = []    
    while counter < len(day_data):
        counter += 1         
        for days in day_data:
            for dates in days:
                for categories in dates:
                        if categories == "Day":
                            for key in dates[categories]:
                                if key == "LongPhrase":
                                    # print(dates[categories][key])
                                    # prints the longphrase description
                                    attach = dates[categories][key]
                                    daytime.append(attach)
    # print(daytime)

    counter = 0
    daytime_rain = []       
    while counter < len(day_data):
        counter += 1          
        for days in day_data:
            for dates in days:
                for categories in dates:
                        if categories == "Day":
                            for key in dates[categories]:
                                if key == "RainProbability":
                                    # print(dates[categories][key])
                                    # prints the longphrase description
                                    attach = dates[categories][key]
                                    daytime_rain.append(attach)
    # print(daytime_rain)


    counter = 0
    nighttime = []     
    while counter < len(day_data):
        counter += 1         
        for days in day_data:
            for dates in days:
                for categories in dates:
                        if categories == "Night":
                            for key in dates[categories]:
                                if key == "LongPhrase":
                                    # print(dates[categories][key])
                                    # prints the longphrase description
                                    attach = dates[categories][key]
                                    nighttime.append(attach)
    # print(nighttime)

    counter = 0
    nighttime_rain = []      
    while counter < len(day_data):
        counter += 1       
        for days in day_data:
            for dates in days:
                for categories in dates:
                        if categories == "Night":
                            for key in dates[categories]:
                                if key == "RainProbability":
                                    # print(dates[categories][key])
                                    # prints the longphrase description
                                    attach = dates[categories][key]
                                    nighttime_rain.append(attach)
    # print(nighttime_rain)


    summary = (f"{len(min_temps)} Day Overview\n    The lowest temperature will be {format_temperature(convert_f_to_c(min(min_temps)))}, and will occur on {MinDictVal}.\n    The highest temperature will be {format_temperature(convert_f_to_c(max(max_temps)))}, and will occur on {MaxDictVal}.\n    The average low this week is {format_temperature(convert_f_to_c(calculate_mean(sum(min_temps),len(min_temps))))}.\n    The average high this week is {format_temperature(convert_f_to_c(calculate_mean(sum(max_temps),len(max_temps))))}.\n\n")
    print(summary)


    counter = 0 
    dailysummary = []
    while counter < len(day_data):
        counter += 1
        for days in day_data:
                    for dates in days:
                        for categories in dates:
                            if categories == "Date": 
                                attach = print(f"-------- {date_ISO} --------\nMinimum Temperature: {formatted_mintemps}\nMaxiumum Temperature: {formatted_maxtemps}\nDaytime: {daytime}\n      Chance of rain:  {daytime_rain}%\nNighttime: {nighttime}\n      Chance of rain:  {nighttime_rain}%\n\n")
                                dailysummary.append(attach)
print(dailysummary)


dailysummary = []
for x in range(len(date_ISO)):
    line1 = f"-------- {date_ISO} --------"
    dailysummary.append(line1)
    line2 = f"Minimum Temperature: {formatted_mintemps}"
    dailysummary.append(line2)
    line3 = f"Maximum Temperature: {formatted_maxtemps}"
    dailysummary.append(line3)
    line4 = f"Daytime: {daytime_rain}"
    dailysummary.append(line4)
    line5 = f"    Chance of rain:  {daytime_rain}%"
    dailysummary.append(line5)
    line6 = f"Nighttime: {nighttime}"
    dailysummary.append(line6)
    line7 = f"    Chance of rain:  {nighttime_rain}%"
    dailysummary.append(line7)
    line8 = "\n\n"
    dailysummary.append(line8)

print(dailysummary)






# day1 = (f"-------- {convert_date(date_ISO[0])} --------\nMinimum Temperature: {format_temperature(convert_f_to_c(min_temps[0]))}\nMaxiumum Temperature: {format_temperature(convert_f_to_c(max_temps[0]))}\nDaytime: {daytime[0]}\n      Chance of rain:  {daytime_rain[0]}%\nNighttime: {nighttime[0]}\n      Chance of rain:  {nighttime_rain[0]}%\n\n")
# print(day1)

# day2 = (f"-------- {convert_date(date_ISO[1])} --------\nMinimum Temperature: {format_temperature(convert_f_to_c(min_temps[1]))}\nMaxiumum Temperature: {format_temperature(convert_f_to_c(max_temps[1]))}\nDaytime: {daytime[1]}\n      Chance of rain:  {daytime_rain[1]}%\nNighttime: {nighttime[1]}\n      Chance of rain:  {nighttime_rain[1]}%\n\n")
# # print(day2)

# day3 = (f"-------- {convert_date(date_ISO[2])} --------\nMinimum Temperature: {format_temperature(convert_f_to_c(min_temps[2]))}\nMaxiumum Temperature: {format_temperature(convert_f_to_c(max_temps[2]))}\nDaytime: {daytime[1]}\n      Chance of rain:  {daytime_rain[2]}%\nNighttime: {nighttime[2]}\n      Chance of rain:  {nighttime_rain[2]}%\n\n")
# # print(day3)

# day4 = (f"-------- {convert_date(date_ISO[3])} --------\nMinimum Temperature: {format_temperature(convert_f_to_c(min_temps[3]))}\nMaxiumum Temperature: {format_temperature(convert_f_to_c(max_temps[3]))}\nDaytime: {daytime[3]}\n      Chance of rain:  {daytime_rain[3]}%\nNighttime: {nighttime[3]}\n      Chance of rain:  {nighttime_rain[3]}%\n\n")
# # print(day4)

# day5 = (f"-------- {convert_date(date_ISO[4])} --------\nMinimum Temperature: {format_temperature(convert_f_to_c(min_temps[4]))}\nMaxiumum Temperature: {format_temperature(convert_f_to_c(max_temps[4]))}\nDaytime: {daytime[4]}\n      Chance of rain:  {daytime_rain[4]}%\nNighttime: {nighttime[4]}\n      Chance of rain:  {nighttime_rain[4]}%\n\n")
# # print(day5)
