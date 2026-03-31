from flask import Flask, render_template, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://rr8807837_db_user:raja44raja@cluster0.jstxelp.mongodb.net/")
db = client["studywithR"]
collection = db["reviews"]

@app.route("/")
def index():
   return render_template("index.html", msg="")

# account Page
@app.route("/account")
def account():
    return render_template("account.html")

# IT Infrastructure Page
@app.route("/itinfra")
def itinfra():
    return render_template("itinfra.html")

# MongoDB Page
@app.route("/mongo")
def mongo():
    return render_template("mongo.html")

# Process Page
@app.route("/process")
def process():
    return render_template("process.html")

# English Page
@app.route("/english")
def english():
    return render_template("english.html")

# English1 Page
@app.route("/english1")
def english1():
    return render_template("english1.html")

# EDA Page
@app.route("/eda")
def eda():
    return render_template("eda.html")

# Cloud Computing Page
@app.route("/cloudcomputing")
def cloudcomputing():
    return render_template("cloudcomputing.html")

# Review Page
@app.route("/review")
def review():
    return render_template("review.html")

@app.route("/save", methods=["POST"])
def save():
    text = request.form.get("text")
    review = request.form.get("review")
    rating= request.form.get("rating")
    if text:
        collection.insert_one({"name": text, "review": review, "rating": rating})
        message = "Saved successfully!"
    else:
        message = "Please enter your name, review, and rating"

    return render_template("review.html", msg=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))