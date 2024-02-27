class TV():
    numTV=0
    _volumen=1
    _canal=1
    _precio=500  
    _control=None  
    def __init__(self,marca,estado):
        self._marca=marca
        self._estado=estado
    def getMarca(self):
        return self._marca
    def setMarca(self,str):
        self._marca=str
    def getCanal(self):
        return self._canal
    def setCanal(self,num):
        if num>0 and num<121 and self._estado==True:
            self._canal=num
    def getVolumen(self):
        return self.volumen
    def setVolumen(self,num):
        if num<8 and num>-1 and self._estado==True: 
            self._volumen=num
    def getPrecio(self):
        return self._precio
    def setPrecio(self,num):
        self._precio=num
    def getControl(self):
        return self._control
    def setControl(self,str):
        self._control=str
    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False
    def getEstado(self):
        return self._estado
    def canalUp(self):
        if self._canal<120 and self._estado==True:
            self._canal+=1
    def canalDown(self):
        if self._canal>1 and self._estado==True:
            self._canal-=1
    def volumenUp(self):
        if self._volumen<7 and self._estado==True:
            self._volumen+=1
    def volumenDown(self):
        if self._volumen>0 and self._estado==True:
            self._volumen-=1
        
