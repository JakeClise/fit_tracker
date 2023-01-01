from flask import Flask, render_template, redirect, request
from activity import Activity
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dash')
def dashboard():
    activities = Activity.get_all_activities()
    return render_template('home.html', user = "Jake", activities = activities)

@app.route('/new-activity')
def new_activity():
    return render_template('log_activity.html')

@app.route('/log-activity', methods = ["POST"])
def log_activity():
    data = {
        "name": request.form['name'],
        "description": request.form['description']
    }
    Activity.save_activity(data)
    return redirect('/dash')


if __name__ == "__main__":
    app.run(debug=True)