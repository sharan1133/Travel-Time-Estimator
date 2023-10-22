from flask import Flask, request, render_template
from flask import jsonify
from geopy.geocoders import Nominatim
from jinja2 import Template
import xgboost 
import geocoder
import pandas as pd
import pickle
import datetime
import geopy.distance



#model = pickle.load(open('model.pkl', 'rb'))

#my_model = pickle.load(open('C:\Users\shara\OneDrive\Desktop\Final_Project\XGModel.bin'))
with open("XGModel.bin", 'rb') as file:
    my_model = pickle.load(file)


app = Flask(__name__)


features = ['Source lat' , 'Source long' , 'Dest lat' , 'Dest long' , 'hod' , 'Geodesic Distance']
outcome = ['mean_travel_time']

def get_hour_of_day():
    now = datetime.datetime.now()
    return now.hour

def get_distance(lat1 , long1 , lat2 , long2):
    src_point = (lat1 , long1)
    dest_point = (lat2 , long2)
    return geopy.distance.geodesic(src_point , dest_point).kilometers

def prepare_df(lat1 , long1 , lat2 , long2 , hod):
    distance = get_distance(lat1 , long1 , lat2 , long2)
    return pd.DataFrame(columns = ['Source lat' , 'Source long' , 'Dest lat' , 'Dest long' , 'hod' , 'Geodesic Distance'],
                       data = [[lat1 , long1 , lat2 , long2 , hod , distance]])

def predict(df):
    prediction = my_model.predict(df[features])
    #prediction_json = jsonify(prediction.tolist())
    #prediction_json = {'prediction':prediction}
    #return prediction_json
    #return render_template('index.html' , prediction = prediction)
    prediction_json = {'prediction': prediction}
    return jsonify(prediction_json)
    #return str(prediction[0])


def geocode_addresses(src_address, dest_address):
    geolocator = Nominatim(user_agent="my-application/1.0")
    src_location = geolocator.geocode(src_address)
    src_lat = src_location.latitude
    src_lng = src_location.longitude
    dest_location = geolocator.geocode(dest_address)
    dest_lat = dest_location.latitude
    dest_lng = dest_location.longitude
    return [src_lat, src_lng, dest_lat, dest_lng]


@app.route('/')
def index():
    return render_template('index.html')

'''@app.route('/geocode', methods=['POST'])
def geocode():
    # Extract the input data from the request
    src_address = request.form['src_address']
    dest_address = request.form['dest_address']

    # Geocode the addresses
    coordinates = geocode_addresses(src_address, dest_address)

    # Return the coordinates as a response
    return jsonify(coordinates)'''


@app.route('/predict', methods=['POST'])
def predict_travel_time():
    src_address = request.form['src_address']
    dest_address = request.form['dest_address']
    src_lat, src_lng, dest_lat, dest_lng = geocode_addresses(src_address, dest_address)
    hod = get_hour_of_day()
    df = prepare_df(src_lat, src_lng, dest_lat, dest_lng, hod)
    prediction = my_model.predict(df[features])
    #prediction_json = jsonify(prediction.tolist())
    prediction_json = prediction.tolist()
    data = prediction_json[0]/60
    print(data)
   
    return render_template('index.html', data=data, src_address=src_address, dest_address=dest_address)


if __name__ == '__main__':
    app.run(host='0.0.0.0')