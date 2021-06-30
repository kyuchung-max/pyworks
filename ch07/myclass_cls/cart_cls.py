class Cart:
    li=[]

    def __init__(self,goods):
        Cart.li.append(goods)

    def showinfo(self):
        print(self.li)

c1=Cart('a')
c1.showinfo()
c2=Cart('b')
c2.showinfo()
c3=Cart('c')
c3.showinfo()