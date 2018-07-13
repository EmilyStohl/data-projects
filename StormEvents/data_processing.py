# -*- coding: utf-8 -*-

# This file was used to combine yearly files into one file for fatalities, locations, and details.
# Only essential columns were selected from each file.
# CSV files can be found at https://www.ncdc.noaa.gov/stormevents/ftp.jsp



import os
import pandas as pd

details_columns = ['BEGIN_DATE_TIME','END_DATE_TIME','EPISODE_ID','EVENT_ID',
 'STATE','YEAR', 'MONTH_NAME','EVENT_TYPE','WFO','INJURIES_DIRECT',
 'INJURIES_INDIRECT','DEATHS_DIRECT','DEATHS_INDIRECT','DAMAGE_PROPERTY',
 'DAMAGE_CROPS','MAGNITUDE','MAGNITUDE_TYPE','TOR_F_SCALE',
 'TOR_LENGTH','TOR_WIDTH','TOR_OTHER_WFO']
details = pd.DataFrame(columns = details_columns)

fatalities_columns = ['FATALITY_ID', 'FATALITY_DATE', 'EVENT_ID','FATALITY_TYPE', 
 'FATALITY_AGE', 'FATALITY_SEX', 'FATALITY_LOCATION']
fatalities = pd.DataFrame(columns = fatalities_columns)

locations_columns = ['EPISODE_ID','EVENT_ID','LOCATION_INDEX','LATITUDE','LONGITUDE']
locations = pd.DataFrame(columns = locations_columns)

narrative_columns = ['EPISODE_ID', 'EVENT_ID', 'EPISODE_NARRATIVE', 'EVENT_NARRATIVE']
narrative = pd.DataFrame(columns = narrative_columns)



for filename in os.listdir(r".\csvfiles"):
    
    if filename[0:10] == 'StormEvent':
        current_df = pd.read_csv(".\\csvfiles\\" + filename)
                   
        if filename[12]== 'd': # details & narratives
            details  = details.append(current_df[details_columns])
            narrative = narrative.append(current_df[narrative_columns])

        elif filename[12] == 'f': # fatalities
            fatalities = fatalities.append(current_df[fatalities_columns])
                     
        elif filename[12] == 'l':  # locations
            locations = locations.append(current_df[locations_columns])

   
details.to_csv('details.csv')
fatalities.to_csv('fatalities.csv')
locations.to_csv('locations.csv')
narrative.to_csv('narrative.csv', sep='|') # different seperator used because 
# narrative entries contain periods and commas

