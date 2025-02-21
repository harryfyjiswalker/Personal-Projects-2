import math
#from itertools import product


def get_station_data(filename: str):
    with open(filename) as new_file:
        # content = new_file.read()
        # print(content)
        stations = {}
        lines = 0
        for line in new_file:
            parts = line.split(";")
            names = parts[3]
            if parts[0] != "Longitude":
                stations[names] = (float(parts[0]),float(parts[1]))
            lines += 1
        return stations

def distance(stations:dict, station1: str, station2:str):
    longitude1 = float(stations[station1][0])
    longitude2 = float(stations[station2][0])
    latitude1 = float(stations[station1][1])
    latitude2 = float(stations[station2][1])
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2    
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    distances = []
    howfar = 0
    for a,b in stations.items():
        for k,v in stations.items():
            station1 = a
            station2 = k
            distancebetween = distance(stations, station1, station2)
            tuple1 = station1, station2, distancebetween
            distances.append(tuple1)
    for i in range(len(distances)):
        if distances[i][2] > howfar:
            howfar = distances[i][2]
        else:
            pass
    for i in range(len(distances)):
        if distances[i][2] == howfar:
            return distances[i]



if __name__ == "__main__":
    stations = {}
    stations = get_station_data("stations1.csv")
    # print(stations)
    # print(distance(stations, "Designmuseo", "Hietalahdentori"))
    print(greatest_distance(stations))
