from flask import Flask,request,render_template
from afractalgenerator_v3_3 import *
app = Flask(__name__)

@app.route('/')
def hello_world():
	return("Hello world!")
	
@app.route('/heebgb/', methods=['GET','POST'])
def fractal_design_heebgb():
	error = None 
	try: 
		if request.method == 'POST':
			#process fractal data
			affinemaps = request.form['affinemaps']
			affinemaps = list(affinemaps.split(","))
			colormaps = request.form['colormaps']
			colormaps = list(colormaps.split(","))
			num_of_iterations = int(request.form['numiter'])
			folder = "static/images/user-generated/"
			filename = "heebgb"
			filenameEXT = "jpg"
			fileURI = folder+filename+"."+filenameEXT
			status = drawIFS(affinemaps,num_of_iterations,method="HeeBGBcolor",seed="Square",colormap=colormaps,filename=fileURI)
			if status==1:
				return(render_template("heebgbprint.html.jinja", name=None, value=fileURI, colormap=colormaps, affinemap=affinemaps, iterations=num_of_iterations))
			else:
				error = "Problem saving image, try again."
				return(render_template('heebgbform.html.jinja', name=None, error=error))
		
		else:
			#deliver initial page
			return(render_template('heebgbform.html.jinja', name=None))
	except Exception as e:
		return(render_template('heebgbform.html.jinja', error=e))
	'''
    error = ''
    try:
	
        if request.method == "POST":
		
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            #flash(attempted_username)
            #flash(attempted_password)

            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('dashboard'))
				
            else:
                error = "Invalid credentials. Try Again."

        return render_template("login.html", error = error)

    except Exception as e:
        #flash(e)
        return render_template("login.html", error = error)  
	'''	