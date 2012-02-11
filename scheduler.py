from icalendar import Calendar, Event
from datetime import datetime
import time
import os

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
    def __init__(self):
        pass

    def isValid(self, event, ical):
        return True

class Scheduler():
    def __init__(self, ical_string, start_date, end_date, new_events):
        self.ical = Calendar.from_string(ical_string)
        self.simpl_ical = Calendar()
        self.new_events = new_events
        self.new_events.sort(key=lambda x: x.duration, reverse=True)
        self.start_date = start_date - start_date%30 + 30
        self.end_date = end_date - end_date%30 + 30

    def findSchedule(self):
        for event in self.new_events:
           is_scheduled = False
           curr_time = self.end_date - event.duration
           while not is_scheduled and not curr_time < self.start_date:
               event.start = curr_time
               event.end = curr_time + event.duration
               is_valid = True
               # check conflicts with current schedule
               for component in self.ical.walk():
                   if component.name == 'VEVENT':
                       #try:
                       dc = component.decoded
                       dtstart = time.mktime(time.strptime(str(dc('dtstart')), '%Y-%m-%d %H:%M:%S+00:00'))/60
                       dtend = time.mktime(time.strptime(str(dc('dtend')), '%Y-%m-%d %H:%M:%S+00:00'))/60
                       if curr_time > dtstart and curr_time < dtend or curr_time + event.duration > dtstart and curr_time + event.duration < dtend or curr_time < dtstart and curr_time + event.duration > dtend or curr_time > dtstart and curr_time + event.duration < dtend or curr_time == dtstart or curr_time + event.duration == dtend:
                           is_valid = False
                           break
               if is_valid:
                   for constraint in event.constraints:
                       if not constraint.isValid(event, self.ical):
                           is_valid = False
                           break
               if is_valid:
                   self.addToCalendar(event)
                   is_scheduled = True
               else:
                   curr_time -= 30

    def addToCalendar(self, event):
        e = Event()
        e['summary'] = event.summary
        e['dtstart'] = datetime.fromtimestamp(event.start*60).strftime('%Y%m%dT%H%M%SZ')
        e['dtend'] = datetime.fromtimestamp(event.end*60).strftime('%Y%m%dT%H%M%SZ')
        e['details'] = event.details
        self.ical.add_component(e)
        self.simpl_ical.add_component(e)

    def writeFile(self):
    	#return self.ical.as_string()
	return self.simpl_ical.as_string()
   
def main():
    events = []
    e = ConstrainedEvent('1This is a test event', 'Not much more to say about it. . .', 10)
    events.append(e)
    e = ConstrainedEvent('2This is a test event', 'Not much more to say about it. . .', 30)
    events.append(e)
    e = ConstrainedEvent('3This is a test event', 'Not much more to say about it. . .', 120)
    events.append(e)
    e = ConstrainedEvent('4This is a test event', 'Not much more to say about it. . .', 60)
    events.append(e)
    e = ConstrainedEvent('5This is a test event', 'Not much more to say about it. . .', 600)
    events.append(e)
    e = ConstrainedEvent('6This is a test event', 'Not much more to say about it. . .', 400)
    events.append(e)
    e = ConstrainedEvent('7This is a test event', 'Not much more to say about it. . .', 25)
    events.append(e)
    e = ConstrainedEvent('8This is a test event', 'Not much more to say about it. . .', 19)
    events.append(e)
    f = open('cmu_demo.ics')
    ical_string = ''
    for line in f:
        ical_string += line
    s = Scheduler(ical_string, time.time()/60, time.time()/60 + 2880, events)
    s.findSchedule()
    f = open('output.ics', 'wb')
    f.write(s.writeFile())

if __name__ == '__main__':
    main()

