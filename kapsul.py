class Makanan:
#atribut
    def __init__(self):
        self.__hargajual = 1000

#private Method
    def __dijual(self):
        print("harga makanan: ", self.__hargajual)

    def setHargaJual(self, harga):
        self.__hargajual = harga

m = Makanan()
m._Makanan__dijual()
m.setHargaJual(2000)

m.__hargajual = 2000
m._Makanan__dijual()

