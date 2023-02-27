class Control:
    def __init__(self):
        self.tv = None

    def enlazar(self, tv):
        tv.control = self
        self.tv = tv

    def turnOn(self):
       self.tv.turnOff()
    def turnOff(self):
        self.tv.turnOff()

    def canalUp(self):
        self.tv.canalUp()
    def canalDown(self):
        self.tv.canalDown()

    def volumenUp(self):
        self.tv.volumenUp()
    def volumenDown(self):
        self.tv.volumenDown()

    def setCanal(self, num):
        self.tv.setCanal(num)

    def getTv(self):
        return self.tv
    def setTv(self, tv):
        self.tv = tv