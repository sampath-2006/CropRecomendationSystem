import pandas as pd
from preprocessing import preprocess_data
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,classification_report
import joblib

crop = pd.read_csv(r"D:\CropRecomendationSystem\CropRecomendationSystem\data\Crop_recommendation.csv")

x_train,x_test,y_train,y_test = preprocess_data(crop)


#DDICTIONARY OF MODELS

models = {
    "LR":LogisticRegression(max_iter=2000),
    "DT":DecisionTreeClassifier(),
    "RF":RandomForestClassifier(),
    "KNN":KNeighborsClassifier(),
    "SVM":SVC()    
}

result = {}

for name,model in models.items():
    model.fit(x_train,y_train)
    predictions = model.predict(x_test)
    acc = accuracy_score(y_test,predictions)
    result[name] = acc
    print(f"accuracy of {name} is {result[name]*100}%")
    

best_model = max(result,key=result.get)
print(f"best model is {best_model}")

final_model = models[best_model]
final_model.fit(x_train,y_train)

 
#8309023750
joblib.dump(final_model,'model.pkl')

print(classification_report(y_true=y_test,y_pred = predictions))
    
