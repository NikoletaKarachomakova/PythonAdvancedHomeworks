from collections import deque

green_light = int(input())
free_window = int(input())
command = input()

is_there_a_crash = False
cars = deque()
total_passed_cars = 0

while command != "END":
    green_pass = green_light
    if command != "green":
        cars.append(command)

    else:
        while len(cars) != 0:
            current_car = cars[0]
            current_length = len(current_car)

            if green_pass + free_window < current_length:
                is_there_a_crash = True
                hit_letter = current_car[green_pass + free_window]
                print("A crash happened!")
                print(f"{current_car} was hit at {hit_letter}.")
                break

            total_passed_cars += 1
            green_pass -= current_length
            cars.popleft()
            if green_pass <= 0:
                break

        if is_there_a_crash:
            break

    command = input()

if not is_there_a_crash:
    print("Everyone is safe.")
    print(f"{total_passed_cars} total cars passed the crossroads.")