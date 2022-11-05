#Python script to load Bhopal wheather data into MySQL table and then print details as required.

#We have used api from visualcrossing.com to get updated wheather data


import urllib.request
import json
import mysql.connector
from datetime import datetime

# This is the core of our weather query URL
BaseURL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/'

ApiKey='TD5A6DRP9YPHUDZ3MEG33LJRF'

#UnitGroup sets the units of the output - us or metric
UnitGroup='us'

#Locations for the weather data. Multiple locations separated by pipe (|)
Locations='Bhopal,IN'

#FORECAST or HISTORY
QueryType='FORECAST'

#1=hourly, 24=daily
AggregateHours='24'

#Params for history only
StartDate = ''
EndDate=''

# Set up the specific parameters based on the type of query
DateParam=None
if QueryType == 'FORECAST':
    print(' - Fetching forecast data')
    QueryParams = 'forecast?aggregateHours=' + AggregateHours + '&unitGroup=' + UnitGroup + '&shortColumnNames=true'
else:
    print(' - Fetching history for date: ', DateParam)

    # History requests require a date.  We use the same date for start and end since we only want to query a single date in this example
    QueryParams = 'history?aggregateHours=' + AggregateHours + '&unitGroup=' + UnitGroup +'&startDateTime=' + StartDate + 'T00%3A00%3A00&endDateTime=' + EndDate + 'T00%3A00%3A00'

Locations='&locations='+Locations

ApiKey='&key='+ApiKey

# Build the entire query
URL = BaseURL + QueryParams + Locations + ApiKey+"&contentType=json"

print(' - Running query URL: ', URL)
print()


response = urllib.request.urlopen(URL)
data = response.read()
weatherData = json.loads(data.decode('utf-8'))

errorCode=weatherData["errorCode"] if 'errorCode' in weatherData else 0

if (errorCode>0):
    print("An error occurred retrieving the data:"+weatherData["message"])
    exit("Script terminated")
    
print( "\nConnecting to mysql database")
mysql_password=input("\nEnter your MySQL Login Password : ")
cnx = mysql.connector.connect(host='localhost',
    user='root',
    passwd=mysql_password,
    database='weather_data_schema')

cursor = cnx.cursor()

# In this simple example, clear out the existing data in the table

delete_weather_data=("TRUNCATE TABLE `weather_data_schema`.`weather_data`")
cursor.execute(delete_weather_data)
cnx.commit()

# Create an insert statement for inserting rows of data 
insert_weather_data = ("INSERT INTO `weather_data_schema`.`weather_data`"
                "(`address`,`latitude`,`longitude`,`datetime`,`maxt`,`mint`,`temp`,`precip`,`wspd`,`wdir`,`wgust`,`pressure`)"
                "VALUES (%(address)s, %(latitude)s, %(longitude)s, %(datetime)s, %(maxt)s,%(mint)s, %(temp)s, %(precip)s, %(wspd)s, %(wdir)s, %(wgust)s, %(pressure)s)")

# Iterate through the locations
locations=weatherData["locations"]
for locationid in locations:  
    location=locations[locationid]
    # Iterate through the values (values are the time periods in the weather data)
    for value in location["values"]:
        data_wx = {
        'address': location["address"],
        'latitude': location["latitude"],
        'longitude': location["longitude"],
        'datetime': datetime.utcfromtimestamp(value["datetime"]/1000.),
        'maxt':  value["maxt"] if 'maxt' in value else 0,
        'mint': value["mint"] if 'mint' in value else 0,
        'temp': value["temp"],
        'precip': value["precip"],
        'wspd': value["wspd"],
        'wdir': value["wdir"],
        'wgust': value["wgust"],
        'pressure': value["sealevelpressure"]
        }
        cursor.execute(insert_weather_data, data_wx)
        cnx.commit()
               
cursor.close() 
cnx.close()
print( "Database connection closed")

print( "Wheather Data Inserted to MySQL from API")



try:
    connection =mysql.connector.connect(host='localhost',
    user='root',
    passwd=mysql_password,
    database='weather_data_schema')
    
    sql_select_Query = "select * from `weather_data`"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of data in table: ", cursor.rowcount)

    print("\nPrinting each data")
    for row in records:
        print("Address = ", row[1], )
        print("Max Temp = ", row[5])
        print("Min Temp  = ", row[6])
        print("Temp  = ", row[7], "\n")

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")