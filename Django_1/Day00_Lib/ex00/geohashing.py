import  sys
import antigravity

def check_date_format(date_format):
    parts = date_format.split('-')
    
    if len(parts) != 4:
        return False

    year, month, day, time = parts
    
    if len(year) != 4 or len(day) != 2 or len(month) != 2:
        return False
    
    try:
        float(time)
    except ValueError:
        return False
    return True
        
if __name__ == '__main__':
    try:
        longitude, latitude = float(sys.argv[1]), float(sys.argv[2])
        date_str = sys.argv[3]

        if not check_date_format(date_str):
            print("Invalid date format")
            exit()

        encode = date_str.encode('utf-8')
        print(antigravity.geohash(latitude, longitude, encode))
    except:
        print("Usage: python3 geohashing.py [longitude] [latitude] [date]")
        print("Example: python3 geohashing.py 37.421542 -122.085589 2005-05-26-10458.68")
        exit()
