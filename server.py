from bottle import run, template, route, request
from bottle import static_file
import time 
import scheduler

@route('/')
def hello():
    return template('index.tpl')

@route('/team')
def team():
    return template('team.tpl')

@route('/help')
def info():
    return template('info.tpl')

class DueDateCon(scheduler.Constraint):
    def __init__(self,duedt):
        self.duedt = time.mktime(time.strptime(duedt, "%m/%d/%Y"))/60

    def isValid(self, event, ical):
        return event.end < self.duedt

@route('/submit', method="POST")
def todo():
    datafile = request.POST.get('cal_file')

# Note: for now we assume that file is PerCal01.ics or whatever, but not valid for the future!  get that info from data

    events = {}
    for data in request.forms:
        if data !=  "cal_file":
            if "event" + data[-1:] in events.keys():
                events["event" + data[-1]][data[:-1]] = request.forms.get(data)
            else:
                events["event" + data[-1]] = { data[:-1] : request.forms.get(data) }

#    output = ""
    sEvent = []
    for a in events:
        eventdata = []
#       output += a + '\n'
#       for c in events[a]:
#           output += '\t' + c + ":\t" + events[a][c] + '\n'
        #eventdata = [events[a]["description"],''
        ce = scheduler.ConstrainedEvent(events[a]["description"],'',int(events[a]["time"]))
        # create the due date constraint
        condt = DueDateCon(events[a]["duedate"])
        ce.addConstraint(condt)
        sEvent.append(ce)

    s = scheduler.Scheduler(datafile.file.read(), time.time()/60, time.time()/60 + 2880, sEvent)
    s.findSchedule()
    newname = s.writeFile()

    return newname



@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/')


run(host='localhost', port=8080)
