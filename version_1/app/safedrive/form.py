from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError, TextAreaField
from wtforms.validators import Required,Length,Email,EqualTo,Regexp,Optional
from ..model import User


class ProfileForm(Form):
    name = StringField('Name', validators=[Optional(), Length(1, 64)])
    device = StringField('Device Id', validators=[Required(), Length(1, 16)])
    phone=StringField('Phone Number',validators=[Required(),Length(1,10)])
    address=TextAreaField('Address',validators=[Optional()])
    emergency=StringField('Emergency Number',validators=[Required(),Length(1,10)])
    submit = SubmitField('Submit')

    def from_model(self, User):
        self.name.data=User.name
        self.device.data = User.device_id
        self.phone.data = User.phone_no
        self.address.data = User.address
        self.emergency.data= User.emergency_no
        

    def to_model(self, User):
        User.name = self.name.data
        User.device_id = self.device.data
        User.phone_no = self.phone.data
        User.address = self.address.data
        User.emergency_no = self.emergency.data

    