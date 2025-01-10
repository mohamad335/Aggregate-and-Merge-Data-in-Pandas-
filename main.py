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
themes= pd.read_csv('data/themes.csv')
set_theme_count=sets["theme_id"].value_counts()#count the number of sets per theme
set_theme_count = pd.DataFrame({'id':set_theme_count.index,'set_count':set_theme_count.values})#create a dataframe
#merge the themes and set_theme_count dataframes
merged_df = pd.merge(set_theme_count, themes, on='id')
#create a plot bar
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Number of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.show()

