class Cart:

    def __init__(self,goods):
        self.li=[]
        self.li.append(goods)

    def showinfo(self):
        print(self.li)

c1=Cart('a')
c1.showinfo()
c2=Cart('b')
c2.showinfo()