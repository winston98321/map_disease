import json
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.basemap import Basemap
from pandas import DataFrame
import statistics as st
from sklearn.linear_model import LinearRegression
import numpy as np
import dataframe_image as dfi
import re
import requests

with open('df.json',encoding="utf-8") as f:
    data = json.load(f)
citys = ['新北市','台中市','臺中市','高雄市','臺北市','台北市','桃園市','台南市','臺南市','彰化縣','屏東縣','雲林縣','新竹縣','苗栗縣','嘉義縣','南投縣','新竹市','宜蘭縣','基隆市','花蓮縣','嘉義市','台東縣','臺東縣','金門縣','澎湖縣','連江縣']

city_people ={}
url = 'https://mobile.stat.gov.tw/CheckBoxListTable.aspx?T=VC41LjMuMg=='
html = requests.get(url).text
for i in citys:
    try:
        str1 = re.search(i+'.*',html).group()[58:70]
        city_people[i] = int(re.search('[,0-9]*',str1).group().replace(',',''))
    except:
        0   

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
plt.title('全台灣各縣市確診比率，截至5/16')
plt.savefig('D:\資料科學\報告\總輸出\各縣市確診比率.png')
plt.show()

km_ratio =[1943.849133,1267.050004,925.4466788,9162.79525,1856.673552,846.5979402,1164.031698,288.9155186,517.2374791,403.3142681,294.7759204,258.1936984,117.5815232,4336.800041,209.661195,2728.547766,69.2233029,4395.141406,60.6021883,928.0213114,836.911309,476.0763889]
hos_ratio =[1.11,1.27,2.85,3.5,1,1.24,1.43,2.29,1.7,1.38,1.81,3.03,1.64,0.88,2.71,1.48,1.6,1.59,1.94,2.8,3.44,3.69]
dis_ratio =[151.39,108.55,141.25,148.99,130.02,101.55,88.99,138.49,94.83,113.51,88.23,80.99,123.66,114.42,124.99,161.58,195.2,105.68,172.21,37.75,110.82,106.19]
th_ratio =[102.97,158.23,159.01,235.05,127.71,150.64,124.18,122.02,104.33,102.44,94.97,112.18,109.57,152.30,139.73,119.10,187.71,255.15,129.38,40.61,79.66,91.87]
df = DataFrame({'縣市': comp_dic.keys(), 'covid-19':comp_dic.values(),'人口密度':km_ratio,'醫療量能':hos_ratio,'法定傳染病':dis_ratio,'醫療人員密度':th_ratio})
df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
table =df.corr()
#fig2
plt.figure(figsize=(16,8))
m = Basemap(projection='mill', resolution='h', llcrnrlat=21.5, urcrnrlat=26.5, llcrnrlon=118, urcrnrlon=122.5)
m.readshapefile('COUNTY_MOI_1090820', name='states', linewidth=0.25, drawbounds=True)
m.drawmapboundary(fill_color='aqua')
m.drawcoastlines(linewidth=0.25)
ax = plt.gca() # get current axes instance
color = 'white'
for k,v in map.items():
    if comp_dic[k] <= 80:
        color = '#8CEA00'
    elif comp_dic[k] <= 120:
        color = '#E1E100'
    elif comp_dic[k] <= 200:
        color = '#FF2D2D'
    elif  comp_dic[k] <= 400:
        color = '#6F00D2'
    else:
        color = '#842B00'
    poly = Polygon(map[k], facecolor=color,edgecolor=color)
    ax.add_patch(poly)
ax.text( 15,35,"All Right Reserved CBK&YoyoTsao", color='black',fontsize=8)
plt.savefig('D:\資料科學\報告\總輸出\台灣密度地圖.png')
plt.show()

#fig3    
'''for k,v in (data.items()):
    plt.figure(figsize=(16,8))
    plt.bar(v.keys(),v.values())    
    plt.xlabel('縣市名')
    plt.ylabel('確診人數')  
    plt.title(k+'台灣各縣市新增確診人數')       
    plt.savefig('D:/資料科學/報告/pic')
    plt.show()'''
i=0
for k,v in (data.items()):
    i+=1
    plt.figure(figsize=(16,8))
    plt.bar(v.keys(),v.values())    
    plt.xlabel('縣市名')
    plt.ylabel('確診人數')  
    plt.title(k+'台灣各縣市新增確診人數')
    plt.savefig('D:/資料科學/報告/pic/'+'0'*i+'.png')
    plt.close()    
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
plt.savefig('D:\資料科學\報告\總輸出\自四月以來確診人數走勢圖.png')
plt.show()


get_ratio = comp_dic.values()
km_ratio =[1943.849133,1267.050004,925.4466788,9162.79525,1856.673552,846.5979402,1164.031698,288.9155186,517.2374791,403.3142681,294.7759204,258.1936984,117.5815232,4336.800041,209.661195,2728.547766,69.2233029,4395.141406,60.6021883,928.0213114,836.911309,476.0763889]
sda = st.pstdev(get_ratio)
sdb = st.pstdev(km_ratio)

x = np.array(list(comp_dic.values())).reshape(-1,1)
model = LinearRegression()
model.fit(x.reshape(-1,1),km_ratio)
plt.scatter(comp_dic.values(),km_ratio)    
plt.xlabel('確診比率')
plt.ylabel('人口密度')  
plt.title('確診比率與人口密度相關性')
tx = df.corr()
#plt.text(0,8000, '相關係數為:'+str(tx['確診比率']['人口密度'])+'\n'+'確診比率的標準差:'+str(sda)+'\n'+'人口密度標準差:'+str(sdb), fontsize=8, color='black')  
predict = model.predict(x)
plt.plot(x,predict,color="red")
plt.savefig('D:\資料科學\報告\總輸出\確診比率與人口密度相關性.png') 
plt.show()

model = LinearRegression()
model.fit(x.reshape(-1,1),dis_ratio)
plt.scatter(comp_dic.values(),dis_ratio)    
plt.xlabel('確診比率')
plt.ylabel('法定傳染病比率')  
plt.title('法定傳染病比率與確診比率相關性')
tx = df.corr()
#plt.text(0,8000, '相關係數為:'+str(tx['確診比率']['人口密度'])+'\n'+'確診比率的標準差:'+str(sda)+'\n'+'人口密度標準差:'+str(sdb), fontsize=8, color='black')  
predict = model.predict(x)
plt.plot(x,predict,color="red")
plt.savefig('D:\資料科學\報告\總輸出\法定傳染病與確診比率相關性.png')  
plt.show()

model = LinearRegression()
model.fit(x.reshape(-1,1),hos_ratio)
plt.scatter(comp_dic.values(),hos_ratio)    
plt.xlabel('確診比率')
plt.ylabel('醫療量能')  
plt.title('醫療量能與確診比率相關性')
tx = df.corr()
#plt.text(0,8000, '相關係數為:'+str(tx['確診比率']['人口密度'])+'\n'+'確診比率的標準差:'+str(sda)+'\n'+'人口密度標準差:'+str(sdb), fontsize=8, color='black')  
predict = model.predict(x)
plt.plot(x,predict,color="red")
 
plt.savefig('D:\資料科學\報告\總輸出\醫療量能與確診比率相關性.png')
plt.show()

model = LinearRegression()
model.fit(x.reshape(-1,1),hos_ratio)
plt.scatter(comp_dic.values(),th_ratio)    
plt.xlabel('確診比率')
plt.ylabel('醫療人員密度')  
plt.title('醫療人員密度與確診比率相關性')
tx = df.corr()
#plt.text(0,8000, '相關係數為:'+str(tx['確診比率']['人口密度'])+'\n'+'確診比率的標準差:'+str(sda)+'\n'+'人口密度標準差:'+str(sdb), fontsize=8, color='black')  
predict = model.predict(x)
plt.plot(x,predict,color="red")
 
plt.savefig('D:\資料科學\報告\總輸出\醫療人員密度與確診比率相關性.png')
plt.show()
dfi.export(table,"D:\資料科學\報告\總輸出\mytable.png") 