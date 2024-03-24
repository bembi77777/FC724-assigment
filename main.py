from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField
from wtforms.validators import InputRequired
app = Flask(__name__)
app.config['SECRET_KEY'] = 'blank'

class Survey(FlaskForm):
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

@app.route('/Home')
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
            file.write(f"Name: {form.Name.data}\n")
            file.write(f"Student number: {form.Student_number.data}\n")
            file.write(f"Email: {form.Email.data}\n")
            file.write(f"Grades: {form.Grades.data}\n")
            file.write(f"Satisfaction: {form.Satisfaction.data}\n")
            file.write(f"Suggestions for improvement: {form.Suggestions_for_improvement.data}\n")

        return redirect(url_for('thank_you'))

    return render_template('datacollection.html', form=form)
@app.route('/thank-you')
def thank_you():
    return 'Thank you'
if __name__ == '__main__':
    app.run(debug = True)
