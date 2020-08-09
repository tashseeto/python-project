import json 
with open("data/forecast_5days_a.json") as json_file:
    forecast = json.load(json_file)
# print(forecast)


day_data = []
for category, categorydata in forecast.items():
    if category == "DailyForecasts":
        day_data.append(categorydata)
# print(day_data)

 
date_ISO = []
for days in day_data:
    # print(days) prints all days
    for dates in days:
        # print(dates) prints days separately
        for categories in dates:
            # relates to key in date dictionary
            if categories == "Date":
                attach = dates[categories]
#                 date_ISO.append(attach)   
# print(date_ISO)

min_temps = []
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
                            # print(dates[categories][key])
                            # prints the longphrase description
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
                            # print(dates[categories][key])
                            # prints the longphrase description
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
                            # print(dates[categories][key])
                            # prints the longphrase description
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
                            # print(dates[categories][key])
                            # prints the longphrase description
                            attach = dates[categories][key]
                            nighttime_rain.append(attach)
# print(nighttime_rain)
