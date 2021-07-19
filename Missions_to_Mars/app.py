# Import dependencies and set up
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
app = Flask(__name__)

# Using flask_pymongo to set up mongo coneection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars_app'
mongo = PyMongo(app)

# Home
@app.route('/')
def index():
    scraper()
    info = mongo.db.info.find_one()
    return render_template('index.html', info=info)

# 
@app.route('/scrape')
def scraper():
    info = mongo.db.info
    info_data = scrape_mars.scrape()
    info.update({}, info_data, upsert=True)
    return redirect('/', code=302)
if __name__ == '__main__':
    app.run(debug=True)