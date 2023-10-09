from flask import Flask

# a minimal flask app for testting a feature. Therefor no further commentary
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

app.run(port=8080, debug=True)