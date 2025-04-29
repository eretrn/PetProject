from pg_func import insert_schedule, insert_stations, insert_days
from pars import works
import random
file = open('stops.txt', 'r', encoding='UTF-8')
input = eval(file.read())
insert_days(6522, works)

"""
for i in input:
    id = i['id']
    arrive_time = i['arrive_time']
    station_number = i['station_number']
    insert_schedule(id, arrive_time, station_number)
    station_name = i['station_name']
    #insert_stations(id, station_name)

file.close()
"""