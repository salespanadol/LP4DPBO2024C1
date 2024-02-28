from Garage import Garage

class Parkinglot(Garage):
    def __init__(self, kapasitas="", jumlahkendaraan="", daftarkendaraan="", namagarasi="", luas=""):
        super().__init__(namagarasi, luas)
        self.kapasitas = kapasitas
        self.jumlahkendaraan = jumlahkendaraan
        self.daftarkendaraan = daftarkendaraan

    def get_kapasitas(self):
        return self.kapasitas

    def set_kapasitas(self, kapasitas):
        self.kapasitas = kapasitas

    def get_jumlahkendaraan(self):
        return self.jumlahkendaraan

    def set_jumlahkendaraan(self, jumlahkendaraan):
        self.jumlahkendaraan = jumlahkendaraan

    def get_daftarkendaraan(self):
        return self.daftarkendaraan

    def set_daftarkendaraan(self, daftarkendaraan):
        self.daftarkendaraan = daftarkendaraan
