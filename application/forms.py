# from flask.ext.wtf import Form
from flask_wtf import FlaskForm
from wtforms import TextField, validators


class EnterDBInfo(FlaskForm):
    dbNotes = TextField(label='Items to add to DB', description="db_enter", validators=[validators.required(), validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])


class RetrieveDBInfo(FlaskForm):
    numRetrieve = TextField(label='Number of DB Items to Get', description="db_get", validators=[validators.required(), validators.Regexp('^\d{1}$', message=u'Enter a number between 1 and 10')])
