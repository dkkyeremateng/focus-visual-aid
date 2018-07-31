from flask import Flask, render_template
import requests

uri = 'http://dev.waziup.io:800/api/v1/domains/waziup/sensors/Kumasi_Hive_One_Sensor71'


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def index():
        data = requests.get(uri)

        data_json = data.json()
        measurements = data_json.get('measurements')

        return render_template('index.html', measurements=measurements)

    return app
