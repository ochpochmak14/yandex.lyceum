from datetime import datetime, timedelta

FORMAT_TIME = '%d.%m.%Y %H:%M'
battery_range = int(input())
charging_duration = int(input())
average_speed = int(input())
departure_input = input()
departure_time = datetime.strptime(departure_input, FORMAT_TIME)
checkpoints = list(map(int, input().split()))
checkpoints.insert(0, 0)

remaining_charge = battery_range
charging_stations = [0]

for idx in range(len(checkpoints) - 1):
    distance_gap = checkpoints[idx + 1] - checkpoints[idx]
    if remaining_charge < distance_gap:
        remaining_charge = battery_range
        charging_stations.append(idx)
    remaining_charge -= distance_gap

time_log = {}
current_time = departure_time

for j in range(1, len(charging_stations)):
    prev_idx = charging_stations[j - 1]
    next_idx = charging_stations[j]
    travel_distance = checkpoints[next_idx] - checkpoints[prev_idx]
    travel_time = travel_distance / average_speed * 60

    if j > 1:
        travel_time += charging_duration

    time_increment = timedelta(minutes=travel_time)
    current_time += time_increment
    time_log[next_idx] = current_time

for station, time in time_log.items():
    print(f'{station} {time.strftime(FORMAT_TIME)}')
