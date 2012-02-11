from bottle import run, template, route, request
from bottle import static_file

@route('/')
def hello():
    return template('index.tpl')

@route('/team')
def team():
    return template('team.tpl')

@route('/help')
def info():
    return template('info.tpl')


@route('/submit', method="POST")
def todo():
    #datafile = request.POST.get('cal_file')
    events = {}
    for data in request.forms:
        if data !=  "cal_file":
            if "event" + data[-1:] in events.keys():
                events["event" + data[-1]][data[:-1]] = request.forms.get(data)
            else:
                events["event" + data[-1]] = { data[:-1] : request.forms.get(data) }

    output = ""
    for a in events:
        output += a + '\n'
        for c in events[a]:
            output += '\t' + c + ":\t" + events[a][c] + '\n'
    return output



@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/')


run(host='localhost', port=8080)
