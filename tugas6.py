from abc import ABC, abstractmethod
class Manusia(ABC):
    def __init__(self, nama=None, nim=None, umur=None, prodi=None):
        self.nama = nama
        self.nim = nim
        self.umur = umur
        self.prodi = prodi

    @abstractmethod
    def input_data(self, nama, nim, umur, prodi):
        pass

    @abstractmethod
    def tampilkan_detail(self):
        pass

class Mahasiswa(Manusia):
    def input_data(self, nama, nim, umur, prodi):
        try:
            if not isinstance(nama, str):
                raise TypeError("Nama harus berupa string")
            if not isinstance(nim, str):
                raise TypeError("NIM harus berupa string")
            if not isinstance(umur, int):
                raise TypeError("Umur harus berupa integer")
            if not isinstance(prodi, str):
                raise TypeError("Prodi harus berupa string")

            if umur < 20:
                raise ValueError("Umur tidak boleh negatif")

            self.nama = nama
            self.nim = nim
            self.umur = umur
            self.prodi = prodi
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")

    def tampilkan_detail(self):
        print("Detail Mahasiswa:")
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Umur: {self.umur}")
        print(f"Prodi: {self.prodi}")

# Contoh penggunaan
mhs = Mahasiswa()
mhs.input_data("Miram", "12345678", 20, "Informatika")
mhs.tampilkan_detail()

# Contoh error handling
mhs.input_data("Budi", "87654321", -1, "Sistem Informasi")  # Umur negatif
mhs.input_data("Cici", 12345678, 21, "Informatika")  # NIM bukan string
