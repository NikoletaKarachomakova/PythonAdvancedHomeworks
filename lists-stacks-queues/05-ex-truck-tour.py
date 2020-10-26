from collections import deque

count_stations = int(input())
station_balance = deque()

for _ in range(count_stations):
    data = list(map(int, input().split()))
    station_balance.append(data[0] - data[1])

total_fuel = 0
current_index = 0
inital_index = -1

while len(station_balance) > 0:
    inital_index += 1
    curr_station = station_balance[current_index]
    if curr_station < 0:
        station_balance.rotate(-1)
    else:
        total_fuel += curr_station
        for index in range(1, len(station_balance)):
            next_station = station_balance[index]
            total_fuel += next_station
            if total_fuel < 0:
                station_balance.rotate(-1)
                total_fuel = 0
                break
            else:
                if index == len(station_balance) - 1:
                    station_balance.clear()
                    print(f"{inital_index}")
                    break
