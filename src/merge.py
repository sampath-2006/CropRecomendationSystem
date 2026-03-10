import pandas as pd


crop = pd.read_csv(r"D:\CropRecomendationSystem\CropRecomendationSystem\data\Crop_recommendation.csv")
yeild = pd.read_csv(r"D:\CropRecomendationSystem\CropRecomendationSystem\data\crop_yield.csv")

#print(crop.head())
#print(yeild.head())

crop = crop[['N','P','K','temperature','humidity','ph','rainfall','label']]
yeild = yeild[['crop','state','year','season','production']]

yeild.rename(columns={'crop':'label'}, inplace=True)

crop['label'] = crop['label'].str.lower()
yeild['label'] = crop['label'].str.lower()

crop['label'] = crop['label'].str.strip()
yeild['label'] = crop['label'].str.strip()

data = pd.merge(crop,yeild,on='label',how = 'inner')

print(crop['label'].unique())
print(yeild['label'].unique())

#print(data.head())
print(data.shape)

# we use only Crop_recomendation.csv data set to train the model and we use the other data set for analysis


