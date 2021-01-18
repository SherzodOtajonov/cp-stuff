class BooleanArray:
    def __init__(self):
        self._d = {'defa':False, 'last':True}

    def setTrue(self, i):
        self._d[i] = True

    def setFalse(self, i):
        self._d[i] = False

    def setAllTrue(self):
        self._d = {'defa': True}

    def setAllFalse(self):
        self._d = {'defa': False}  

    def getValue(self, i):
        if i in self._d:
            return self._d[i]
        return self._d['defa']
