import os
import math
import csv

populartimes =
[
    {
    "id": "ChIJSYuuSx9awokRyrrOFTGg0GY",
    "name": "Gran Morsi",
    "address": "22 Warren St, New York, NY 10007, USA",
    "types": [
        "restaurant",
        "food",
        "point_of_interest",
        "establishment"
    ],
    "coordinates": {
        "lat": 40.71431500000001,
        "lng": -74.007766
    },
    "rating": 4.4,
    "rating_n": 129,
    "international_phone_number": "+1 212-577-2725",
    "time_spent": [
        90,
        180
    ],
    "current_popularity": 33,
    "populartimes": [
        {
        "name": "Monday",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 19, 20, 17, 0, 0, 20, 28, 26, 18, 10, 6, 0
        ]
        },
        {
        "name": "Tuesday",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 27, 19, 10, 0, 0, 34, 42, 42, 35, 26, 15, 0
        ]
        },
        {
        "name": "Wednesday",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 34, 23, 13, 0, 0, 36, 46, 47, 39, 26, 13, 0
        ]
        },
        {
        "name": "Thursday",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 42, 42, 28, 0, 0, 59, 61, 46, 39, 32, 20, 0
        ]
        },
        {
        "name": "Friday",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 44, 40, 28, 0, 0, 70, 96, 100, 80, 48, 22, 0
        ]
        },
        {
        "name": "Saturday",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 42, 48, 47, 36, 21, 0
        ]
        },
        {
        "name": "Sunday",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 34, 34, 28, 21, 10, 0
        ]
        }
    ],
    "time_wait": [
        {
        "name": "Monday",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 0, 0, 0, 0, 15, 15, 15, 0, 15, 15, 0
        ]
        },
        {
        "name": "Tuesday",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 0
        ]
        },
        {
        "name": "Wednesday",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 0
        ]
        },
        {
        "name": "Thursday",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 0
        ]
        },
        {
        "name": "Friday",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 15, 0
        ]
        },
        {
        "name": "Saturday",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 15, 0
        ]
        },
        {
        "name": "Sunday",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 15, 0, 0, 0
        ]
        }
    ]
    }

]

populartimes_keys = dict.keys(populartimes[0])

keys = ['id', 'name', 'address', 'types', 'coordinates', 'rating', 'rating_n', 'populartimes',
        'popularity', 'current_popularity', 'time_wait', 'time_spent', 'phone']

weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
weekdays_seperated = []
for day in weekdays:
    for i in range(0,24):
        weekdays_seperated.append(day + str(i))

# Keys for CSV header
allkeys = keys[0:4] + ['lat'] + ['lng'] + keys[5:7] + keys[8:12] + weekdays_seperated
# print(allkeys)
# print(weekdays_seperated)
# print(allkeys)


populartimes_updated = []
for row in populartimes:
    row_dict = {}
    for key in row:
        if key == 'coordinates':
            row_dict['lat'] = row[key]['lat']
            row_dict['lng'] = row[key]['lng']
            # print('lat', row[key]['lat'])
            # print('lng', row[key]['lng'])
        elif key == 'populartimes':
            i = 0
            for day in row[key]:
                hour24 = day['data']
                for hour in hour24:
                    row_dict[weekdays_seperated[i]] = hour
                    # print(weekdays_seperated[i],hour)
                    i = i + 1
        else:
            row_dict[key] = row[key]
            # print(key, row[key])
    # print(row_dict)
    populartimes_updated.append(row_dict)
    # print(populartimes_updated)

print(populartimes_updated)

with open('populartimes.csv', 'w', newline='') as csvfile:
    fieldnames = allkeys
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in populartimes_updated:
        # print(row)
        writer.writerow(row)