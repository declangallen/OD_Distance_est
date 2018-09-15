import googlemaps 
import os 
import numpy as np
import pandas as pd

path = 'C:/Users/Declan/Desktop/Python/OD_Distance'
os.chdir(path)
cwd = os.getcwd()
print(cwd)
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
print(onlyfiles)

OD = pd.read_csv(onlyfiles[1])
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

results = []
for x in range(OD_test.shape[0]):
           direct = gmaps.directions(origin = OD_test['origin'][x],
                       destination = OD_test['dest'][x],
                       mode = 'transit',
                       transit_mode = 'bus')
           results.append(direct)

x = dir[0]['legs'][0]['steps']
for idx, val in enumerate(x):
    print(val['html_instructions'],
          ', Duration (sec):',
          val['duration']['value'])

x = dir[0]['legs'][0]['steps']

directions = []
for idx, val in enumerate(x):
    direct = val['html_instructions']
    directions.append(direct)

durations = []
for idx, val in enumerate(x):
    durat = val['duration']['value']
    durations.append(durat)

