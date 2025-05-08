from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/aboutdili')
def about():
    return render_template('about.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/meettheteam')
def team():
    return render_template('team.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

if __name__ == '__main__':
    app.run(debug=True)