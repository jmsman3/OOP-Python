class Engine:
    def __init__(self) -> None:
        pass

    def Start(self):
        pass
class Driver:
    def __init__(self) -> None:
        pass 

class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()
    def start(self):
        self.engine.Start()