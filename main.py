
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('Covid2.csv') 


x = df['7-Tages-Inzidenz']
y = df['Anzahl Fälle']
tote= df['Todesfälle']

plt.plot(y,tote)

plt.xlabel('Anzahl Fälle', fontsize=18)
plt.ylabel('7-Tages-Inzidenz', fontsize=16)

plt.plot(x, y)
plt.legend(['Todesfälle','Anzahl Fälle'])
plt.title('Lagebericht zu Covid 19')
plt.show()

