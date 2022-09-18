
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from ml_news_core import similarNews

app = Flask(__name__)

@app.route("/")
def index():
    return "Machine Learning API for Balanced News Summary" # Just updating my code

@app.route("/ml-related-news",methods=["GET"])
def api():
    args = request.args
    return args