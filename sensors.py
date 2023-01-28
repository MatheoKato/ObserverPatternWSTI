from observable import Observable
class Sensors(Observable):
    def __init__(self):
        super().__init__()

    def read_data(self, temp, humidity):
        self.temp = temp
        self.humidity = humidity
        self.notify(self.temp, self.humidity)
