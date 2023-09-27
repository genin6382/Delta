from flask import Flask
count=0
app = Flask(__name__)
@app.route("/")
def hello_world():
    global count
    count+=1
    dic = {"repsone":"Hello world" , "timesRequested":count}
    return dic