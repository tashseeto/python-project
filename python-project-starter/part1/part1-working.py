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
count = 0
for days in day_data[0:4]:
    print(days)
   






# count = 0
# for days, values in day_data[0][0]:
#     if days == "Date":
#         date_ISO.append(values)
#         count += 1
    # this prints all dates
    
# print(date_ISO)
    
    # for key in days[0]:
    #     if key == "Date":
    #         date_ISO.append(days[0][key])

# #         elif key in days[1]:
#             if key == "Date":
#                 date_ISO.append(days[1][key])

#         # print(key, days[0][key])
# print(date_ISO)
            # above prints keys and values for fri 19 yippee!

# , days[1], days[2], days[3], days[4]






    # print(days[0])
    #  days[1], days[2], days[3], days[4])
    # this prints all dictionaries in list

    # for keys in days[0]:
    #     print (keys)
    #     above prints the keys for Fri 19

    # for values in days[0]:
    #     print(days[0][values])
        # above prints values for Fri 19
        

# print(daily_info)