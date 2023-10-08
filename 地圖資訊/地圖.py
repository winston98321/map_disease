'''import plotly.express as px

df = px.data.election()
geojson = px.data.election_geojson()

fig = px.choropleth_mapbox(df, geojson=geojson, color="winner",
                           locations="district", featureidkey="properties.district",
                           center={"lat": 23.973875, "lon": 120.982024},
                           mapbox_style="carto-positron", zoom=9)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
'''
'''
# fake data
d = {'Date': ['2008061612', '2008061612', '2008061612'], 'lon': ['121.4420', '120.4420', '119.4420'], 'lat': ['24.9976', '24.9976', '24.9976']}
df = DataFrame(data=d)
# IMPORTANT: convert to float
df[['lat', 'lon']] = df[['lat', 'lon']].astype(float)
df.head()

testlon = df[df['Date']=='2008061612']['lon'].values
testlat = df[df['Date']=='2008061612']['lat'].values

fig = plt.figure(figsize=(12, 10))
m = Basemap(projection='cyl', resolution='h', llcrnrlat=21.5, urcrnrlat=26.5, llcrnrlon=118, urcrnrlon=122.5)

m.readshapefile('gadm36_TWN_0', name='Taiwan', linewidth=0.25, drawbounds=True)
m.readshapefile('shapefile/TWN_adm2', name='Taiwan', linewidth=0.25, drawbounds=True)
m.drawcoastlines()
m.plot(testlon, testlat, 'r.')
'''
city_people ={}
date_city ={}
map ={}
from pandas import DataFrame
import matplotlib.pyplot as plt
import json
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

plt.figure(figsize=(16,8))
m = Basemap(projection='mill', resolution='l', llcrnrlat=21.5, urcrnrlat=26.5, llcrnrlon=118, urcrnrlon=122.5)

#m.readshapefile('COUNTY_MOI_1090820', name='states', linewidth=0.25, drawbounds=True)
m.readshapefile('gadm36_TWN_2', name='states', linewidth=0.25, drawbounds=True)
m.drawcoastlines(linewidth=0.25)
state_names = []
for info, shape in zip(m.states_info, m.states):
       state_names.append(info['NL_NAME_2'])


ax = plt.gca() # get current axes instance

# get Texas and draw the filled polygon
seg = m.states[state_names.index('南投縣')]

with open('mapp.json',encoding="utf-8") as f:
    map = json.load(f)
f.close()

poly = Polygon(seg, facecolor='#7f1818',edgecolor='#7f1818')
ax.add_patch(poly)

map['南投縣'] = seg
file = open('mapp.json', "w",encoding='utf-8')
json.dump(map, file,ensure_ascii=False)
file.close()

#新北市基隆市

plt.show()



