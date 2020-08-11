import csv
import json
import pandas as pd

with open("urzad_miasta.csv", "r") as f:
    x = pd.read_csv(f, delimiter=";")

print(x.where(x["NAZWA"] == "Toruń").dropna())
# with open("miasta.json", "r") as f:
#     miasta_JSON = json.load(f)

# with open("miasta.csv", "w") as f:
#     writer = csv.writer(f)
#     writer.writerow("name", "totalPopulation", "menPopulation", "womenPopulation", "powiat", "wojewodztwo", "latitude", "longitude", "area", "plates" ,"president")
#     for miasto in miasta_JSON:
#         for key in miasto:
#             print(key)
#         break