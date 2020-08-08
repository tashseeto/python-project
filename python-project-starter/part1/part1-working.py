import json 
with open("data/forecast_5days_a.json") as json_file:
    forecast = json.load(json_file)

# print(forecast)

day_data = []
for category, categorydata in forecast.items():
    if category == "DailyForecasts":
        day_data.append(categorydata)
# print(day_data)
  
daily_info = []
for days in day_data:
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