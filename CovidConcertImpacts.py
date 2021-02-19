#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import numpy as np

print("Setup Complete")


# In[7]:


#get path of file to read
my_filepath = r"C:\Users\ARI\Documents\Databases Spring 2019\Covid Concert Proj\CovidConcertImpacts.xlsx"
#read file into variable
cc_data = pd.read_excel(my_filepath) 


# In[8]:


#print first 5 rows
cc_data.head()


# In[9]:


#get size and shape of dataset
cc_data.shape


# In[10]:


#get count of how many yes & no responses in percent
cc_data['PandemicIncreaseInHoursOfMusic'].value_counts(normalize = True)


# In[11]:


#get count of how many yes & no responses
cc_data['PandemicIncreaseInHoursOfMusic'].value_counts()


# In[12]:


#how to get the number for each music way 
cc_data['WaysToListenToMusic'].head()


# In[13]:


#saves amount of people that put down Spotify to variable
spotify_count=cc_data['WaysToListenToMusic'].str.contains('Spotify')
#gets percentage of how many people chose Spotify
spotify_count.value_counts(normalize=True)


# In[14]:


#split each row based on delimited passed to that function
get_music= cc_data['WaysToListenToMusic'].str.split(', ', expand=True)
get_music.head()


# In[15]:


#stack this dataframe 
music_by_person = get_music.stack().to_frame()
music_by_person.head()


# In[16]:


music_by_person.columns=['Software']


# In[17]:


music_by_person.index = ['0','0','1','1','2','3',
                         '4','4','4','4','5', '5',
                        '6','6','7','7','7','8','9','9','10',
                         '10','11','12','13','14', '15',
                        '16','16','17','18','18','19','20','20','20',
                         '21','21','21','21','22', '22',
                        '23','23','24','25','25','25','26','26','27',
                         '28','28','28','29','29', '30',
                        '30','31','31','32','33','33','33','34','34',
                         '35','35','36','36','36'
                        ]
music_by_person


# In[18]:


music_by_person.index.name='Person'
music_by_person.reset_index(inplace=True)
music_by_person


# In[19]:


music_by_person['Software']


# In[20]:


music_by_person['Software'].unique()


# In[21]:


ds=music_by_person['Software'].value_counts().to_frame()
ds


# In[22]:


#bar plot to show which music software is used the most
ds.plot(kind='bar',figsize=(14,5), color='#04B404')
plt.title('Music Software Count')
plt.xlabel('Software')
plt.ylabel('Count of Users')


# In[23]:


# show first 5 rows for Hours of music a day
cc_data['HoursOfMusicADay'].head()


# In[24]:


#count how many times the value for hours of music was chosen and set it to a variable
music_time= cc_data['HoursOfMusicADay'].value_counts().to_frame()
music_time


# In[ ]:





# In[25]:


music_time.plot(kind='bar',figsize=(14,5), color='blue')
plt.title('Time Spent Listening to Music Per Day')
plt.xlabel('Number of Hours')
plt.ylabel('Count of Users')


# In[26]:


music_time.describe()


# In[43]:


#QUES 2 HOW LIKELY TO LISTEN TO WATCH LIVESTREAM IF WATCH OWN FOOTAGE


# In[44]:


#how many people said yes/no to watching own footage
cc_data['WatchedOwnConcertFootage'].value_counts()


# In[56]:


#how many said y or n to watching live streams
cc_data['WatchedLivestreamShows'].value_counts()


# In[66]:


#How many watched both LIVE STREAM & OWN FOOTAGE

stream_and_footage= cc_data[(cc_data['WatchedOwnConcertFootage']=='Yes') & 
                    (cc_data['WatchedLivestreamShows']=='Yes')]
l=len(stream_and_footage)
print('Number of users that watched both live stream and own footage: ',l)


# In[68]:


s_and_f = stream_and_footage['WatchedOwnConcertFootage'].to_frame()


# In[69]:


no_stream_and_footage= cc_data[(cc_data['WatchedOwnConcertFootage']=='No') & 
                    (cc_data['WatchedLivestreamShows']=='No')]
l2=len(no_stream_and_footage)
print('Number of users that did not watch both live stream and own footage: ',l2)


# In[72]:


no_s_and_f =no_stream_and_footage['WatchedOwnConcertFootage'].to_frame()


# In[232]:


#shows if people that had both NO or both YES
result = pd.concat([s_and_f, no_s_and_f],ignore_index=True, sort=False)


# In[75]:


result.describe()


# In[ ]:


#Que3  Increase in music listening during pandemic


# In[39]:


#increase in hours of music during pandemic in percent
cc_data['PandemicIncreaseInHoursOfMusic'].value_counts(normalize = True)


# In[49]:


increase=cc_data[(cc_data['PandemicIncreaseInHoursOfMusic']=='Yes')& 
                    (cc_data['HoursOfMusicADay']==6)]
increase


# In[79]:


#Que4  Support artists during pandemic?


# In[106]:


pm=cc_data['PurchasedMerch'].value_counts()


# In[107]:


wls=cc_data['WatchedLivestreamShows'].value_counts()


# In[109]:


#combine columns with value counts
data = [pm, wls]

headers = ["PurchasedMerch", "WatchedLivestreamShows"]

df3 = pd.concat(data, axis=1, keys=headers)


# In[110]:


df3


# In[115]:


#plot bar graph for how many people used each way to listen to music
df3.plot(kind='bar', figsize=(13,5))
plt.ylabel('Number of Users')
plt.xlabel('Support Artists')
plt.title('How people support Artists')


# In[ ]:


#CONTINUE TO WATCH LIVESTREAMS AFTER COVID


# In[52]:


cc_data['ContinueToWatchLivestreams'].value_counts(normalize= True)


# In[ ]:


#QUES 5 IF A PERSON LISTENS TO ALOT OF MUSIC WILL THEY BE LIKELY TO ATTEND SHOW POST PANDEMIC?


# In[119]:


cc_data['HoursOfMusicADay'].value_counts().to_frame()


# In[53]:


cc_data['VaccineLikelinessAttendingShows'].value_counts(normalize=True)


# In[120]:


cc_data['VaccineLikelinessAttendingShows'].value_counts().to_frame()


# In[124]:


#get data columns
df_attendShows=cc_data[['HoursOfMusicADay','VaccineLikelinessAttendingShows']]


# In[131]:


#group by 
df_group1=df_attendShows.groupby(['VaccineLikelinessAttendingShows'],as_index=False).mean()

df_group1


# In[ ]:


#conclusion = ppl who listen to more music have higher likeliness to  attend shows


# In[137]:


#QUES 6 how will ppl want to have memories of concerts 


# In[138]:


#get data columns
df_memories=cc_data[['ShareConcertsSocialMedia','FutureConcertMomentos','ConcertPostsOnSocialMedia','BuyMerchPostPandemic']]


# In[141]:


df_memories


# In[154]:


sc=df_memories['ShareConcertsSocialMedia'].value_counts()


# In[155]:


fcm=df_memories['FutureConcertMomentos'].value_counts()


# In[157]:


data = [sc, fcm]

headers = ["ShareConcertsSocialMedia", "FutureConcertMomentos"]

df4 = pd.concat(data, axis=1, keys=headers)
df4


# In[159]:


#plot bar graph for how many people used each way to listen to music
df4.plot(kind='bar', figsize=(13,5))
plt.ylabel('Number of Users')
plt.xlabel('Memories')
plt.title('Will People Want More Memories Post Covid')


# In[160]:


cp=df_memories['ConcertPostsOnSocialMedia'].value_counts()


# In[161]:


bm=df_memories['BuyMerchPostPandemic'].value_counts()


# In[164]:


data = [cp, bm]

headers = ["ConcertPostsOnSocialMedia", "BuyMerchPostPandemic"]

df5 = pd.concat(data, axis=1, keys=headers)
df5


# In[166]:


#plot bar graph for how many people used each way to listen to music
df5.plot(kind='bar', figsize=(13,5))
plt.ylabel('Number of Users')
plt.xlabel('Memories')
plt.title('Frequency of memories Post Covid')


# In[167]:


#Ques 7 HOW WILL PEOPLE TAKE PRECAUTIONS


# In[56]:


#how to get the number for each music way 
cc_data['PrecautionType'].head()


# In[57]:


#split each row based on delimited passed to that function
get_precautions= cc_data['PrecautionType'].str.split(', ', expand=True)
get_precautions.head()


# In[58]:


#stack this dataframe 
precautions = get_precautions.stack().to_frame()
precautions.head()


# In[59]:


precautions.columns=['Type']


# In[60]:


precautions.head()


# In[61]:


precautions.index = ['0','0','0','1','1','2',
                         '3','4','5','5','5', '6',
                        '6','7','8','8','8','9','9','10',
                         '10','12','12','12','13', '15',
                        '15','15','16','16','16','17','17','17','18',
                         '18','19','19','20','20', '21',
                        '21','21','22','22','23','23','23','24','25',
                         '25','26','26','27','29', '30',
                        '31','31','31','32','32','33','33','34','34',
                         '34','35','35','35'
                        ]
precautions


# In[62]:


precautions['Type'].unique()


# In[63]:


dp=precautions['Type'].value_counts().to_frame()
dp


# In[64]:


precautions['Type'].value_counts(normalize=True)


# In[197]:


#bar plot to show which music software is used the most
dp.plot(kind='bar',figsize=(14,5), color='#04B404')
plt.title('Type of Precautions Wanted')
plt.xlabel('Precaution Type')
plt.ylabel('Count of Users')


# In[65]:


#Will people continue taking precautions?
cc_data['PrecautionsOrRegular'].value_counts().to_frame()


# In[66]:



cc_data['SuggestedVenuePrecautions'].head()


# In[67]:


#split each row based on delimited passed to that function
get_venuePre= cc_data['SuggestedVenuePrecautions'].str.split(', ', expand=True)
get_venuePre.head()


# In[68]:


#stack this dataframe 
venuePre = get_venuePre.stack().to_frame()
venuePre.head()


# In[69]:


venuePre.columns=['Type']


# In[70]:


venuePre.index = ['0','0','0','1','2','3',
                         '4','5','5','5','6', '6',
                        '7','8','8','9','10','11','12','13',
                         '14','15','16','17','18', '19',
                        '20','21','21','22','22','23','23','24','24',
                         '24','25','26','26','27', '27',
                        '27','28','29','29','30','30','31','31','32',
                         '33','34','35','36','36'
                        ]


# In[71]:


dv=venuePre['Type'].value_counts().to_frame()
dv


# In[73]:


venuePre['Type'].value_counts(normalize=True)


# In[72]:


#bar plot to show which music software is used the most
dv.plot(kind='bar',figsize=(14,5), color='blue')
plt.title('Type of Precautions Wanted for Venues')
plt.xlabel('Precaution Type')
plt.ylabel('Count of Users')


# In[222]:


get_artists= cc_data['ArtistsToSee'].str.split(', ', expand=True)
get_artists.head()


# In[224]:


#stack this dataframe 
artists_tosee = get_artists.stack().to_frame()


# In[225]:


artists_tosee.columns=['Artists']


# In[228]:


artists_tosee.index = ['0','0','1','1','2','3',
                         '4','5','5','6','7', '8',
                        '9','9','10','11','12','13','14','15','16','17','18', '19',
                        '20','21','22','23','23','23','23','23',
                         '24','25','26','27','28', '29',
                        '30','31','32','32','32','32','33','34','35','36'
                        ]


# In[229]:


da=artists_tosee['Artists'].value_counts().to_frame()
da


# In[231]:


#bar plot to show which music software is used the most
da.plot(kind='bar',figsize=(14,5), color='purple')
plt.title('Which Artists People Want to See Post Covid')
plt.xlabel('Artists')
plt.ylabel('Count of Users')


# In[240]:


get_generes= cc_data['Genres'].str.split(', ', expand=True)
get_generes.head()


# In[242]:


#stack this dataframe 
genres = get_generes.stack().to_frame()
genres


# In[259]:


genres.columns=['Genres']


# In[260]:


genres.index = ['0','0','0','0','1','1',
                         '1','1','2','2','2', '2',
                        '2','2','2','3','4','5','5','5','6','6','6', '6',
                        '7','7','7','8','8','9','9','9',
                         '9','10','10','10','10', '11',
                        '11','11','11','11','11','12','12','12','12','13','13','14','14','15','16','16','16'
                     ,'16','17','17','17','17','18','18','18','19','19','19','19','20','20','21','21','21','22','22'
                ,'22','22','22','23','23','24','24','24','24','25','25','25','25','25','26','26','26','26','27','27','27','27'
                ,'28','28','28','28','28','28','28','29','29','30','31','31','31','31','32','32','32','32','33','33','33',
                '33','33','34','35','35','36','36','36'
                        ]


# In[261]:


dg=genres['Genres'].value_counts().to_frame()
dg


# In[262]:


#bar plot to show which music software is used the most
dg.plot(kind='bar',figsize=(14,5), color='purple')
plt.title('Genres')
plt.xlabel('Genres')
plt.ylabel('Count of Users')


# In[ ]:




