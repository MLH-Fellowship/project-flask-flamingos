from importlib_resources import Package
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import json

load_dotenv()
app = Flask(__name__)

with open('app/static/profiles.json') as f:
    parsedProfiles = json.load(f)

@app.route('/')
def index():
    return render_template('about.html', profiles = parsedProfiles, url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', profiles = parsedProfiles, url=os.getenv("URL"))

@app.route('/work-experience')
def experience():
    return render_template('work-experience.html', profiles = parsedProfiles, url=os.getenv("URL"))

@app.route('/education')
def education():
    return render_template('education.html', profiles = parsedProfiles, url=os.getenv("URL"))

@app.route('/places')
def places():
    return render_template('places.html', profiles = parsedProfiles, url=os.getenv("URL"))

@app.route('/contact')
def contact():
    return render_template('contact.html', profiles = parsedProfiles, url=os.getenv("URL"))
