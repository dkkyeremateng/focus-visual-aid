from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    data = requests.get('http://dev.waziup.io:800/api/v1/domains/waziup/sensors/Kumasi_Hive_One_Sensor71')

    data_json = data.json()
    measurements = data_json.get('measurements')

    return render_template('index.html', measurements=measurements)


if __name__ == '__main__':
    app.run(debug=True)
