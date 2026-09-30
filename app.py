from flask import Flask, render_template
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'mapbox_token': os.getenv('MAPBOX_TOKEN', 'your_token_here'),
        'default_lat': os.getenv('DEFAULT_LAT', '40.7128'),
        'default_lng': os.getenv('DEFAULT_LNG', '-74.0060'),
    }
    return render_template('index.html', **context)

@app.route('/sensor')
def sensor():
    context = {
        'default_lat': os.getenv('DEFAULT_LAT', '40.7128'),
        'default_lng': os.getenv('DEFAULT_LNG', '-74.0060'),
    }
    return render_template('index2.html', **context)

if __name__ == '__main__':
    app.run(host=os.getenv('HOST_ADDRESS', 'localhost'), port=int(os.getenv('PORT', 5000)), debug=True)
