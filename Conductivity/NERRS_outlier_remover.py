# Program is used to remove outliers from NERRS Metoxit Point Data
# The conditons for classifying a point as an outlier is as follows:
# For every point, the difference between two consecutive points must not be more than 5 PSU on both sides
# -If the difference on one side is greater than 5 PSU, but not the other, it will not be counted as an outlier
# -Stop in break of time frame must not be greater than 2 hours

import pandas as pd
import os
from datetime import datetime as dt
import datetime

def timeWithinRange (time_a, time_b):
    delta = time_a-time_b
    if delta <= 2 and delta >= -2:
        return True
    else:
        return False

def NERRS_sal_grapher(file_name, location):
    #__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    #raw_data_folder = os.path.join(__location__, '')
    #raw_data_location_folder = os.path.join(raw_data_folder, location)

    #adjusted_data_folder = os.path.join(__location__, '')

    # Opens NERRS raw data file
    NERRS_data = pd.read_csv(os.path.join(location, file_name))

    # Goes through entire NERRS data file
    # For each point (index):
    #   date_current = NERRS_data.loc[i, "Datetime_Adjusted_UTC+1"]
    #   salinity_current = NERRS_data.loc[i, "Salinity"]
    # Checks point right before it:
    # if i != 0:
    # (Index-1): 
    #   date_before = NERRS_data.loc[i-1, "Datetime_Adjusted_UTC+1"]
    #   salinity_before = NERRS_data.loc[i-1, "Salinity"]
    #   - Is the time in between greater than 2 hours?
    #   time_valid_left = timeWithinRange(date_current, date_before)
    # 
    # Checks point right after it
    # if i != (len(NERRS_data)-1)
    # 
    for i in range(len(NERRS_data)):
        salinity = condSalConv(eureka_data.loc[i, "Conductivity"], eureka_data.loc[i, "Temperature"])

    def NERRS_time_converter(date_time):
        
        date = date_time.split(" ")[0]
        time = date_time.split(" ")[1]
        m1, d1, y1 = [int(date_part) for date_part in date.split("/")]
        date1 = dt(y1, m1, d1)
        converted_time = dt.strptime(time, "%H:%M")
        datetime_dt_est = dt.combine(date1, converted_time.time())

        datetime_dt_utc = datetime_dt_est + datetime.timedelta(hours=6)

        return datetime_dt_utc

    nerrs_datetime_list = []
    for value in NERRS_data["DateTimeStamp"]:
        nerrs_datetime_list.append(NERRS_time_converter(value))


    NERRS_data["Datetime_Adjusted_UTC+1"] = nerrs_datetime_list

    print(NERRS_data)


    # Updates data file name to reflect the outliers haven been taken out
    file_name_adjusted = file_name + "_OR.csv"

    NERRS_data.to_csv(os.path.join(location ,file_name_adjusted))


# Metoxit Point 2020
NERRS_sal_grapher("wqbmpwq2020.csv", "Metoxit_Point\\")

# Metoxit Point 2021
NERRS_sal_grapher("wqbmpwq2021.csv", "Metoxit_Point\\")

# Metoxit Point 2022
NERRS_sal_grapher("wqbmpwq2022.csv", "Metoxit_Point\\")

# Metoxit Point 2023
NERRS_sal_grapher("wqbmpwq2023.csv", "Metoxit_Point\\")




