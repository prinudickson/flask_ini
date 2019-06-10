#Note:
#Please follow the below link to understand the app better.
#https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/

#to be done
# need to include sample viz
# https://www.fullstackpython.com/blog/responsive-bar-charts-bokeh-flask-python-3.html
# need to include a connection to a DB 
# need to figure out the tutorial

from flask import Flask, render_template    

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)





