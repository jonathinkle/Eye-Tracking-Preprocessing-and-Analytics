#!/usr/bin/python

# import libraries ========
import pandas as pd
import os
import numpy as np
# =========================

# store data paths
demo_path = "/Users/jaw69/Desktop/Demos-Surveys/Demographic_data.csv"
survey_path = "/Users/jaw69/Desktop/Demos-Surveys/Questionnaires_and_Stimuli_Ratings.csv"
beh_path = "/Users/jaw69/Desktop/Demos-Surveys/data/beh/"

# import .csv files into pandas data frames
demos = pd.DataFrame.from_csv(path=demo_path,header=1,sep=',')
surveys = pd.DataFrame.from_csv(path=survey_path,header=1,sep=',')

# rename columns for easier indexing
demos.columns = ['ResponseSet','Name','ExRef','Email','IP','Status','StartDate',
                 'EndDate','Finished','Px','Sex','Age','BirthCountry','BirthCountryText',
                 'UScitizen','otherCitizen','USlength','USlengthText','AfricanAmerican',
                 'AmericanIndian','AsianAmerican','HispanicLatino','WhiteCaucasian',
                 'OtherEthnicity','OtherEthnicityText','NatlAffiliation','FoodAllergies',
                 'WeightLossDiet','DietText','HoursSinceEating','HungerRating',
                 'LocationLat','LocationLong','LocationAcc']#,'Unnamed']
# for sex variable, 1 is male, 2 is female
# for weight loss diet, 1 is yes, 2 is no
                 
# rename columns for easier indexing                 
surveys.columns = ['ResponseSet','Name','ExRef','Email','IP','Status','StartDate',
                   'EndDate','Finished','InstrText','Px',
                   'apple','apple.eaten','apple.taste','apple.health','apple.freq','apple.want',
                   'chewybar','chewybar.eaten','chewybar.taste','chewybar.health','chewybar.freq','chewybar.want',
                   'applechips','applechips.eaten','applechips.taste','applechips.health','applechips.freq','applechips.want',
                   'fignewtons','fignewtons.eaten','fignewtons.taste','fignewtons.health','fignewtons.freq','fignewtons.want',
                   'animals','animals.eaten','animals.taste','animals.health','animals.freq','animals.want',
                   'edamame','edamame.eaten','edamame.taste','edamame.health','edamame.freq','edamame.want',
                   'snickers','snickers.eaten','snickers.taste','snickers.health','snickers.freq','snickers.want',
                   'pretzels','pretzels.eaten','pretzels.taste','pretzels.health','pretzels.freq','pretzels.want',
                   'gummys','gummys.eaten','gummys.taste','gummys.health','gummys.freq','gummys.want',
                   'pbcrackers','pbcrackers.eaten','pbcrackers.taste','pbcrackers.health','pbcrackers.freq','pbcrackers.want',
                   'lays','lays.eaten','lays.taste','lays.health','lays.freq','lays.want',
                   'trailmix','trailmix.eaten','trailmix.taste','trailmix.health','trailmix.freq','trailmix.want',
                   'doritos','doritos.eaten','doritos.taste','doritos.health','doritos.freq','doritos.want',
                   'banana','banana.eaten','banana.taste','banana.health','banana.freq','banana.want',
                   'naturevalley','naturevalley.eaten','naturevalley.taste','naturevalley.health','naturevalley.freq','naturevalley.want',
                   'popcorn','popcorn.eaten','popcorn.taste','popcorn.health','popcorn.freq','popcorn.want',
                   'kitkat','kitkat.eaten','kitkat.taste','kitkat.health','kitkat.freq','kitkat.want',
                   'sunseeds','sunseeds.eaten','sunseeds.taste','sunseeds.health','sunseeds.freq','sunseeds.want',
                   'goldfish','goldfish.eaten','goldfish.taste','goldfish.health','goldfish.freq','goldfish.want',
                   'popchips','popchips.eaten','popchips.taste','popchips.health','popchips.freq','popchips.want',
                   'almonds','almonds.eaten','almonds.taste','almonds.health','almonds.freq','almonds.want',
                   'orange','orange.eaten','orange.taste','orange.health','orange.freq','orange.want',
                   'oreos','oreos.eaten','oreos.taste','oreos.health','oreos.freq','oreos.want',
                   'pistachios','pistachios.eaten','pistachios.taste','pistachios.health','pistachios.freq','pistachios.want',
                   'cheetos','cheetos.eaten','cheetos.taste','cheetos.health','cheetos.freq','cheetos.want',
                   'snickers_HRank','chewybar_HRank','apple_HRank','naturevalley_HRank',
                   'cheetos_HRank','lays_HRank','gummys_HRank','popcorn_HRank','popchips_HRank',
                   'kitkat_HRank','oreos_HRank','banana_HRank','pretzels_HRank',
                   'pistachios_HRank','edamame_HRank','trailmix_HRank','orange_HRank',
                   'sunseeds_HRank','goldfish_HRank','animals_HRank','almonds_HRank',
                   'pbcrackers_HRank','fignewtons_HRank','applechips_HRank','doritos_HRank',
                   'snickers_TRank','chewybar_TRank','apple_TRank','naturevalley_TRank',
                   'cheetos_TRank','lays_TRank','gummys_TRank','popcorn_TRank','popchips_TRank',
                   'kitkat_TRank','oreos_TRank','banana_TRank','pretzels_TRank',
                   'pistachios_TRank','edamame_TRank','trailmix_TRank','orange_TRank',
                   'sunseeds_TRank','goldfish_TRank','animals_TRank','almonds_TRank',
                   'pbcrackers_TRank','fignewtons_TRank','applechips_TRank','doritos_TRank',
                   'snickers_WRank','chewybar_WRank','apple_WRank','naturevalley_WRank',
                   'cheetos_WRank','lays_WRank','gummys_WRank','popcorn_WRank','popchips_WRank',
                   'kitkat_WRank','oreos_WRank','banana_WRank','pretzels_WRank',
                   'pistachios_WRank','edamame_WRank','trailmix_WRank','orange_WRank',
                   'sunseeds_WRank','goldfish_WRank','animals_WRank','almonds_WRank',
                   'pbcrackers_WRank','fignewtons_WRank','applechips_WRank','doritos_WRank',                 
                   'itunes','itunes.enjoy','itunes.use','itunes.freq','itunes.want',
                   'stubhub','stubhub.enjoy','stubhub.use','stubhub.freq','stubhub.want',
                   'target','target.enjoy','target.use','target.freq','target.want',
                   'walmart','walmart.enjoy','walmart.use','walmart.freq','walmart.want',
                   'staples','staples.enjoy','staples.use','staples.freq','staples.want',
                   'redbox','redbox.enjoy','redbox.use','redbox.freq','redbox.want',
                   'jiffylube','jiffylube.enjoy','jiffylube.use','jiffylube.freq','jiffylube.want',
                   'faa','faa.enjoy','faa.use','faa.freq','faa.want',
                   'dominos','dominos.enjoy','dominos.use','dominos.freq','dominos.want',
                   'cvs','cvs.enjoy','cvs.use','cvs.freq','cvs.want',
                   'amc','amc.enjoy','amc.use','amc.freq','amc.want',
                   'bn','bn.enjoy','bn.use','bn.freq','bn.want',
                   'walmart_ERank','jiffylube_ERank','itunes_ERank','redbox_ERank','target_ERank','faa_ERank',
                   'amc_ERank','bn_ERank','cvs_ERank','dominos_ERank','stubhub_ERank','staples_ERank',
                   'walmart_URank','jiffylube_URank','itunes_URank','redbox_URank','target_URank','faa_URank',
                   'amc_URank','bn_URank','cvs_URank','dominos_URank','stubhub_URank','staples_URank',
                   'walmart_WRank','jiffylube_WRank','itunes_WRank','redbox_WRank','target_WRank','faa_WRank',
                   'amc_WRank','bn_WRank','cvs_WRank','dominos_WRank','stubhub_WRank','staples_WRank',
                   'BIS','BIS.1','BIS.2','BIS.3','BIS.4','BIS.5','BIS.6','BIS.7','BIS.8','BIS.9','BIS.10','BIS.11','BIS.12','BIS.13','BIS.14','BIS.15',
                   'BIS.16','BIS.17','BIS.18','BIS.19','BIS.20','BIS.21','BIS.22','BIS.23','BIS.24','BIS.25','BIS.26','BIS.27','BIS.28','BIS.29','BIS.30',
                   'SCS','SCS.1','SCS.2','SCS.3','SCS.4','SCS.5','SCS.6','SCS.7','SCS.8','SCS.9','SCS.10',
                   'SCS.11','SCS.12','SCS.13','SCS.14','SCS.15','SCS.16','SCS.17','SCS.18','SCS.19','SCS.20',
                   'SCS.21','SCS.22','SCS.23','SCS.24','SCS.25','SCS.26','SCS.27','SCS.28','SCS.29','SCS.30',
                   'SCS.31','SCS.32','SCS.33','SCS.34','SCS.35','SCS.36','SCS.37','SCS.38',
                   'BISBAS','BISBAS.1','BISBAS.2','BISBAS.3','BISBAS.4','BISBAS.5','BISBAS.6','BISBAS.7','BISBAS.8','BISBAS.9','BISBAS.10',
                   'BISBAS.11','BISBAS.12','BISBAS.13','BISBAS.14','BISBAS.15','BISBAS.16','BISBAS.17','BISBAS.18','BISBAS.19','BISBAS.20',
                   'BISBAS.21','BISBAS.22','BISBAS.23','BISBAS.24','BISBAS.25',
                   'EAT','EAT.1','EAT.2','EAT.3','EAT.4','EAT.5','EAT.6','EAT.7','EAT.8','EAT.9','EAT.10','EAT.11','EAT.12','EAT.13','EAT.14',
                   'EAT.15','EAT.16','EAT.17','EAT.18','EAT.19','EAT.20','EAT.21','EAT.22','EAT.23','EAT.24','EAT.25','EAT.26',
                   'Health.1','Health.2','Health.3','Health.4','Health.5','Health.6',
                   'Max.1','Max.2','Max.3','Max.4','Max.5','Max.6','Max.7','Max.8','Max.9','Max.10','Max.11','Max.12','Max.13',
                   'LocationLat','LocationLong','LocationAcc']#,'unnamed']

# function to replace 1s and 7s as 2s and 6s
f = lambda x: {1:2,7:6}.get(x,x) - 1

# compress chewybar.taste column
surveys['chewybar.taste'] = surveys['chewybar.taste'].apply(f)

item = ["applechips","oreos","lays","animals","kitkat","pistachios","pretzels","gummys","banana","snickers","trailmix","popcorn","naturevalley","edamame","orange","almonds","sunseeds","doritos","popchips","pbcrackers","fignewtons","cheetos","chewybar","apple","goldfish"]
mean_salience = [1.8297,2.7789,2.9525,1.7939,2.6336,2.0572,2.7719,3.4962,2.2509,2.8141,3.7722,1.7959,2.893,2.6522,3.7306,3.7699,3.6107,2.7088,3.6016,3.8724,4.3858,4.5497,4.5941,4.8961,5.6011] 
mean_NZ_salience = [33.1414,36.6935,37.8168,38.7447,39.893,41.1788,41.9956,42.9191,44.4421,45.0561,45.7403,47.8104,48.1152,51.1988,51.2374,51.7608,53.2404,53.3807,58.1236,60.1454,60.4417,60.9437,60.9822,64.0292,64.2261] 
median_NZ_salience = [13,19,20,18,20,16,16,26,22,32,23,11,21,33,25,26,26,27,31,43,47,55,35,40,54] 
price = [1.0,0.63,0.41,0.37,0.66,1.08,0.46,0.50,0.16,0.79,1.09,0.72,0.43,2.27,0.77,0.57,0.79,0.41,0.80,0.38,1.04,0.41,2.96,0.24,0.33]
calories = [50,270,240,130,210,120,160,70,105,250,160,100,190,130,45,100,150,240,100,190,100,310,100,80,200]

d = {'item' : item,
     'mean_salience' : mean_salience,
     'mean_NZ_salience' : mean_NZ_salience,
     'median_NZ_salience' : median_NZ_salience,
     'price' : price,
     'calories' : calories}

salience_df = pd.DataFrame(d)

# =====================================================================================================================

print 'rename columns done...'

# =====================================================================================================================

tmp_surveys = surveys

# select only data that comes from participants, not test, NAs, or otherwise
demos = demos.dropna(subset=['Px'], how='any')
demos = demos[demos['Px'].str.contains("|".join(['Px','px','pX','PX']))] # RAs don't put the 'Px' in consistently, so catch all variations
surveys = surveys.dropna(subset=['Px'], how='any')
surveys = surveys[surveys['Px'].str.contains("|".join(['Px','px','pX','PX']))]

# remove known particpants with data issues from the data frame
demos = demos[demos.Px != 'Px03']
surveys = surveys[surveys.Px != 'Px03']

# strip 'Px' from participant ids and convert to numeric; this makes for easier indexing by participant later on
demos['Px'] = demos['Px'].str.slice(start=2,stop=4).convert_objects(convert_numeric=True)
surveys['Px'] = surveys['Px'].str.slice(start=2,stop=4).convert_objects(convert_numeric=True)

# =====================================================================================================================

print 'demos and survey manipulations done...'

# Sort and score survey measures ======================================================================================

Px_ids = pd.Series(surveys[['Px']].Px)

# use Chris Coutlee's ABIS
ABIS_attention = surveys[['BIS.5','BIS.8','BIS.9','BIS.12','BIS.20']].mean(axis=1)

ABIS_motor = surveys[['BIS.2','BIS.14','BIS.17','BIS.19']].mean(axis=1)

ABIS_nonplanning = surveys[['BIS.1','BIS.7','BIS.13','BIS.30']].mean(axis=1)

SCS = surveys[['SCS.1','SCS.2','SCS.3','SCS.4','SCS.5','SCS.6','SCS.7','SCS.8','SCS.9','SCS.10',
               'SCS.11','SCS.12','SCS.13','SCS.14','SCS.15','SCS.16','SCS.17','SCS.18','SCS.19','SCS.20',
               'SCS.21','SCS.22','SCS.23','SCS.24','SCS.25','SCS.26','SCS.27','SCS.28','SCS.29','SCS.30',
               'SCS.31','SCS.32','SCS.33','SCS.34','SCS.35','SCS.36','SCS.37','SCS.38']].sum(axis=1)          
         
BISBAS = surveys[['BISBAS.1','BISBAS.2','BISBAS.3','BISBAS.4','BISBAS.5','BISBAS.6','BISBAS.7','BISBAS.8','BISBAS.9','BISBAS.10',
                  'BISBAS.11','BISBAS.12','BISBAS.13','BISBAS.14','BISBAS.15','BISBAS.16','BISBAS.17','BISBAS.18','BISBAS.19','BISBAS.20',
                  'BISBAS.21','BISBAS.22','BISBAS.23','BISBAS.24','BISBAS.25']]     

EAT = surveys[['EAT.1','EAT.2','EAT.3','EAT.4','EAT.5','EAT.6','EAT.7','EAT.8','EAT.9','EAT.10','EAT.11','EAT.12','EAT.13','EAT.14',
               'EAT.15','EAT.16','EAT.17','EAT.18','EAT.19','EAT.20','EAT.21','EAT.22','EAT.23','EAT.24','EAT.25','EAT.26']]
EAT = EAT.subtract(2,axis=1)
EAT = EAT.replace(to_replace=[-1],value=0)
EAT = EAT.sum(axis=1)                       
               
# higher score means more health conscious               
HealthConsc = surveys[['Health.1','Health.2','Health.3','Health.4','Health.5','Health.6']]
HealthConsc = HealthConsc.mean(axis=1)

Maximization = surveys[['Max.1','Max.2','Max.3','Max.4','Max.5','Max.6','Max.7','Max.8','Max.9','Max.10','Max.11','Max.12','Max.13']].mean(axis=1)

column_names = ['Px','ABIS_attention','ABIS_motor','ABIS_nonplanning','SCS','EAT','HealthConsc','Max']

survey_scores = pd.DataFrame({'Px' : Px_ids,
                              'ABIS_attention' : ABIS_attention,
                              'ABIS_motor' : ABIS_motor,
                              'ABIS_nonplanning' : ABIS_nonplanning,
                              'SCS' : SCS,
                              'EAT' : EAT,
                              'HealthConsc' : HealthConsc,
                              'Maximization' : Maximization})

survey_scores.to_csv('SurveyScores.csv',sep=',',header=column_names)

# =====================================================================================================================

print 'survey scoring done...'

# Import behavioral data and append survey scores and stimuli ratings/rankings ========================================

# empty list to store imported data
frames = []

# import data from csv files
for datafile in os.listdir(beh_path):
    frames.append(pd.read_csv(os.path.join(beh_path,datafile), header=0, delim_whitespace=True))
    
# concatenate data loaded into frames    
beh_data = pd.concat(frames) 

# empty frames list
frames = []

# add in placeholders for salience ratings, price, and calories
beh_data['d_mean_salience'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['d_meanNZ_salience'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['d_medianNZ_salience'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['d_price'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['d_calories'] = np.repeat(np.nan,len(beh_data),axis=0)

# add in placeholders for food rating variables; d means 'delta'
beh_data['d_HealthRank'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['d_HealthRate'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['d_TasteRank'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['d_TasteRate'] = np.repeat(np.nan,len(beh_data),axis=0)

# add in placeholders for non-food rating variables; d means 'delta'
beh_data['d_EnjoyRank'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['d_EnjoyRate'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['d_UseRank'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['d_UseRate'] = np.repeat(np.nan,len(beh_data),axis=0)

# add in placeholders for food and non-food want ranking/rating variables
beh_data['d_WantRank'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['d_WantRate'] = np.repeat(np.nan,len(beh_data),axis=0)

# add in placeholders for survey measures
beh_data['ABIS_attention'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['ABIS_motor'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['ABIS_nonplanning'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['SCS'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['EAT'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['HealthConsc'] = np.repeat(np.nan,len(beh_data),axis=0)
beh_data['Maximization'] = np.repeat(np.nan,len(beh_data),axis=0)

# loops through subsets of data split by groupby value (in this case, 'Px')
# n is value from column
# g is the subset of rows with the value n from 'Px'
# in the future, replace sub-loops with series-wide operations for speed
for n,g in beh_data.groupby('Px'):
    # only concatenate data if survey data exists for participant
    if n in surveys.Px.values:
        # some subjects don't have all the food trials, adjust the range for loops accordingly    
        if g[g.Phase=='food'].shape[0] == 276:
            food_max = 276
            nfood_max = 342
        else:
            food_max = 300
            nfood_max = 366
        # begin concatenation loops to join trial-specific survey data to behavioral data
        for row in range(food_max):
            #try:
            g['d_HealthRank'][row] = -1 * (surveys[surveys.Px==n][(g.Left_Item[row] + '_HRank')].values - surveys[surveys.Px==n][(g.Right_Item[row] + '_HRank')].values)
            g['d_HealthRate'][row] = surveys[surveys.Px==n][(g.Left_Item[row] + '.health')].values - surveys[surveys.Px==n][(g.Right_Item[row] + '.health')].values
            g['d_TasteRank'][row] = -1 * (surveys[surveys.Px==n][(g.Left_Item[row] + '_TRank')].values - surveys[surveys.Px==n][(g.Right_Item[row] + '_TRank')].values)
            g['d_TasteRate'][row] = surveys[surveys.Px==n][(g.Left_Item[row] + '.taste')].values - surveys[surveys.Px==n][(g.Right_Item[row] + '.taste')].values
            g['d_WantRank'][row] = -1 * (surveys[surveys.Px==n][(g.Left_Item[row] + '_WRank')].values - surveys[surveys.Px==n][(g.Right_Item[row] + '_WRank')].values)
            g['d_WantRate'][row] = surveys[surveys.Px==n][(g.Left_Item[row] + '.want')].values - surveys[surveys.Px==n][(g.Right_Item[row] + '.want')].values
            g['d_mean_salience'][row] =  salience_df.mean_salience[salience_df.item == g.Left_Item[row]].values - salience_df.mean_salience[salience_df.item == g.Right_Item[row]].values
            g['d_meanNZ_salience'][row] = salience_df.mean_NZ_salience[salience_df.item == g.Left_Item[row]].values - salience_df.mean_NZ_salience[salience_df.item == g.Right_Item[row]].values
            g['d_medianNZ_salience'][row] = salience_df.median_NZ_salience[salience_df.item == g.Left_Item[row]].values - salience_df.median_NZ_salience[salience_df.item == g.Right_Item[row]].values
            g['d_price'][row] = salience_df.price[salience_df.item == g.Left_Item[row]].values - salience_df.price[salience_df.item == g.Right_Item[row]].values
            g['d_calories'][row] = salience_df.calories[salience_df.item == g.Left_Item[row]].values - salience_df.calories[salience_df.item == g.Right_Item[row]].values
            g['ABIS_attention'][row] = survey_scores.ABIS_attention[survey_scores.Px==n].values
            g['ABIS_motor'][row] = survey_scores.ABIS_motor[survey_scores.Px==n].values
            g['ABIS_nonplanning'][row] = survey_scores.ABIS_nonplanning[survey_scores.Px==n].values
            g['SCS'][row] = survey_scores.SCS[survey_scores.Px==n].values
            g['EAT'][row] = survey_scores.EAT[survey_scores.Px==n].values
            g['HealthConsc'][row] = survey_scores.HealthConsc[survey_scores.Px==n].values
            g['Maximization'][row] = survey_scores.Maximization[survey_scores.Px==n].values
            #except Exception:
            #    pass
        for row in range(food_max,nfood_max):
            #try:
            g['d_EnjoyRank'][row] = -1 * (surveys[surveys.Px==n][(g.Left_Item[row] + '_ERank')].values - surveys[surveys.Px==n][(g.Right_Item[row] + '_ERank')].values)
            g['d_EnjoyRate'][row] = surveys[surveys.Px==n][(g.Left_Item[row] + '.enjoy')].values - surveys[surveys.Px==n][(g.Right_Item[row] + '.enjoy')].values
            g['d_UseRank'][row] = -1 * (surveys[surveys.Px==n][(g.Left_Item[row] + '_URank')].values - surveys[surveys.Px==n][(g.Right_Item[row] + '_URank')].values)
            g['d_UseRate'][row] = surveys[surveys.Px==n][(g.Left_Item[row] + '.use')].values - surveys[surveys.Px==n][(g.Right_Item[row] + '.use')].values
            g['d_WantRank'][row] = -1 * (surveys[surveys.Px==n][(g.Left_Item[row] + '_WRank')].values - surveys[surveys.Px==n][(g.Right_Item[row] + '_WRank')].values)
            g['d_WantRate'][row] = surveys[surveys.Px==n][(g.Left_Item[row] + '.want')].values - surveys[surveys.Px==n][(g.Right_Item[row] + '.want')].values
            g['ABIS_attention'][row] = survey_scores.ABIS_attention[survey_scores.Px==n].values
            g['ABIS_motor'][row] = survey_scores.ABIS_motor[survey_scores.Px==n].values
            g['ABIS_nonplanning'][row] = survey_scores.ABIS_nonplanning[survey_scores.Px==n].values
            g['SCS'][row] = survey_scores.SCS[survey_scores.Px==n].values
            g['EAT'][row] = survey_scores.EAT[survey_scores.Px==n].values
            g['HealthConsc'][row] = survey_scores.HealthConsc[survey_scores.Px==n].values
            g['Maximization'][row] = survey_scores.Maximization[survey_scores.Px==n].values
            #except Exception:
            #    pass
        frames.append(g)
    
beh_data = pd.concat(frames)

# remove mysterious 'Unnamed' columns from data
beh_data = beh_data.drop(['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6'], axis=1)

# =====================================================================================================================

print 'combine surveys and behavior done...'

# =====================================================================================================================

# export data for Lucie to analyze
#beh_data.to_stata('Behavioral_Data_for_Lucie.dta')
beh_data.to_excel('Clean_Behavioral_Data.xlsx', sheet_name='Sheet1')
#surveys.to_stata('Survey_Data_for_Lucie.dta')
surveys.to_excel('Clean_Survey_Data.xlsx', sheet_name='Sheet1')

print 'export done...'

print 'Data mashing complete'