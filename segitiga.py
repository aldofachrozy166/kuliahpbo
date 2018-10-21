class Segitiga:
    def __init__(self, jumlah sisi='3',bentuk_segitiga='sembarang')
        self.jumlah_sisi = jumlah_sisi
        self.bentuk_segitiga = bentuk_segitiga
    def Pn (self):
        print("jumlah sisi", self.jumlah_sisi)
        print("bentuk_segitiga", self.bentuk_segitiga)

class SegitigaSamaSisi(Segitiga):
    def __init__(self, jumlah_sisi, bentuk_segitiga="samasisi"):
        self.jumlah_sisi = jumlah_sisi
        self.bentuk_segitiga = bentuk_segitiga

a = Segitiga()
a.Pn
b = SegitigaSamaSisi()
b.Pn()
