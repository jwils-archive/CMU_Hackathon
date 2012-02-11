class Event(object):
    """Used to store both set events and events we 
       plan on scheduling"""
    def __init__(self):
        self.constraints = []

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

    def set_start(self, start):
        self.start = start

    def get_start(self):
        return self.start