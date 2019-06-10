#Note:
#Please follow the below link to understand the app better.
#https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/

#to be done
# need to include sample viz
# https://www.fullstackpython.com/blog/responsive-bar-charts-bokeh-flask-python-3.html
# need to include a connection to a DB 
# need to figure out the tutorial

from flask import Flask, render_template    

from flask_azure_oauth import FlaskAzureOauth

app = Flask(__name__)

app.config['AZURE_OAUTH_TENANCY'] = 'xxx'
app.config['AZURE_OAUTH_APPLICATION_ID'] = 'xxx'
app.config['AZURE_OAUTH_CLIENT_APPLICATION_IDS'] = ['xxx']

auth = FlaskAzureOauth()
auth.init_app(app=app)

@app.route('/unprotected')
def unprotected():
    return 'hello world'


@app.route('/protected')
@auth()
def protected():
    return 'hello authenticated entity'

@app.route('/protected-with-single-scope')
@auth('required-scope')
def protected_with_scope():
    return 'hello authenticated and authorised entity'

@app.route('/protected-with-multiple-scopes')
@auth('required-scope1 required-scope2')
def protected_with_multiple_scopes():
    return 'hello authenticated and authorised entity'

@app.route("/")
def home():
   return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)





