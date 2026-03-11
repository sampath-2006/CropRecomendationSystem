import numpy as np
import joblib
import flask

#initialising web server
app = flask.Flask(__name__)

model = joblib.load("src/model.pkl")
label_encoder = joblib.load("src/label_encodel.pkl")

@app.route("/")

def Home():
    return flask.render_template("index.html")

@app.route("/predict",methods = ["POST"])

def predict():
    
    #used for getting the values entered in the front end
    N = float(flask.request.form["N"])
    P = float(flask.request.form["P"])
    K = float(flask.request.form["K"])
    temperature = float(flask.request.form["temperature"])
    humidity = float(flask.request.form["humidity"])
    ph = float(flask.request.form["ph"])
    rainfall = float(flask.request.form["rainfall"])
    
    #feature engineering
    
    np_ratio = N / P
    nk_ratio = N / K
    pk_ratio = P / K
    
    temp_humidity = temperature * humidity
    temp_rainfall = temperature * rainfall
    humidity_rainfall = humidity * rainfall
    
    nutrient_sum = N + P + K
    
    features = np.array([[N,P,K,temperature,humidity,ph,rainfall,np_ratio,nk_ratio,pk_ratio,nutrient_sum,temp_humidity,temp_rainfall,humidity_rainfall]])
    
    ss = joblib.load("src/standard_scaler.pkl")
    features = ss.transform(features)
    
    prediction = model.predict(features)
    
    
    crop = label_encoder.inverse_transform(prediction)[0]
    
    return flask.render_template("index.html",prediction=crop,N=N,P=P,K=K,temperature=temperature,humidity=humidity,ph=ph,rainfall=rainfall)

if __name__ == "__main__":
    app.run(debug = True)
    
    
    




