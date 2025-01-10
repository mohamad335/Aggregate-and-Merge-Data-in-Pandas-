import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import Image, display
sets=pd.read_csv('data/sets.csv')
#create new siries with the year of the set
sets_by_years=sets.groupby('year').count()
sets_by_years['set_num'].head()#give value of set_num of years
#plt.plot(sets_by_years.index[:-2],sets_by_years['set_num'][:-2])#plot the graph
#plt.show()#show the graph
#plt.savefig('sets_by_years.png')#save the graph
#aggricate the number of themes by year and give the number of unique theme_id
themes_by_year=sets.groupby(['year']).agg({'theme_id':pd.Series.nunique})
#we need to change the name of the column
themes_by_year.rename(columns={'theme_id':'nr_themes'}, inplace=True)
#print(themes_by_year.head())
#create a line plot of the number of themes released by year-on-ye and the number of sets released by year-on-year
#ax1=plt.gca()#get current axis
#ax2=ax1.twinx()#create a twin axis

#ax1.plot(themes_by_year.index[:-2],themes_by_year['nr_themes'][:-2],color='g')#plot and color the number of themes
#ax2.plot(sets_by_years.index[:-2],sets_by_years['set_num'][:-2],color='b')#plot and color the number of sets
#ax1.set_xlabel('Year')
#ax1.set_ylabel('Number of themes',color='g')
#ax2.set_ylabel('Number of sets', color='b')
#plt.title('Number of themes and sets released by year-on-year')
#plt.show()#show the graph
#create scatter plot of the average number of parts per set
parts_of_sets=sets.groupby(['year']).agg({'num_parts':pd.Series.mean})#average number of parts per set
plt.scatter(parts_of_sets.index[:-2], parts_of_sets['num_parts'][:-2])#scatter plot
plt.title('Average number of parts per set')
plt.xlabel('Year')
plt.ylabel('Number of parts')
plt.savefig('images/parts_of_sets.png')
plt.show()

