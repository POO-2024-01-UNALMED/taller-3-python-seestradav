
class Control():
    _tv=None
    def enlazar(self,tv)-> None:
        self._tv=tv
        self._tv.setControl(self)
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()
    def setCanal(self):
        self._tv.setCanal(self)
    
