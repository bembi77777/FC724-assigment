from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/datacollection')
def data_collection():
    return render_template('datacollection.html')

if __name__ == '__main__':
    app.run(debug = True)
