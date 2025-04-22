#  Lifecycle Notifier

class Logger:
    def __init__(self):
        print("Logger initialized.")

    def __del__(self):
        print("Logger destroyed.")

log = Logger()
del log
