from flask import Flask

app = Flask(__name__)
count=0
@app.route("/")
def hello_world():
    global count
    count=count+1
    return f"<p>Hello world! You have requested this endpoint {count} times </p>"