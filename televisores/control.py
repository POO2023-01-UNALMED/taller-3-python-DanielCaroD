class Control:
    def __init__(self):
        self.tv = None

    def enlazar(self, tv):
        self.tv = tv
        tv.control = self

    def turnOn(self):
       if self.tv is not None:
           self.tv.turnOn()
    def turnOff(self):
        if self.tv is not None:
            self.tv.turnOff()

    def canalUp(self):
        if self.tv is not None:
            self.tv.canalUp()
    def canalDown(self):
        self.tv.canalDown()

    def volumenUp(self):
        if self.tv is not None:
            self.tv.volumenUp()
    def volumenDown(self):
        if self.tv is not None:
            self.tv.volumenDown()

    def setCanal(self, num):
        if self.tv is not None:
            self.tv.setCanal(num)

    def getTv(self):
        return self.tv
    def setTv(self, tv):
        self.tv = tv