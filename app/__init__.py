from importlib.resources import Package
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
    return render_template('index.html', profiles = parsedProfiles, url=os.getenv("URL"))
