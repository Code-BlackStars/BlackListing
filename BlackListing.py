from flask import Flask, render_template, url_for,flash,redirect
from forms import RegistrationForm, LoginForm, ZipCodeForm
import pymongo
from pymongo import MongoClient
from googlemapsdb import calculateDistance, mongoReadDb
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c61b50522f7fbc6186af128713d4516d'
client = pymongo.MongoClient("mongodb+srv://PelumiA:dbtest@cluster0.qqike.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test
collection = db["BlackListing"]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    id = 0
    result = collection.find({})
    for items in result:
        id += 1
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.business.data
        address = form.address.data
        state = form.state.data
        zipcode= form.zipcode.data
        city = form.city.data
        #generic insert
        id+=1
        collection.insert_one({"_id":id, "name": name, "address":address, "city": city, "zipcode":zipcode, "state":state})
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route('/businesses', methods=['GET','POST'])
def businesses():
    form = ZipCodeForm()
    finalQuery = mongoReadDb()
    distances = {}
    if form.zipcode.data is not None:
        distances = calculateDistance(finalQuery, form.zipcode.data)
    return render_template('businesses.html', distances = distances, form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data=='password':
            flash('Yoou have beem logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html',title='login',form=form)
