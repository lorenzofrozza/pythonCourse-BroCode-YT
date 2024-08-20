temp = 36
is_raining = False

# or = at least one condition must be True
# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

# and = both conditions must be True
# temp = 22
# is_sunny = True
#
# if temp >= 28 and is_sunny:
#     print("It is hot outside")
#     print("It is sunny!")
# elif temp <=  0 and is_sunny:
#     print("It is cold outside")
#     print("It is sunny!")
# elif 28 > temp > 0 and is_sunny:
#     print("It is warm outside")
#     print("It is sunny!")

# not = inverts the condition (not Flase, not True)
temp = 0
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY!")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY!")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY!")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is CLOUDY!")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside")
    print("It is CLOUDY!")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is CLOUDY!")
