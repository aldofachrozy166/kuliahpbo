class Pegawai:
    def __init__(self,n,j,g):
        self.nama = n
        self.jabatan = j
        self.gaji = g

    def tampilkan(self):
        print(self.nama,",",self.jabatan,"dan",self.gaji*30)

p1 = Pegawai("adi","admin",5000)
p1.tampilkan()
