from datetime import datetime


class Timer:
    def __enter__(self):
        self.start = datetime.now()
        self.duration = None
    
    def __exit__(self, *args):
        self.duration = (datetime.now() - self.start).total_seconds()