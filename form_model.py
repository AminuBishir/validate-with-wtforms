class LoginForm(Form):
	username = StringField('Username',[validators.required(), validators.Length(min=3)])
	password = PasswordField('Password',[validators.required,validators.Length(min=3)])
	remember_me = BooleanField('Remember Me')