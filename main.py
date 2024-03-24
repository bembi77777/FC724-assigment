from flask import Flask, render_template, redirect, url_for
from flask import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField
from wtforms.validators import InputRequired
app = Flask(__name__)
app.config['SECRET_KEY'] = 'blank'

class Survey(FlaskFrom):
    name = StringField('Name', validators=[InputRequired()])
    student_number = StringField('Student number', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    grades = StringField('Grades', validators=[InputRequired()])
    satisfaction = SelectField('Overall Satisfaction', choices=[
        ('', 'Select Satisfaction Level'),
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('average', 'Average'),
        ('poor', 'Poor')
    ])
    suggestions = TextAreaField('Suggestions For Improvement', validators=[InputRequired()])

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
