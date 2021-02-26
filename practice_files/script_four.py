import numpy as np
import sys
from datetime import datetime
from datetime import timedelta
#
# def toDate(x):
#     return datetime.strptime(str(x), "%Y-%m-%d")
#
# date, maxTemp, minTemp = np.loadtxt("/home/koshta/Documents/coding/greatLearnings/resources/data/archive/GlobalTemperatures.csv",
#                                       delimiter=",",
#                                       unpack=True,
#                                       skiprows=1,
#                                       usecols=(0, 3, 5),
#                                       dtype=np.dtype([('date', 'datetime64[s]'), ('maTemp', np.float64), ('minTemp', np.float64)]),
#                                       converters={0 : lambda x : x.decode("utf-8"), 3 : lambda x : float(x.strip() or np.nan), 5 : lambda x : float(x.strip() or np.nan)})
#
# print("Number of observations: ", len(date))
# print("The minimum temperature: ", np.nanmin(minTemp))
# print("The maximum temperature: ", np.nanmax(maxTemp))

dateOne, avgTemp, city, country = np.loadtxt("/home/koshta/Documents/coding/greatLearnings/resources/data/archive/GlobalLandTemperaturesByCity.csv",
                                      delimiter=",",
                                      unpack=True,
                                      skiprows=1,
                                      usecols=(0, 1, 2, 3),
                                      dtype=np.dtype([("dateOne", "datetime64[s]"), ("avgTemp", np.float64), ("City", str, 25), ("Country", str, 25 )]),
                                      converters={0 : lambda x : x.decode("utf-8"), 1 : lambda x : float(x.strip() or np.nan)})

print("Number of observations: ", len(dateOne))
print("The minimum temperature: ", np.nanmin(avgTemp))
print("The maximum temperature: ", np.nanmax(avgTemp))
print(len(avgTemp[avgTemp<0])/len(avgTemp))

print(4)