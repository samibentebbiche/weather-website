from flask import render_template, redirect, request, url_for
import requests
from weather import app
from datetime import datetime

@app.route('/',methods=['GET','POST'])
def weather_home():
    if request.method == 'POST':
        place = request.form['place']
        return redirect(url_for('weather',place=place))
    return render_template("index.html")

@app.route('/weather/<place>',methods=['GET','POST'])
def weather(place):
    weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+place+'&units=metric&appid=aae913c5c3a9f7bfdeb9410ef576d901')
    weather_obj = weather.json()

    temp_c = float(weather_obj['main']['temp'])
    temp_min = float(weather_obj['main']['temp_min'])
    temp_max = float(weather_obj['main']['temp_max'])
    humidity = float(weather_obj['main']['humidity'])
    pressure = float(weather_obj['main']['pressure'])
    speed_wind = float(weather_obj['wind']['speed'])
    weather_cond = str(weather_obj['weather'][0]['main'])
    weather_cond_description = str(weather_obj['weather'][0]['description'])
    sun_rise = datetime.fromtimestamp(int(weather_obj['sys']['sunrise'])).strftime('%Y-%m-%d %H:%M:%S')
    sun_set = datetime.fromtimestamp(int(weather_obj['sys']['sunset'])).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('weather.html',place = place , temp_c = temp_c , temp_max=temp_max ,temp_min=temp_min, weather_cond=weather_cond)