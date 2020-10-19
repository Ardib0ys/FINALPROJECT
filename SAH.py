# import libraries
from bs4 import BeautifulSoup
# import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# specify the url
url = 'https://kawalpemilu.org/#pilpres:0'
url2 = 'https://www.bps.go.id/dynamictable/2017/05/04/1241/indeks-demokrasi-indonesia-idi-menurut-provinsi-2009-2017.html'

# The path to where you have your chrome webdriver stored:
webdriver_path = 'D:\PyCharm\chromedriver_win32/chromedriver.exe'

# Add arguments telling Selenium to not actually open a window
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')

# Fire up the headless browser
browser = webdriver.Chrome(executable_path=webdriver_path,
                           options=chrome_options)
browser2 = webdriver.Chrome(executable_path=webdriver_path,
                           options=chrome_options)
# Load webpage
browser.get(url)
browser2.get(url2)

# It can be a good idea to wait for a few seconds before trying to parse the page
# to ensure that the page has loaded completely.
time.sleep(10)

# Parse HTML, close browser
soup = BeautifulSoup(browser.page_source, 'html.parser')
soup2 = BeautifulSoup(browser2.page_source,'html.parser')
# print(soup)
pretty = soup.prettify()
browser.quit()
# find results within table
results = soup.find('table',{'class':'table'})
rows = results.find_all('tr',{'class':'row'})
array = []
#jokowi = []
#prabowo = []
total2019 = []

# find results within table
result_value    = soup2.find('table', attrs={'id': 'tableRightBottom'})
rows_value      = result_value.find_all('tr')
value = []

for id, r in enumerate(rows_value[:-1]):
    # find all columns per result
    data_value = rows_value[id].find_all('td', attrs={'class': 'datas'})

    # check that columns have data
    if len(data_value) == 0:
        continue

    # write columns to variables
    #wilayah = data_wilayah[0].find('b').getText()

    nilai = data_value[-1].getText()
    # Remove decimal point
    # nilai = nilai.replace('.','')
    # Cast Data Type Integer
    nilai = float(nilai)
    value.append(nilai)


# print(rows)
for r in rows:
    # find all columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
# write columns to variables
    wilayah = data[1].find('a').getText()
    if wilayah != 'KALIMANTAN UTARA':
        #satu = data[2].find('span', attrs={'class':'abs'}).getText()
        #dua = data[3].find('span', attrs={'class': 'abs'}).getText()
        tiga = data[4].find('span', attrs={'class': 'sah'}).getText()
        tsah = data[5].find('span', attrs={'class':'tsah'}).getText()
        # Remove decimal point
        #satu = satu.replace('.','')
        #dua = dua.replace('.','')
        tiga = tiga.replace('.', '')
        tsah = tsah.replace('.','')

        # Cast Data Type Integer
        #satu = int(satu)
        #dua = int(dua)
        tiga = float(tiga)
        tsah = float(tsah)
        perbandingan = tiga/(tiga+tsah)*100

        array.append(wilayah)
        #jokowi.append(satu)
        #prabowo.append(dua)
        total2019.append(perbandingan)

# Convert to numpy
np_array = np.array(array)
#np_jokowi= np.array(jokowi)
#np_prabowo= np.array(prabowo)
np_total = np.array(total2019)
np_value = np.array(value)



df =pd.DataFrame({'x':np_array,'persentase suara sah':np_total,'Index Demokrasi Indonesia':np_value})

plt.plot( 'x', 'persentase suara sah', data=df, marker='o',  markersize=4,  linewidth=1)
plt.plot( 'x', 'Index Demokrasi Indonesia', data=df, marker='o',  markersize=4,  linewidth=1)

plt.xticks(rotation=90,ha='right')
plt.legend(loc='best')

plt.show()

# Hacktoberfest2020
# Support open source and pick a limited edition T-shirt or plant a tree.
