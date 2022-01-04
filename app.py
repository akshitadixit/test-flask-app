from flask import Flask, jsonify, render_template, render_template_string, request
import pickle
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vulnerability1')
def login():
    return render_template('login.html')
    
@app.route("/vulnerability2", methods=["POST"]) 
def hackme():
    data = base64.urlsafe_b64decode(request.form['pickled'])
    deserialized = pickle.loads(data)
    # do something with deserialized or just
    # get pwned.

    return '', 204
    
@app.route('/vulnerability3/') 
def hello_ssti():
	person = {'name':"world", 'secret':"UGhldmJoZj8gYWl2ZnZoei5wYnovcG5lcnJlZg=="}
	if request.args.get('name'):
		person['name'] = request.args.get('name')
	template = '''<h2>Hello {{person}}!</h2>'''
	return render_template_string(template, person=person['name'])

####
# Private function if the user has local files.
###
def get_user_file(f_name):
	with open(f_name) as f:
		return f.readlines()

app.jinja_env.globals['get_user_file'] = get_user_file # Allows for use in Jinja2 templates

# runs on machine ip address to make it visible on netowrk
app.run(debug=True, host='0.0.0.0')
