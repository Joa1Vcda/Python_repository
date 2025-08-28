car_speed = 61
car_location = 100

RADAR_LOCATION = 100
RADAR_RANGE = 1
RADAR_MAX_SPEED = 60

RANGE_1 = RADAR_LOCATION - RADAR_RANGE
RANGE_2 = RADAR_LOCATION + RADAR_RANGE

car_speed_2 = input("car speed: ")
car_location_2 = input("car locantion: ")

"""try method"""

try:
    car_location_float = float(car_location_2)
    car_in_radar = car_location_float >= RANGE_1 and car_location_float <= RANGE_2

    car_speed_float = float(car_speed_2)
    test_1 = car_speed_float > RADAR_MAX_SPEED
    test_2 = car_speed_float <= RADAR_MAX_SPEED

    fined_in_radar_range = car_in_radar and test_1
    not_fined_in_radar = car_in_radar and test_2

    if car_in_radar:
        print("car in radar zone")

    if fined_in_radar_range:
        print("car fined in radar zone")
    elif not_fined_in_radar:
        print("car was not fined")
    else:
        print(
            "car outside the radar zone,impossible to verify possible fine,try car location between 99-101"
        )
except:
    print("car locantion and car speed need to be a digit,try again")

"""if method"""

car_in_radar = car_location >= RANGE_1 and car_location <= RANGE_2

test_1 = car_speed > RADAR_MAX_SPEED
test_2 = car_speed <= RADAR_MAX_SPEED

fined_in_radar_range = car_in_radar and test_1
not_fined_in_radar = car_in_radar and test_2

if car_in_radar:
    print("car in radar zone")

if fined_in_radar_range:
    print("car fined in radar zone")
elif not_fined_in_radar:
    print("car not fined in radar zone")
else:
    print(
        "car outside the radar zone,impossible to verify possible fine,try car location between 99-101"
    )
