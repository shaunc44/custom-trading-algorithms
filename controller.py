from flask import (
	Flask, render_template, redirect, 
	url_for, request, session, json
)
from forms import FilterForm
import datetime as dt
from models import run_model


app = Flask(__name__)

app.config['SECRET_KEY'] = open('secret_key', 'rb').read() 


@app.route("/", methods = ["GET"])
def main():
	return render_template("login.html")


@app.route("/about")
def about():
	return render_template("about.html")


@app.route("/create-algo")
def create_algo():
	return render_template("create_algo.html")


@app.route("/logout")
def logout():
	return render_template("login.html")
#add code here to enable secure logout


@app.route("/dashboard")
def dashboard():
	username = session['username']
	user_id = models.User.get_id(username)
	# events = models.Events.get_user_events(user_id)
	return render_template("dashboard.html", user=username, event=events)


@app.route("/filter", methods=["POST"]) #this route should go to graph part of page??
def filter():
	my_form = FilterForm(request.form)

	# Start & End Dates
	startdate_input = request.form['startdate'] #increment dates here????????
	rundate = dt.datetime.strptime(startdate_input, '%m/%d/%Y').strftime('%Y-%m-%d')
	enddate_input = request.form['enddate']
	enddate = dt.datetime.strptime(enddate_input, '%m/%d/%Y').strftime('%Y-%m-%d')

	# Last Price
	lp_low = request.form['inputLastPriceLow']
	lp_high = request.form['inputLastPriceHigh']

	# Price to Earnings
	pe_low = request.form['inputPeLow']
	pe_high = request.form['inputPeHigh']

	# Dividend Yield
	dy_low = request.form['inputDivYieldLow']
	dy_high = request.form['inputDivYieldHigh']

	# RSI buy & sell signals
	rsi_buy = request.form['inputRsiBuy']
	rsi_sell = request.form['inputRsiSell']

	run = run_model.RunLoop(rundate, enddate, lp_low, lp_high, pe_low, pe_high, dy_low, dy_high, rsi_buy, rsi_sell)
	run.run_loop()

	print("\nRequest Form = ", request.form)
	print("\nValidate Form = ", my_form.validate())

	return json.jsonify(my_form.errors)





if __name__ == "__main__":
	app.run(host="127.0.0.1", port=5000, debug=True)


# @app.route("/")
# def home():
# 	events = models.Events.all_events()
# 	return render_template("index.html", event=events)


# @app.route("/check-login", methods=["POST"])
# def check_login():
# 	username = request.form['username']
# 	password = request.form['password']

# 	success = model.User.check_login(username, password)
# 	if success:
# 		session['username'] = username
# 		return dashboard()
# 	else:
# 		return render_template("login.html")


# @app.route("/logged-in-home")
# def logged_in_home():
# 	username = session['username']
# 	events = models.Events.all_events()
# 	return render_template("logged-in-home.html", event=events)


# @app.route("/register")
# def register():
# 	return render_template("register.html")


# @app.route("/check-register", methods=["POST"])
# def check_register():
# 	username = request.form['username']
# 	password = request.form['password']
# 	success = models.User.check_register(username)
# 	if success:
# 		session['username'] = username
# 		models.User.add_new_user(username, password)
# 		return dashboard()
# 	else:
# 		return render_template("register.html")


# @app.route("/create-event")
# def create_event():
# 	username = session['username']
# 	return render_template("create-event.html")

# @app.route("/add-event", methods=["POST"])
# def add_event():
# 	username = session['username']
# 	title = request.form['title']
# 	description = request.form['description']
# 	location = request.form['location']
# 	user_id = models.User.get_id(username)
# 	models.Events.add_event(title, description, location, user_id)
# 	return dashboard()

# @app.route("/update-event")
# def update_event():
# 	username = session["username"]
# 	return render_template("update-event.html")

# @app.route("/update", methods=["POST"])
# def update():
# 	username = session['username']
# 	title = request.form['title']
# 	user_id = models.User.get_id(username)
# 	result = models.Events.get_event_to_update(title, user_id)
# 	if result:
# 		return input_update_info(title)
# 	else:
# 		return render_template("update-event.html")

# @app.route("/input-update-info")
# def input_update_info(title):
# 	username = session['username']
# 	session['title'] = title
# 	return render_template("input-update-info.html", name=title)

# @app.route("/add-update", methods=["POST"])
# def add_update():
# 	old_title = session['title']
# 	username = session['username']
# 	title = request.form['title']
# 	description = request.form['description']
# 	location = request.form['title']
# 	result = models.Events.add_update(old_title, title, description, location)
# 	return dashboard()

# @app.route("/delete-event")
# def delete_event():
# 	username = session['username']
# 	return render_template("delete-event.html")

# @app.route("/delete", methods=["POST"])
# def delete():
# 	username = session['username']
# 	title = request.form['title']
# 	user_id = models.User.get_id(username)
# 	result = models.Events.delete(title, user_id)
# 	if result:
# 		return dashboard()
# 	else:
# 		return delete_event()

# @app.route("/attend")
# def attend():
# 	username = session['username']
# 	return render_template("attend.html")

# @app.route("/attend-event")
# def attend_event():
# 	username = session['username']
# 	title = request.form['title']
# 	user_id = models.User.get_id(username)
# 	result = models.Events.attend(title, user_id)
# 	if result: