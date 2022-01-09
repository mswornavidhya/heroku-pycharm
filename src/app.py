from flask import Flask

app = Flask(__name__) # Creating connectivity with app

# to intialize the webapp and when the site is accessed through the link,
# what to be shown is given using <h1>
@app.route("/")
def home_view(): # Give proper intent for this function
    return "<h1>Welcome to Heroku Testing Project</h1>"