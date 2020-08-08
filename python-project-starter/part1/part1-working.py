import json 
with open("data/forecast_5days_a.json") as json_file:
    forecast = json.load(json_file)

# print(forecast)

day_data = []
for keys, values in forecast.items():
    print(values)


#     for dailyforecast, daily_data in values:
#         for date, date_data in daily_data:
#             day_data.append(daily_data)
            

# print(day_data)


  # print(day_data)
        # day_data.append(keys)
        # print(day_data)
        # print(values)