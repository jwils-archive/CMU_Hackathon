from bottle import run, template, route, request
from bottle import static_file

@route('/')
def hello():
    return template('index.tpl')


@route('/submit', method="POST")
def todo():
	#datafile = request.POST.get('cal_file')
	output = ""
	for constraint in request.POST:
		if constraint == 'cal_file':
			continue
		else:
			output += request.POST.get(constraint)
	return output


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/')


run(host='localhost', port=8080)