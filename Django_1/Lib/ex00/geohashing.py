#!/bin/python3
import antigravity
import sys

if __name__ == '__main__':
    try:
        if len(sys.argv) != 4:
            print("Usage: python3 geohashing.py [latitude] [longitude] [date]")
            print("Example: python3 geohashin.py 37 -122 2005-05-26-10458.68")
            exit

        latitude = float(sys.argv[2])
        longitude = float(sys.argv[3])
        date = sys.argv[4]
        
        encode = date.encode('utf-8')
        geo = antigravity.geohash(latitude, longitude, encode)
        print(geo)
    except IndexError as e:
        print(e)
        
    