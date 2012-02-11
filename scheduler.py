from icalendar import Calendar, Event
from datetime import datetime

class ConstrainedEvent():
    def __init__(self, summary, details, duration, start=0, end=0):
        self.summary = summary
	self.details = details
	self.start = start
	self.end = end
	self.duration = duration
	self.constraints = []
	
    def getID(self):
        return id(self)

    def addConstraint(self, constraint):
    	self.constraints.append(constraint)

class Constraint():
    def __init__(self, eventid):
        self.eventid = eventid

    def isValid(self, ical):
        return True

class ConstrainedCal():
    def __init__(self, ical):
        self.ical = ical
	self.events = []
	self.generate_cal()

    def generate_cal(self):
        for component in self.ical.walk():
	    dc = component.decoded
	    e = ConstrainedEvent(dc['summary'], dc['details'], 0, dc['dtstart'], dc['dtend'])
	   self.events += e

class Scheduler():
    def __init__(self, fname):
        self.ical = Calendar.from_string(open(fname, 'rb').read())
	self.tree = ConstrainedCal(self.ical)

    def findSchedule(self):
        pass

    def test_add(self):
        event = Event()
	event['summary'] = 'test event'
	event['dtstart'] = datetime(2012, 2, 4, 8, 0, 0).strftime('%Y%m%dT%H%M%S')
	event['dtend'] = datetime(2012, 2, 4, 10, 0, 0).strftime('%Y%m%dT%H%M%S')
	self.ical.add_component(event)

    def test_save(self):
        f = open('test_save.ics', 'wb')
        f.write(self.ical.as_string())
        f.close()

def main():
    s = Scheduler('test.ics')
    s.test_add()
    s.test_save()

if __name__ == '__main__':
    main()

