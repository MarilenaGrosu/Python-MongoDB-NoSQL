#1) Să se reprezinte grafic (de tip pie) valoarea medie a daunelor pentru 
#al doilea semestru pentru marcile Audi si Ford pentru fiecare an de fabricatie

import pandas as pd
df = pd.read_csv("clienti_daune.csv")
print(df)
df['DATA_VANZARII'] = pd.to_datetime(df['DATA_VANZARII'])
dataf = df[((df['MARCA'] == 'AUDI') | (df['MARCA'] == 'FORD')) & (pd.DatetimeIndex(df['DATA_VANZARII']).month>5)]
print(dataf)
dataframe = df.groupby('AN_FABRICATIE')['VALOARE_DAUNA'].mean()
plot= dataframe.plot.pie(subplots=True, figsize=(6, 3))


#2)Sa se grupeze dupa tara producatoare si sa afiseze valoarea medie a pretului 
#manoperei

import pandas as pd
df = pd.read_csv("clienti_daune.csv")
print(df)
dataf = dataframe = df.groupby('TARAPRODUCATOR')['PRET_MANOPERA'].mean()
print(dataf)


#3) Sa se grupeze dupa tara producatoare si sa afiseze tara producatoare si 
#toate tagurile fiecarei marci din tara producatoare respctiva. 
#Sa se calculeze de cate ori apare tagul bad pentru fiecare tara producatoare.

import pandas as pd
df = pd.read_csv("clienti_daune.csv")
print(df)
dataf = dataframe = df.groupby('TARAPRODUCATOR')['MARCA']


#4) Să se creeze setul format din user_usage și supported_devices și 
#să se reprezinte grafic (bare verticale) traficul însumat (coloana monthly_mb)
#pentru fiecare brand (coloana Retail Branding).

import pandas as pd
df1 = pd.read_csv('user_usage.csv')
print(df1)
df2 = pd.read_csv('supported_devices.csv')
print(df2)
dataf = pd.concat([df1, df2], axis=1, sort=False)
print(dataf)
dataframe = dataf.groupby('Retail Branding')['monthly_mb'].sum()
print(dataframe)
dataf= dataframe.nlargest(3)
dataf.sort_values().plot( kind='bar', color = 'lightblue')



#5) Să se afișeze, utilizând fișierul phone_data.csv, durata însumata pentru 
#fiecare lună și durata însumată pentru un anumit tip de rețea (mobile) pentru 
#fiecare lună.

import pandas as pd
df = pd.read_csv('phone_data.csv')
print(df)
dataframe1 = df.groupby('month')['duration'].sum()
dataframe2 = df[df['network_type']=='mobile'].groupby('month')['duration'].sum()
print(dataframe1)
print(dataframe2)




#6) Sa se construiasca un pivot table utilizand datele: http://bit.ly/2cLzoxH

import pandas as pd
data_url = "http://bit.ly/2cLzoxH"
df = pd.read_csv(data_url)
print(df)
pivot_table=pd.pivot_table(df, values=None, index=["country", "year"], columns=None, aggfunc='mean',  margins=True, margins_name='All')
print(pivot_table)



#7) Sa se reprezinte grafic sub forma de bare 3 marci din Europa care au 
#cele mai mici daune totale.

import pandas as pd
df = pd.read_csv("clienti_daune.csv")
print(df)
dataframe = df.groupby('MARCA')['VALOARE_DAUNA'].sum()
dataf= dataframe.nlargest(3)
dataf.sort_values().plot( kind='bar', color = 'lightblue')



