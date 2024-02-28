from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, jumlahkursi="", jumlahpintu="", tahunproduksi=0, merk="", plat="", warna=""):
        super().__init__(tahunproduksi, merk, plat, warna)
        self.jumlahkursi= jumlahkursi
        self.jumlahpintu = jumlahpintu

    def get_jumlahkursi(self):
        return self.jumlahkursi

    def set_jumlahkursi(self, jumlahkursi):
        self.jumlahkursi= jumlahkursi

    def get_jumlahpintu(self):
        return self.jumlahpintu

    def set_jumlahpintu(self, jumlahpintu):
        self.jumlahpintu = jumlahpintu
