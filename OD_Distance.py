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

dir = gmaps.directions(origin = OD_test['origin'][0],
                       destination = OD_test['dest'][0],
                       mode = 'transit',
                       transit_mode = 'bus')


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

p = []
for idx, val in enumerate(res):
    r = val
    dat = []
    for c, value in enumerate(r):
        #d = value['duration']['value']
        d = value['html_instructions']
        dat.append(d)
    p.append(dat)


OD_test['Directions'] = [p[x] for x in range(OD_test.shape[0])]