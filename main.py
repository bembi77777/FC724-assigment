from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blank'

class Survey(FlaskForm):
    name = StringField('Name:', validators=[InputRequired()])
    student_number = StringField('Student number:', validators=[InputRequired()])
    email = StringField('Email:', validators=[InputRequired()])
    grades = StringField('Grades:', validators=[InputRequired()])
    satisfaction = SelectField('Overall Satisfaction:', choices=[
        ('', 'Select Satisfaction Level'),
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('average', 'Average'),
        ('poor', 'Poor')
    ])
    suggestions = TextAreaField('Suggestions For Improvement:', validators=[InputRequired()])

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/Information')
def information():
    return render_template('information.html')

@app.route('/Datacollection', methods=['GET', 'POST'])
def data_collection():
    form = Survey()
    if form.validate_on_submit():
        print("Form validation successful")
        with open('feedback.txt', 'a') as file:
            file.write(f"Name: {form.name.data}\n")
            file.write(f"Student number: {form.student_number.data}\n")
            file.write(f"Email: {form.email.data}\n")
            file.write(f"Grades: {form.grades.data}\n")
            file.write(f"Satisfaction: {form.satisfaction.data}\n")
            file.write(f"Suggestions for improvement: {form.suggestions.data}\n")

        return redirect(url_for('thank_you'))

    return render_template('datacollection.html', form=form)
@app.route('/thank-you')
def thank_you():
    return 'Thank you'
if __name__ == '__main__':
    app.run(debug = True)