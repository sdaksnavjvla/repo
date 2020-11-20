import flask
from flask import request, url_for, render_template, redirect


app = flask.Flask(__name__)

@app.route('/',methods=['GET','POST'])
def my_maps():

  mapbox_access_token = 'pk.eyJ1IjoiYW1vc2FuZHJlaWNhIiwiYSI6ImNraHF1Mzk3OTBiMWwycG10bTdldHRqcG8ifQ.yRwvlAqvEeZMcpjYFrLpAw'

  return render_template('index.html',
        mapbox_access_token=mapbox_access_token)

if __name__ == '__main__':
    app.run(debug=True)