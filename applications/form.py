from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField,IntegerField
from wtforms.validators import DataRequired

class UserDataForm(FlaskForm):
    name = StringField('Tv Show', validators=[DataRequired()])
    #Movie_Description = StringField(validators=[DataRequired()])
    rating = SelectField ('Rating',validators=[DataRequired()],
                          choices= [('1', '1'), ('2', '2'),('3', '3'),('4', '4'),('5', '5')])           
    submit = SubmitField('Add Movie')