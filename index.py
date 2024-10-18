import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\Rakhm\\Downloads\\Brann1_stor.csv", delimiter=";", decimal=",", index_col=False)
# print(df)

#Variabler
masse_data = df[['Vekt [g]']] - 2213.6 
temperatur_data = df[['Kanal 19 [C]', "Kanal 20 [C]"]] 

# Massen til heptan som en funksjon av tiden
def masseHeptan(t):
   return masse_data.iloc[t].values[0] 
# Temperaturen til heptan som en funksjon av tiden
def temperatur(t): 
   kanal19 = temperatur_data.iloc[t, 0]
   kanal20 = temperatur_data.iloc[t, 1]
   return (kanal19 + kanal20) / 2

# antall sekunder 
time_values = range(len(masse_data))
#ulike verdiene
mass_values = [masseHeptan(t) for t in time_values]
temperature_values = [temperatur(t) for t in time_values]

# Resultatet som en graf
plt.plot(time_values, mass_values, label='Massen til Heptan')
plt.plot(time_values, temperature_values, label='Temperaturen til Heptan')
plt.xlabel('Tid (sekunder)')
plt.ylabel('Massen og Temperaturen')
plt.title('Brann1_liten - Temperatur og Masse')
plt.text(time_values[0], mass_values[0], f'{mass_values[0]:.2f} g')
plt.text(time_values[-1], mass_values[-1], f'{mass_values[-1] + 2.7:.2f} g')
plt.text(time_values[0], temperature_values[0], f'{temperature_values[0]:.2f} C')
plt.text(time_values[-1], temperature_values[-1], f'{temperature_values[-1]:.2f} C')
plt.legend()
plt.grid(True)  
plt.show()


   
# Massetapsraten som en funksjon av tiden
def masseTapsRaten(t):
    m_i = masse_data.iloc[t].values[0] 
    m_i_pluss = masse_data.iloc[t + 1].values[0] 
    t_i_pluss = t + 1
    formelen = (m_i - m_i_pluss) / (t_i_pluss - t)
    return formelen

#tid for massetapsraten
tid_mtr = range(len(masse_data) - 1)
#massetapsrate etter så så mange sekunder
mtr_hver = [masseTapsRaten(t) for t in tid_mtr]


plt.figure(figsize=(10, 6))
plt.plot(tid_mtr, mtr_hver)
plt.xlabel('Tid (sekunder)')
plt.ylabel('Massetapsrate g/m^2s')
plt.title('Graf av masstapsraten over tid')
plt.grid(True)
plt.xticks(range(0, len(tid_mtr), 50))
plt.show()

def masseFluksen(t):
    m_i = masse_data.iloc[t].values[0] 
    m_i_pluss = masse_data.iloc[t + 1].values[0] 
    t_i_pluss = t + 1
    arealet = 0.2 * 0.2 #arealet oppgitt i meter
    massetapsraten = (m_i - m_i_pluss) / (t_i_pluss - t)
    formelen = massetapsraten / arealet
   #  print(f"3. Massefluksen etter {t} sekunder er: {formelen:.2f}")
    return formelen

# Tidspunkter for massefluksen
tid_massefluksen = range(len(masse_data) - 1)

# Massefluksen etter hvert sekund
massefluksen_data = [masseFluksen(t) for t in tid_massefluksen]

plt.figure(figsize=(10, 6))
plt.plot(tid_massefluksen, massefluksen_data)
plt.xlabel('Tid (sekunder)')
plt.ylabel('Massefluks (g/m^2/s)')
plt.title('Graf av massefluksen over tid')
plt.grid(True)
plt.show()

def strålingen(t):
   kanal19 = temperatur_data.iloc[t, 0] + 273.15 #Gjøre om fra celcius til kelvin
   kanal20 = temperatur_data.iloc[t, 1] + 273.15 #Gjøre om fra celcius til kelvin
   temperatur =  (kanal19 + kanal20) / 2
   stefan_boltzmann_konstant = 5.67 * 10**(-8)
   emissivitet = 0.9
   formelen = emissivitet * stefan_boltzmann_konstant * temperatur**4
   return formelen

# Tidsverdier
tid_verdier = range(len(temperatur_data))

# Beregning av strålingen for hver tid
strålingsverdier = [strålingen(t) for t in tid_verdier]

# Plot av strålingen
plt.plot(tid_verdier, strålingsverdier)
plt.xlabel('Tid (Sekunder)')
plt.ylabel('Stråling (W)')
plt.title('Stråling fra flammen over tid')
plt.grid(True)
plt.show()













