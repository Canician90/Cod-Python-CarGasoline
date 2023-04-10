class Car:
    def __init__(self):
        self.gas = 50.0
        self.is_running = False

    def start(self):
        if self.gas > 0:
            self.is_running = True
            print("Engine started.")
        else:
            print("Out of gas.")

    def stop(self):
        self.is_running = False
        print("Engine stopped.")

    def run(self):
        if self.is_running:
            self.gas -= 0.5
            if self.gas <= 0:
                self.stop()
                print("Out of gas.")
            elif self.gas <= 1:
                self.stop()
                print("Red light! Motor stopped.")
            elif self.gas <= 5:
                print("Red light! Low fuel.")
            else:
                print("Driving with {0:.1f} liters of gas left.".format(self.gas))

# Create a new car and start the engine
car = Car()
car.start()

# Simulate driving until the motor stops
while car.is_running:
    car.run()
