# Robot Class


class Brain():
    def __init__(self, imu, range_find, computer, controller,camera):
        self.imu = imu
        self.range_find = range_find
        self.computer = computer
        self.controller = controller
        self.camera = camera

    def locate(self):
        print(f'Locating axis... with {self.imu}')

    def measure(self):
        print(f'Measuring... with {self.range_find}')
    
    def calculate(self):
        print(f'Calculating Trajectory...with {self.computer}')
        print(f'Predicting best movement...with {self.computer}')

    def execute(self):
        print(f'Executing Movement Order...with {self.computer}')
        print(f'Executing Movement...with {self.controller}')

if __name__ == '__main__':

    hardware = Brain('interial','range finder','pi','ad')
    print(hardware.imu,'and', hardware.range_find)
    hardware.calculate()


    