class Murid:

    def __init__(self):
        self.nama = input("Nama :")

    def display(self):
        print("Nama:",self.nama)

class NilaiPelajaran:

    def __init__(self):
        print("Nilai Pelajaran")
        self.math = int(input("Math:"))
        self.biology = int(input("Biology:"))

    def display(self):
        print ("Rata2 Nilai:", (self.math + self.biology)/2)

class Student (Murid, Nilai Pelajaran):
    def __init__(self):
        Murid.__init__(self)
        NilaiPelajaran.__init__(self)

    def result(self):
        Murid.display(self)
        NilaiPelajaran.display(self)

stu1 = student()
stu2 = student()

stu1.result()
stu2.result()
