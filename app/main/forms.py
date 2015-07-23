from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    job_file = FileField( 'Job file')
    submit = SubmitField('Submit')
