from televisores import tv

class Control:
    def __init__(self):
        self.tv = tv

    def enlazar(self, tv):
        tv.control = Control

    def turnOn(self):
        self.tv.estado = True
    def turnOff(self):
        self.tv.estado = False

    def canalUp(self):
        if (self.tv.estado == True and self.tv.canal < 120):
            self.tv.canal += 1
    def canalDown(self):
        if (self.tv.estado == True and self.tv.canal > 1):
            self.tv.canal -= 1

    def volumenUp(self):
        if (self.tv.estado == True and self.tv.volumen < 7):
            self.tv.volumen += 1
    def volumenDown(self):
        if (self.tv.estado == True and self.tv.volumen > 0):
            self.tv.volumen -= 1

    def setCanal(self, num):
        if ((self.tv.estado == True) and (num >= 1) and (num <=120)):
            self.tv.canal = num