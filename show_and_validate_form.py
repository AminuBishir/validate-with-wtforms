#the '/' below indicates that this is default/index page
@app.route('/',methods=['GET','POST'])
def home_page():
	#create object of our LoginForm
	login_form = LoginForm()
	
	#check if our request is of GET type, then display form
	if request.method == 'GET':
		return render_template('home.html',login_form=login_form)
		
	else:
	#our request is of POST type which mean data is being submitted via the form
	
	#validate the login grab our data here and do something with it
	if login_form.validate() #check if the data conform to the rules
		username = login_form.username.data
		userpass = login_form.password.data
		stay_logged = login_form.remember_me.data #boolean yes or no
		
		#now that we have the data we can do what we like with it
	else:
	# some form's rules are violated, you can acess the errors in the template through login_form.errors