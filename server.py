from flask import Flask, render_template, request
import datetime
import requests

date = datetime.datetime.now().today().date()
posts_data = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
print(posts_data)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=posts_data, date=date)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<post_id>")
def post(post_id):
    return render_template("post.html", post_id=post_id, post=posts_data[int(post_id) - 1], date=date)

@app.route("/form_entry")
def receive_data():
    pass

if __name__ == "__main__":
    app.run(debug=True)