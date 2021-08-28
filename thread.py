from threading import Thread, Event
import signal

exit_event = Event()

def signal_handler(signal, frame):
    exit_event.set()

signal.signal(signal.SIGINT, signal_handler)

class KillableThread(Thread):
    def __init__(self, sleep_interval=1, target=None, name=None, args=(), kwargs={}):
        super().__init__(None, target, name, args, kwargs)
        self._kill = Event()
        self._interval = sleep_interval
        print(self._target)

    @property
    def is_kill(self):
        return self._kill.is_set()

    def run(self):
        while True:
            # Call custom function with arguments
            self._target(*self._args)

            # If no kill signal is set, sleep for the interval,
            # If kill signal comes in while sleeping, immediately
            #  wake up and handle
            is_killed = self._kill.wait(self._interval)
            if is_killed:
                break

        print("Killing Thread")


    def kill(self):
        self._kill.set()


