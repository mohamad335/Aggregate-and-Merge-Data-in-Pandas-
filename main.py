import pandas as pd
import matplotlib.pyplot as plt
sets=pd.read_csv('data/sets.csv')
#create new siries with the year of the set
sets_by_years=sets.groupby('year').count()
sets_by_years['set_num'].head()#give value of set_num of years
plt.plot(sets_by_years.index,sets_by_years['set_num'])#plot the graph
plt.show()#show the graph
