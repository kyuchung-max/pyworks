class ScaleC:
    def __init__(self,unit_from, unit_to, factor):
        self.unit_from=unit_from
        self.unit_to=unit_to
        self.factor=factor

    def convert(self,val):
        return self.factor*val

if __name__=='__main__':
    c1= ScaleC('inches','mm',25)
    print(str(c1.convert(2)) + c1.unit_to)