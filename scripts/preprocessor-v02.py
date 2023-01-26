#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%%
df = pd.read_csv('../data/raw_data_2.csv',encoding='ISO-8859-1', on_bad_lines='skip',delimiter=';',low_memory=False)
#%%
df.info()
#%%
df.head()
#%%
df['reservation_time'] = df[['foglalas napja','foglalas ideje_oraperc']].apply(' '.join,axis=1)
#%%
df['journey_start_time'] = df[['indulas napja','indulasi ido']].apply(' '.join,axis=1)
#%%
df['ajanlat datuma'] = pd.to_datetime(df['ajanlat datuma'])
#%%
df.rename(columns={'ajanlat datuma':'date_of_offer'},inplace=True)
#%%
df = df.drop('foglalas napja',axis=1)
#%%
df = df.drop('foglalas ideje_oraperc',axis=1)
#%%
df = df.drop('indulas napja',axis=1)
#%%
df = df.drop('indulasi ido',axis=1)
#%%
df['utas regisztracios datuma'] = pd.to_datetime(df['utas regisztracios datuma'])
#%%
df.rename(columns={'utas regisztracios datuma':'passenger_registration_date'},inplace=True)
#%%
df['passenger_birth_date'] = pd.to_datetime(df['utas szuletesi datuma'])
#%%
df = df.drop('utas szuletesi datuma',axis=1)
#%%
df.rename(columns={'foglalt helyek szama':'no_reserver_seats'},inplace=True)
#%%
df.rename(columns={'utas neme':'passenger_gender'},inplace=True)
#%%
pd.get_dummies(df,columns=['passenger_gender'])
#%%
df.rename(columns={'utas kora':'passenger_age'},inplace=True)
#%%
df.rename(columns={'utas foglalkozasa':'passenger_job'},inplace=True)
#%%
df = df.drop('utazas tipusa',axis=1)
#%%
df.rename(columns={'indulas orszaga':'origin_country'},inplace=True)
#%%
df.rename(columns={'indulas varosa':'origin_city'},inplace=True)
#%%
df.rename(columns={'erkezes orszaga':'destination_country'},inplace=True)
#%%
df.rename(columns={'utazas eve':'year_of_trip'},inplace=True)
#%%
df.rename(columns={'erkezes varosa':'destination_city'},inplace=True)
#%%
df.rename(columns={'utdij':'trip_fee'},inplace=True)
#%%
df.rename(columns={'pénznem':'currency'},inplace=True)
#%%
df.rename(columns={'hazai vagy nemzetkozi':'national_or_international'},inplace=True)
#%%
df.rename(columns={'foglalási napok (utazas napja-foglalas napja)':'booking_interval'},inplace=True)
#%%
df.rename(columns={'magan vagy uzleti':'business_or_non_business'},inplace=True)
#%%
df.rename(columns={'autok gyartasi eve':'car_year_of_production'},inplace=True)
#%%
df.rename(columns={'autok életkora':'car_age'},inplace=True)
#%%
df.rename(columns={'max utasszám':'max_no_of_passengers'},inplace=True)
#%%
df.rename(columns={'sofõr szuletesi ideje':'driver_birth_date'},inplace=True)
#%%
df.rename(columns={'sofor reg datuma':'driver_registration_date'},inplace=True)
#%%
df.rename(columns={'sofor neme':'driver_gender'},inplace=True)
#%%
df['driver_birth_date'].isnull().value_counts()
#%%
# dropping driver birthdate, as there are 489,253 missing values
df = df.drop('driver_birth_date',axis=1)
#%%
df['car_age'].value_counts()['#ÉRTÉK!']
#%%
df = df[df.car_age != '#ÉRTÉK!']
#%%
df['car_age'] = pd.to_numeric(df['car_age'])
# dropping the 14 rows, which had car_age == '#ÉRTÉK!'
#%%
df['driver_registration_date'].isnull().value_counts()
# 31,609 rows are missing driver registration date -- as of now I will not drop this column but is unable to convert it to datetime
#%%
df.to_csv('data_preprocessed_v02')