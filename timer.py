import time


class Timer():
    def __init__(self):
        self.running = False
        self.start_time = None
        self.elapsed_time = 0

    def start_timer(self):
        if not self.running:
            self.running = True
            if self.start_time is None:
                self.start_time = time.time()
            else:
                self.start_time = time.time() - self.elapsed_time

    def stop_timer(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time

    def get_time(self):
        if self.running:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            return self.format_time(elapsed_time)

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{int(minutes):02}:{seconds:05.2f}"
