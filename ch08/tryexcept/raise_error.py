class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    #pass
    def fly(self):
        print('eagle fly')

eagle= Eagle()
eagle.fly()