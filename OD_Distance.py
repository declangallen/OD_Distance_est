import googlemaps 
import os 
import numpy as np
import pandas as pd
import csv

path = 'C:/Users/Declan/Desktop/Python/OD_Distance'
os.chdir(path)
cwd = os.getcwd()
print(cwd)
files = os.listdir(path)


OD = pd.read_csv(files[2])
OD = OD.set_index('TCode')
gmaps = googlemaps.Client('AIzaSyASwfwu2HvXzn0puz-GmFI_nLeOgRgJ4ns')

OD[['ox','oy']]
OD['origin'] = [[OD['ox'][x],OD['oy'][x]] for x in range(OD.shape[0])]
OD['dest'] = [[OD['dx'][x],OD['dy'][x]] for x in range(OD.shape[0])]

OD_test = OD.iloc[:2]

lat_long = {
        "lat" : '44.902000',
        "lng" : '-93.393530'
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


results = []
for x in range(OD_test.shape[0]):
           direct = gmaps.directions(origin = OD_test['origin'][x],
                       destination = OD_test['dest'][x],
                       mode = 'transit',
                       transit_mode = 'bus')
           results.append(direct)

results[1][0]['legs'][0]['steps'][2]['html_instructions']


#for idx, val in enumerate(x):
#    print(val['html_instructions'],
#          ', Duration (sec):',
#          val['duration']['value'])

#x = dir[0]['legs'][0]['steps']

res = []
for idx, val in enumerate(results):
    x = results[idx][0]['legs'][0]['steps']
    res.append(x)

duration = []
direction = []
for idx, val in enumerate(res):
    r = val
    dur_list = []
    dir_list= []
    for c, value in enumerate(r):
        dur = value['duration']['value']
        dir = value['html_instructions']
        dur_list.append(dur)
        dir_list.append(dir)
    duration.append(dur_list)
    direction.append(dir_list)

OD_test['Directions'] = [direction[x] for x in range(OD_test.shape[0])]
OD_test['Durations'] = [duration[x] for x in range(OD_test.shape[0])]

results[0][0]['legs'][0]['steps'][3]['travel_mode']
results[0][0]['legs'][0]['steps'][3]['transit_details']['line']['short_name']

OD_test.to_csv('OD_test.csv')