# Import Libraries
import main as function
import numpy as np
import matplotlib.pyplot as plt

# Specify the URL
url  = 'https://kawalpemilu.org/#pilpres:0'
soup = function.getData(url)

# Find results within table
results = soup.find('table', {'class':'table'})
rows    = results.find_all('tr',{'class':'row'})
list_wilayah = []
jokowi       = []
prabowo      = []

# Print(rows)
for r in rows:
    # Find columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    # Write columns to variables
    wilayah = data[1].find('a').getText()
    capres1 = data[2].find('span', attrs={'class': 'abs'}).getText()
    capres2 = data[3].find('span', attrs={'class': 'abs'}).getText()

    #Removing decimal point
    capres1 = capres1.replace('.', '')
    capres2 = capres2.replace('.', '')

    # Cast Data Type Integer
    capres1 = int(capres1)
    capres2 = int(capres2)
    list_wilayah.append(wilayah)
    jokowi.append(capres1)
    prabowo.append(capres2)

# Convert to numpy
np_wilayah = np.array(list_wilayah)
np_jokowi  = np.array(jokowi)
np_prabowo = np.array(prabowo)

# Plot Data
fig,ax   = plt.subplots(figsize=(10, 5))
# fig,ax = plt.subplots()
# print(ax)
pos   = list(range(len(np_jokowi)))
width = 0.25

# print (ind-width/2)

ax.bar(pos, np_jokowi, width, color='brown', label='Jokowi')
ax.bar([p + width for p in pos], np_prabowo, width, color='blue', label='Prabowo')
ax.set_xticks([p + 0.5 * width for p in pos])
ax.set_xticklabels(np_wilayah)

## Naming Label
plt.xlabel('Provinsi')
plt.ylabel('Perolehan Suara')

## Styling x,y value
plt.yticks(np.arange(np_jokowi.min(), np_jokowi.max(), 4000000))
plt.xticks(rotation='vertical', ha='right')
plt.legend(loc='upper right')
plt.yscale('linear')

plt.show()