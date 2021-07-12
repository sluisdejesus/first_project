class Session:
    def __init__(self, session_name,weekday, instructor, time, id=None):
        self.session_name = session_name
        self.weekday = weekday
        self. instructor = instructor
        self.time = time
        self.id = id