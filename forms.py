from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, FileField, IntegerField, SubmitField, EmailField, SelectField
from wtforms.validators import Email, EqualTo, DataRequired, ValidationError
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, punctuation
from table import Users


class AddForm(FlaskForm):
    type = SelectField(u'Type: ', choices=[('cpu', 'CPUs'), ('ram', 'RAM modules'), ('mobo', 'Motherboards')])
    name = StringField("Product name")
    description = TextAreaField("Description")
    brand = StringField("Brand/vendor")
    price = IntegerField("Price")
    photo = FileField("Image")
    submit = SubmitField("Add this")


class LoginForm(FlaskForm):
    login = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    login = StringField('Username', validators=[DataRequired()])
    email = EmailField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


    def validate_password(self, password):
        isFine = True
        if not any(i in ascii_lowercase for i in password.data): isFine = False
        if not any(i in ascii_uppercase for i in password.data): isFine = False
        if not any(i in digits for i in password.data): isFine = False
        if not any(i in punctuation for i in password.data): isFine = False
        if not isFine:
            raise ValidationError('''Your password must contain at least one digit, lowercase letter,
                                     uppercase letter, a symbol from the set of .,;:!?%$#@&*^|\~[]{/}''')

    def validate_username(self, login):
        if self.login.data[0] not in ascii_letters:
            raise ValidationError('the first letter in login must be Latin')
        user = Users.query.filter_by(login=login.data).first()
        if user is not None:
            raise ValidationError('there already is an user with such username')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('there already is an user with this e-mail address')


class CommentForm(FlaskForm):
    like = SelectField(u'Rating ', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    comment = TextAreaField("Comment")
    submit = SubmitField("Comment")