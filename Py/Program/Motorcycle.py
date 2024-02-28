from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, tipemotor="", kapasitastangki="", tahunproduksi=0, merk="", plat="", warna=""):
        super().__init__(tahunproduksi, merk, plat, warna)
        self.tipemotor= tipemotor
        self.kapasitastangki = kapasitastangki

    def get_tipemotor(self):
        return self.tipemotor

    def set_tipemotor(self, tipemotor):
        self.tipemotor= tipemotor

    def get_kapasitastangki(self):
        return self.kapasitastangki

    def set_kapasitastangki(self, kapasitastangki):
        self.kapasitastangki = kapasitastangki