# Car Powered by Engine

class Engine:
    def start(self):
        print("Engine starts!")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def run(self):
        self.engine.start()

e = Engine()
c = Car(e)
c.run()
