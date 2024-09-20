import sys
# import antigravity

# def geohashing(longitude, latitude, date):
#     print(hash(date))

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print("Usage: python3 geohashing.py [latitude] [longitude] [date]")
        print("Example: python3 geohashin.py 37 -122 2005-05-26-10458.68")
        exit
    latitude = float(sys.argv[1])
    longitude = float(sys.argv[2])
    date = sys.argv[3]
    
    encode = date.encode('utf-8')
    # geo = antigravity.geohash(latitude, longitude, encode)
    print(latitude)
    