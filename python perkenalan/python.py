# Definisi class Perkenalan
class Perkenalan:
    def __init__(self, nama, prodi, hobi, mimpi):
        self.nama = nama
        self.prodi = prodi
        self.hobi = hobi
        self.mimpi = mimpi

    def tampilkan_hobi(self):
        return ', '.join(self.hobi)
    
    def perkenalkan(self):
        return (
            f"Halo, nama saya {self.nama}.\n"
            f"Saya adalah mahasiswa program studi {self.prodi}.\n"
            f"Hobi saya adalah {self.tampilkan_hobi()}.\n"
            f"Saya bermimpi untuk menjadi {self.mimpi}."
        )

# Data perkenalan
nama = "Hafizh Nurfitrian Syah"
prodi = "Informatika"
hobi = ["membaca buku", "menggambar anime"]
mimpi = "Machine Learning Engineer"

# Membuat objek dari kelas Perkenalan
perkenalan_diri = Perkenalan(nama, prodi, hobi, mimpi)

# Menampilkan perkenalan diri
print(perkenalan_diri.perkenalkan())