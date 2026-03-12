import pandas as pd
import random

models = [
"Tesla Model 3",
"Tesla Model Y",
"Nissan Leaf",
"Hyundai Kona",
"Tata Nexon EV",
"MG ZS EV",
"Mahindra XUV400",
"BYD Atto 3"
]

cities = [
"Delhi",
"Mumbai",
"Bangalore",
"Pune",
"Hyderabad",
"Chennai",
"Kolkata",
"Ahmedabad"
]

data = []

for i in range(2000):

    model = random.choice(models)
    battery = random.randint(30, 90)
    range_km = random.randint(250, 600)
    charging_time = random.randint(30, 90)
    charging_power = random.randint(25, 150)
    location = random.choice(cities)
    charging_cost = random.randint(200, 600)

    data.append([
        model,
        battery,
        range_km,
        charging_time,
        charging_power,
        location,
        charging_cost
    ])

df = pd.DataFrame(data, columns=[
"Vehicle_Model",
"Battery_Capacity_kWh",
"Range_km",
"Charging_Time_min",
"Charging_Power_kW",
"Location",
"Charging_Cost"
])

df.to_csv("ev_data.csv", index=False)

print("Dataset generated with", len(df), "rows")