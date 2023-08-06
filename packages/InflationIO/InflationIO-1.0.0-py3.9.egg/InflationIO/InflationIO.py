# Libraries
import requests
import json
import datetime
import Adafruit_IO as io
from time import sleep

# Setup
# Adafruit IO
ADAFRUIT_IO_KEY = 'c36f59e54ca740759d5274d8e5c8cabb'
ADAFRUIT_IO_USERNAME = 'dsblock19'
aio = io.Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
# Feeds
Inflationio = aio.feeds('investments.inflation')

# Constants and Variables
T = 1
T2 = 10
Inflation = 0
CurrentCPI = 0
OldCPI = 267.054 # April 2021
month = 0
day = 0
year = 0

# BLS API
headers = {'Content-type': 'application/json'}

dt = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
print('Program Begins at ' + str(dt))

def GrabData(year):
    try:
        # Pull Data
        print('\nPulling Data')
        data = json.dumps({"seriesid": ['CUUR0000SA0','SUUR0000SA0'],"startyear":year, "endyear":year})
        p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
        json_data = json.loads(p.text)

        # Calculate Inflation
        CurrentCPI = json_data['Results']['series'][0]['data'][0]['value']
        CurrentCPI = float(CurrentCPI)
        Inflation = ((CurrentCPI - OldCPI) / OldCPI) * 100
        print('\nCurrent CPI: ' + str(CurrentCPI))
        print('Benchmark CPI: ' + str(OldCPI))
        print('Inflation: ' + str(Inflation))

        # Send to Adafruit IO
        aio.send_data(Inflationio.key, Inflation)

        print('\nDone')
        sleep(3600 * T)
    except (Exception) as e:
        print('\nError - ', e)

def InflationIO():
    print('Start')
    while True:

        # Date
        year = datetime.datetime.now().strftime('%Y')
        month = datetime.datetime.now().strftime('%m')
        day = datetime.datetime.now().strftime('%d')
        hour = datetime.datetime.now().strftime('%H')

        if int(month) == 1:
            year = int(year) - 1

        if (int(day) == 10) and (int(hour) == 12):
            GrabData(year)
        elif (int(day) == 13) and (int(hour) == 12):
            GrabData(year)
        elif (int(day) == 28) and (int(hour) == 12):
            GrabData(year)
        else:
            pass

        sleep(60 * T2)
