import numpy as np
import pandas as pd
from astropy.io import ascii as at
import csv 

df1 = pd.read_csv('/Users/ihahn/cassi/gaiadr3696/grrrr1.csv') 
df1 = df1.rename(columns ={"EW":"gdr3696", "species":"species", "wavelength":"wavelength", "ep":"expot", "gf":"loggf"}  )
df2 = pd.read_csv('/Users/ihahn/cassi/gaiadr3603/grrrr2.csv') 
df2 = df2.rename(columns = {"EW":"gdr3664", "species":"species", "wavelength":"wavelength", "expot":"expot2", "loggf":"loggf2"})

df1["gdr3664"] = " "

#enumerate method
'''for df2Row, i in enumerate(df2['index']):
    for df1Row, j in enumerate(df1['index']):
        if df1['wavelength'][df1Row]==df2['wavelength'][df2Row]:
            #print(f"Matching wavelengths: {i}")
            df1.at[df1Row, 'expot2'] = df2.at[df2Row, 'expot2']
            df1.at[df1Row, 'loggf2'] = df2.at[df2Row, 'loggf2']
            df1.at[df1Row, 'gdr3664'] = df2.at[df2Row, 'gdr3664']
            break
            
            
            
        if (df1Row == len(df1)-1):
            params2={\
                'wavelength':(df2.at[df2Row, 'wavelength']), \
                'species':(df2.at[df2Row, 'species']), \
                'loggf2':(df2.at[df2Row, 'loggf2']), \
                'gdr3664':(df2.at[df2Row, 'gdr3664']), \
                'expot2':(df2.at[df2Row, 'expot2'])}
            
            #append dictionary to dataframe 1
            df1 = df1.append(params2, ignore_index=True)'''


#iterrows method for looping through df more simply than ennumerate, works better
for index2, row2, in df2.iterrows():
    for index1, row1 in df1.iterrows():
        if row1['wavelength'] == row2['wavelength']:
            #df1.at[index1, 'expot2'] = row2['expot2']
            #df1.at[index1, 'loggf2'] = row2['loggf2']
            df1.at[index1, 'gdr3664'] = row2['gdr3664']
            break

        if index1 == len(df1)-1:
            params2={\
                'wavelength':(row2['wavelength']), \
                'species':(row2['species']), \
                'loggf':(row2['loggf2']), \
                'gdr3696':(""), \
                'expot':(row2['expot2']), \
                #'expot2':row2['expot2'],\
                'gdr3664':(row2['gdr3664']),}
                #'loggf2' : (row2['loggf2'])}
            
            #append dictionary to dataframe 1
            df1 = df1.append(params2, ignore_index=True)

df1 = df1.sort_values(by='species')
print(df1)
df1.to_csv('combined_lines_1.csv', index=False) 
        