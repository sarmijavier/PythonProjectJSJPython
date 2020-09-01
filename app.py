from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map


app = Flask(__name__, template_folder='templates', static_folder='static')
app = Flask(__name__)
app.config['GOOGLEMAPS_KEY'] = 'AIzaSyDnS4RxGp0v36GNTeTrI_otzjWSS_oLjZc'
bootstrap = Bootstrap(app) 
GoogleMaps(app)


@app.route('/')
def home():
        # creating a map in the view
    mymap =  Map(
        identifier="sndmap",
        lat=4.505980,
        lng=-74.102920,
        markers=[
          {
            'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
            'lat': 4.505980,
            'lng': -74.102920,
            'infobox': "<img src='http://maps.google.com/mapfiles/ms/icons/green-dot.png' >"
          }
        ],
        style="height:500px;width:500px;margin:0;",
    )
    

    return render_template("home.html", mymap=mymap)


if __name__ == "__main__":
    app.run(debug=1)