class Vehicle:
    def __init__(self, tahunproduksi=0, merk="", plat="", warna=""):
        self.tahunproduksi = tahunproduksi
        self.merk = merk
        self.plat = plat
        self.warna = warna

    def get_tahunproduksi(self):
        return self.tahunproduksi

    def set_tahunproduksi(self, tahunproduksi):
        self.tahunproduksi = tahunproduksi

    def get_merk(self):
        return self.merk

    def set_merk(self, merk):
        self.merk = merk

    def get_plat(self):
        return self.plat

    def set_plat(self, plat):
        self.plat = plat

    def get_warna(self):
        return self.warna

    def set_warna(self, warna):
        self.warna = warna