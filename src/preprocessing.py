import pandas as pd
import matplotlib as plt
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split


crop = pd.read_csv(r"D:\CropRecomendationSystem\CropRecomendationSystem\data\Crop_recommendation.csv")

print(crop.shape)
#print(crop.head())

#print(crop.info())

#print(crop.isnull().sum())
#no missing values found

#print(crop.duplicated().sum())
#no duplicate rows found

#distribution of data
#print(crop.describe())


#detection of outiliers
#crop.boxplot(figsize=(10,6))

def preprocess_data(crop):

    x = crop.drop('label',axis = 1)
    y = crop['label']

    #ADDING NEW FEATURES AS THERE ARE VERY LESS FEATURES

    #NUTRIENT RATIOS
    x['np_ratio'] = x['N']/x['P'] 
    x['nk_ratio'] = x['N']/x['K']
    x['pk_ratio'] = x['P']/x['K']

    #NUTRIENT SUM
    x['nutrient_sum'] = x['N'] + x['P'] + x['K']

    

    #WEATHERICAL CONDITIONS
    x['temp_humidity'] = x['temperature'] * x['humidity']
    x['temp_rainfall'] = x['temperature'] * x['rainfall']
    x['humidity_rainfall'] = x['humidity'] * x['rainfall']


    le = LabelEncoder()
    y = le.fit_transform(y)

    ss = StandardScaler()
    x = ss.fit_transform(x)

    x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=42,test_size=0.2)

    #print(x_train.shape)
    #print(x_test.shape)
    #print(y_train.shape)
    #print(y_test.shape)
    return x_train,x_test,y_train,y_test




