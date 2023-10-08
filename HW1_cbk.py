import json
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.basemap import Basemap
from pandas import DataFrame


with open('df.json',encoding="utf-8") as f:
    data = json.load(f)
    
city_people ={
'新北市':'3989880',
'臺中市':'2806385',
'高雄市':'2731782',
'臺北市':'2490445',
'桃園市':'2266913',
'臺南市':'1855449',
'彰化縣':'1250631',
'屏東縣':'801914',
'雲林縣':'667667',
'新竹縣':'575746',
'苗栗縣':'536585',
'嘉義縣':'491507',
'南投縣':'482841',
'新竹市':'451689',
'宜蘭縣':'449435',
'基隆市':'362239',
'花蓮縣':'320405',
'嘉義市':'263821',
'臺東縣':'213032',
'金門縣':'140740',
'澎湖縣':'106174',
'連江縣':'13711'}

'''
map['澎湖縣'] = [119.2,23.3]
map['金門縣'] = [118.44112,24.48564]
map['連江縣'] = [[119.97473,26.2142]
'''     
   
#fig1
map ={}
with open('mapp.json',encoding="utf-8") as f:
    map = json.load(f)


get_people ={}

for v in (data.values()):
    for k,vv in v.items():
        if k in get_people.keys():
            get_people[k] += vv
        else:
            get_people[k] = vv

print('\n',get_people)

comp_dic ={}
total_people = 0
total_get_people = 0
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
for i in city_people:
    total_people += int(city_people[i])
for i in get_people:
    total_get_people += int(get_people[i])
for i in city_people:
    comp_dic[i] = 10000*float(get_people[i])/float(city_people[i])
#print(total_get_people/total_people)

plt.figure(figsize=(16,8))
plt.bar(comp_dic.keys(),comp_dic.values())
plt.xlabel('縣市名')
plt.ylabel('比率(每萬人')
plt.hlines(10000*total_get_people/total_people,-0.5,21.5,color = "red")
plt.title('全台灣各縣市確診比率，結至5/7')
plt.show()

df = DataFrame({'縣市': comp_dic.keys(), '確診比率':comp_dic.values()})
df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
#fig2
plt.figure(figsize=(16,8))
m = Basemap(projection='mill', resolution='h', llcrnrlat=21.5, urcrnrlat=26.5, llcrnrlon=118, urcrnrlon=122.5)
m.readshapefile('COUNTY_MOI_1090820', name='states', linewidth=0.25, drawbounds=True)
m.drawmapboundary(fill_color='aqua')
m.drawcoastlines(linewidth=0.25)
ax = plt.gca() # get current axes instance
color = 'white'
for k,v in map.items():
    if comp_dic[k] <= 25:
        color = '#8CEA00'
    elif comp_dic[k] <= 40:
        color = '#E1E100'
    elif comp_dic[k] <= 80:
        color = '#FF2D2D'
    elif  comp_dic[k] <= 150:
        color = '#6F00D2'
    else:
        color = '#842B00'
    poly = Polygon(map[k], facecolor=color,edgecolor=color)
    ax.add_patch(poly)
ax.text( 15,35,"All Right Reserved CBK&YoyoTsao", color='black',fontsize=8)

plt.show()

#fig3    
for k,v in (data.items()):
    plt.figure(figsize=(16,8))
    plt.bar(v.keys(),v.values())    
    plt.xlabel('縣市名')
    plt.ylabel('確診人數')  
    plt.title(k+'台灣各縣市新增確診人數')       
    plt.show()

#fig4
sum_num=0
num_list =[]
for k,v in (data.items()):
    for vv in v.values():
        sum_num += int(vv)
    num_list.append(sum_num)
    sum_num =0

plt.figure(figsize=(16,8))
x=[]
for i in list(data.keys()):
    x.append(i[5:])
x.reverse()
num_list.reverse()
plt.plot(x,num_list)    
plt.xlabel('日期')
plt.ylabel('確診人數')  
plt.title('自四月以來確診人數走勢圖')       
plt.show()  