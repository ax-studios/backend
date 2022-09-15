

class Hi:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self.name

    @property.setter
    def name(self,name):
        self.name = name

