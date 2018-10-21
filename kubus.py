class kubus:
    def __init__(self,s):
        self.sisi = s

    def tampilkansisi(self):
        print(self.sisi)

    def luas (self):
        print("luas= " ,self.sisi ** 2)

kubus1 = kubus(4)
kubus1.tampilkansisi()
kubus1.luas()
