#!/usr/bin/env python3

import requests
import datetime
# $ python3 -m pip install geopy
from geopy.geocoders import Nominatim

# initiating ISS API
API="http://api.open-notify.org/iss-now.json"

# initiating Nominatim API
geolocator=Nominatim(user_agent="geoapiExercises")

def main():
    resp=requests.get(API).json()
    # print(resp)
    
    position=resp['iss_position']
    # print(position) # returns lat and lon
    
    latitude=position['latitude']
    longitude=position['longitude']
    
    # use geopy to get city/country by lat and long
    location = geolocator.reverse(latitude+","+longitude)
    # print(location)

    epoch_time=resp['timestamp']
    # convert epoch time to date time (import, then datetime.datetime.fromtimestamp(epoch)
    date_time=datetime.datetime.fromtimestamp(epoch_time)
    # print(epoch_time)
    # print(date_time)

    print("CURRENT LOCATION OF THE ISS")
    print(f"Timestamp: {date_time}")
    print(f"Lon: {position['longitude']}")
    print(f"Lat: {position['latitude']}")
    print(f"City/Country: {location}")

if __name__=="__main__":
    main()
