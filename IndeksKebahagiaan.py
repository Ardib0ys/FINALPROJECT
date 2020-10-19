import numpy as np
import matplotlib.pyplot as plt
import main as func
import pandas as pd

urlbps = 'https://www.bps.go.id/dynamictable/2017/05/04/1243/indeks-kebahagiaan-menurut-provinsi-2014-2017.html'
soup1 = func.getData(urlbps)

# find results within table
result_wilayah = soup1.find('table', attrs={'id': 'tableLeftBottom'})
result_value = soup1.find('table', attrs={'id': 'tableRightBottom'})
rows_wilayah = result_wilayah.find_all('tr')
rows_value = result_value.find_all('tr')

data_ipm = {}

for id, r in enumerate(rows_wilayah[:-1]):
    # find all columns per result
    data_result = r.find_all('td', attrs={'id': 'th4'})
    data_value = rows_value[id].find_all('td', attrs={'class': 'datas'})
    # check that columns have data
    if len(data_result) == 0:
        continue

    wilayah = data_result[0].getText()
    wilayah = wilayah.replace('\n', '')
    nilai = data_value[-1].getText()
    # Remove decimal point
    nilai = nilai.replace('.', '')
    # Cast Data Type Integer
    nilai = int(nilai)
    data_ipm.update([(wilayah, nilai)])

soup2 = func.getData('https://kawalpemilu.org/#0',second=10)
# find results within table
results2 = soup2.find('table',{'class':'table'})
rows2 = results2.find_all('tr',{'class':'row'})
# index 0 = tinggi, index1 = rendah

data_kawal = {}
jumlah_jokowi = []
jumlah_prabowo = []

# print(rows)
for r in rows2[:-1]:
    # find all columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    # write columns to variables
    provinsi = data[1].find('a').getText()
    provinsi = provinsi.replace('\n', '')
    satu = data[2].find('span', attrs={'class':'abs'}).getText()
    dua = data[3].find('span', attrs={'class': 'abs'}).getText()
    # Remove decimal point
    satu = satu.replace('.','')
    dua = dua.replace('.','')
    # Cast Data Type Integer
    satu = int(satu)
    dua = int(dua)

    if provinsi == 'KEPULAUAN BANGKA BELITUNG':
        provinsi = 'KEP. BANGKA BELITUNG'
    elif provinsi == 'KEPULAUAN RIAU':
        provinsi = 'KEP. RIAU'
    elif provinsi == 'DAERAH ISTIMEWA YOGYAKARTA':
        provinsi = 'DI YOGYAKARTA'

    if satu > dua:
        jumlah_jokowi.append(data_ipm[provinsi])
    elif dua > satu:
        jumlah_prabowo.append(data_ipm[provinsi])

rata_jokowi = round(np.mean(jumlah_jokowi))
rata_prabowo = round(np.mean(jumlah_prabowo))

# Create Dictionary
my_dict = {'paslon':['JOKOWI', 'PRABOWO'],'value':[rata_jokowi, rata_prabowo]}
# Create Dataframe
df = pd.DataFrame(my_dict)

# Plot dataframe to histogram
plt.bar(df['paslon'], df['value'])
plt.xlabel('Calon Presiden')
plt.ylabel('Rata-Rata Indeks Demokrasi Indonesia')
plt.gca().set_ylim([df['value'].min()-50,df['value'].max()+50])
plt.xticks(rotation=30,ha='right')
plt.legend(loc='upper right')
plt.show()

# Hacktoberfest2020
