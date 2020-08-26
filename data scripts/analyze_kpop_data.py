import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

kpop_data = pd.read_csv('../data/music/kpop_songs_data.csv', index_col = 0)
print(kpop_data.head(6))
#plt.show()
#print(kpop_data.groupby(['Artist Name']).mean())
'''
bts_tempo = kpop_data[kpop_data['Artist Name'] == 'BTS']['Tempo']  
exo_tempo = kpop_data[kpop_data['Artist Name'] == 'EXO']['Tempo']  
twice_tempo = kpop_data[kpop_data['Artist Name'] == 'TWICE']['Tempo']
blackpink_tempo = kpop_data[kpop_data['Artist Name'] == 'BLACKPINK']['Tempo']

sns.distplot(bts_tempo, label = 'BTS tempo')
sns.distplot(exo_tempo, label = 'EXO tempo')
sns.distplot(twice_tempo, label = 'TWICE tempo')
sns.distplot(twice_tempo, label = 'BLACKPINK tempo')
'''
#title('Distribution of musical tempo of four k-pop groups', size = 20)
#legend(prop = {'size': 18});
