import googlemaps 
import os 
import numpy as np
import pandas as pd
import csv
import datetime

path = 'C:/Users/Declan/Desktop/Python/OD_Distance'
os.chdir(path)
cwd = os.getcwd()
print(cwd)
files = os.listdir(path)


OD = pd.read_csv(files[2])
OD = OD.set_index('TCode')
gmaps = googlemaps.Client('AIzaSyCz5TdwmyCNSi_dvG7MGBfKEYR35bMAcT4')

OD[['ox','oy']]
OD['origin'] = [[OD['ox'][x],OD['oy'][x]] for x in range(OD.shape[0])]
OD['dest'] = [[OD['dx'][x],OD['dy'][x]] for x in range(OD.shape[0])]

OD_test = OD.iloc[:2]

lat_long = {
        "lat" : '44.998687',
        "lng" : '-93.255739'
        }

 
dest_lat_long = {
        "lat" : '44.979409', 
        "lng" : '-93.266648'
        }

print(lat_long)

#dir = gmaps.directions(origin = OD_test['origin'][0],
#                       destination = OD_test['dest'][0],
#                       mode = 'transit',
#                       transit_mode = 'bus')

DT = datetime.strptime('2018-9-19 07:45', '%Y-%m-%d %H:%M')
				  
results = []
for x in range(OD_test.shape[0]):
           direct = gmaps.directions(origin = OD_test['origin'][x],
                       destination = OD_test['dest'][x],
                       mode = 'transit',
                       transit_mode = 'bus',
					   arrival_time = DT)
           results.append(direct)

results[1][0]['legs'][0]['steps'][1]['html_instructions']
results[1][0]['legs'][0]['steps'][1]['duration']['value']
results[1][0]['legs'][0]['departure_time']

#for idx, val in enumerate(x):
#    print(val['html_instructions'],
#          ', Duration (sec):',
#          val['duration']['value'])

#x = dir[0]['legs'][0]['steps']

arrival = []
departure = []
for idx, val in enumerate(results):
	r = val
	for c, value in enumerate(r):
		x = val[0]['legs'][0]['departure_time']['text']
		y = val[0]['legs'][0]['arrival_time']['text']
	departure.append(x)
	arrival.append(y)
	del(r)


res = []
for idx, val in enumerate(results):
    x = val[0]['legs'][0]['steps']
    res.append(x)

duration = []
direction = []
route = []
for idx, val in enumerate(res):
    r = val
    dur_list = []
    dir_list = []
    route_list = []
    for c, value in enumerate(r):
        dur = value['duration']['value']
        dir = value['html_instructions']
        if value['travel_mode'] == 'TRANSIT':
            bus_no = value['transit_details']['line']['short_name']
            route_list.append(bus_no)
        else:
           route_list.append('Walk')
        dur_list.append(dur)
        dir_list.append(dir)
    duration.append(dur_list)
    direction.append(dir_list)
    route.append(route_list)

OD_test['Directions'] = [direction[x] for x in range(OD_test.shape[0])]
OD_test['Durations_sec'] = [duration[x] for x in range(OD_test.shape[0])]
#OD_test['Bus_route'] = [route[x] for x in range(OD_test.shape[0])]
OD_test['Final_Arrival'] = [arrival[x] for x in range(OD_test.shape[0])]
OD_test['Initial_Departure'] = [departure[x] for x in range(OD_test.shape[0])]
OD_test['Total_Trip_Duration_mins'] = [(datetime.strptime(OD_test['Final_Arrival'][x], '%H:%M%p') 
									  - datetime.strptime(OD_test['Initial_Departure'][x], '%H:%M%p'))
									 .seconds/60 
									 for x in range(OD_test.shape[0])]

results[0][0]['legs'][0]['steps'][3]['travel_mode']
results[0][0]['legs'][0]['steps'][3]['transit_details']['line']['short_name']

OD_test.to_csv('OD_test.csv')

OD_t = OD_test[['Name','Durations','Directions']]

s = OD_t.apply(lambda x: pd.Series(x['Durations']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'Duration (sec)'
s = s.reset_index()
t = OD_t.apply(lambda x: pd.Series(x['Directions']),axis=1).stack().reset_index(level=1, drop=True)
t.name = 'Direction'
t = t.reset_index().drop(['TCode'], axis = 1)
merge = s.join(t)

merge = merge.set_index('TCode').join(OD_test[['Name','Final_Arrival','Initial_Departure','Total_Trip_Duration_mins']])

merge.to_csv('OD_t.csv')