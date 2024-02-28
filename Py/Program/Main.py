from Car import Car
from Motorcycle import Motorcycle
from Parkinglot import Parkinglot
from tabulate import tabulate  # Library untuk membuat tabel

# Membuat objek-objek untuk data kendaraan (hardcoded)
cars = [
    Car(jumlahkursi=4, jumlahpintu=4, tahunproduksi=2020, merk="Toyota", plat="B 1234 CD", warna="Black"),
    Car(jumlahkursi=2, jumlahpintu=2, tahunproduksi=2018, merk="Honda", plat="B 5678 EF", warna="Red"),
    Car(jumlahkursi=5, jumlahpintu=4, tahunproduksi=2022, merk="Ford", plat="B 9012 GH", warna="Blue")
]

motorcycles = [
    Motorcycle(tipemotor="Sport", kapasitastangki="10L", tahunproduksi=2019, merk="Yamaha", plat="B 9876 FG", warna="Blue"),
    Motorcycle(tipemotor="Matic", kapasitastangki="5L", tahunproduksi=2021, merk="Suzuki", plat="B 5432 HI", warna="White"),
    Motorcycle(tipemotor="Cub", kapasitastangki="3L", tahunproduksi=2020, merk="Honda", plat="B 2468 IJ", warna="Red")
]

# Membuat objek Garage dan Parkinglot
parkinglot1 = Parkinglot(kapasitas="100", jumlahkendaraan="0", daftarkendaraan="", namagarasi="Pakiran gg", luas="200 m2")

# Menambahkan kendaraan ke daftar kendaraan di parking lot
all_vehicles = cars + motorcycles
parkinglot1.set_daftarkendaraan(all_vehicles)
parkinglot1.set_jumlahkendaraan(len(all_vehicles))


print("Informasi Parkiran:")
print("Nama Parkiran:", parkinglot1.get_namagarasi())
print("Luas Parkiran:", parkinglot1.get_luas())
print("Kapasitas Parkiran:", parkinglot1.get_kapasitas())
print("Jumlah Kendaraan di Parkiran:", parkinglot1.get_jumlahkendaraan())

print("\nDaftar Kendaraan di Parkiran:")
for kendaraan in parkinglot1.get_daftarkendaraan():
    if isinstance(kendaraan, Car):
        print("-", kendaraan.get_merk(), "dengan plat", kendaraan.get_plat())
    elif isinstance(kendaraan, Motorcycle):
        print("-", kendaraan.get_merk(), "dengan plat", kendaraan.get_plat())
# Menampilkan daftar kendaraan dalam bentuk tabel

print("\nInformasi Detail Kendaraan:")
table_data = []
for vehicle in all_vehicles:
    if isinstance(vehicle, Car):
        vehicle_type = "Car"
        jumlah_kursi = vehicle.get_jumlahkursi()
        jumlah_pintu = vehicle.get_jumlahpintu()
        atribut_khusus = f"Jumlah Kursi: {jumlah_kursi}, Jumlah Pintu: {jumlah_pintu}"
    elif isinstance(vehicle, Motorcycle):
        vehicle_type = "Motorcycle"
        tipe_motor = vehicle.get_tipemotor()
        kapasitas_tangki = vehicle.get_kapasitastangki()
        atribut_khusus = f"Tipe Motor: {tipe_motor}, Kapasitas Tangki: {kapasitas_tangki}"
    table_data.append([vehicle_type, vehicle.get_merk(), vehicle.get_plat(), vehicle.get_warna(), atribut_khusus])

# Menampilkan tabel
headers = ["Type", "Merk", "Plat", "Warna", "Attribut Khusus"]
print(tabulate(table_data, headers=headers, tablefmt="grid"))