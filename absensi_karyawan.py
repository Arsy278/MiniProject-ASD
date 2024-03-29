from datetime import datetime
import os
os.system('cls')

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')
class colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[33m'

class PendataanKehadiran:
    def __init__(self):
        self.kehadiran_karyawan = {
            "nama_karyawan": "arsy",
            "waktu": []
        }

    def catat_kehadiran(self, nama_karyawan, tanggal):
        if nama_karyawan in self.kehadiran_karyawan["nama_karyawan"]:
            self.kehadiran_karyawan["waktu"] = ({"waktu":tanggal})
            input(f"Tekan {colors.YELLOW}Enter{colors.RESET} untuk melanjutkan...")
        else:
            print(f"{colors.RED}Nama tidak terdaftar di dalam perusahaan.{colors.RESET}")
            input(f"Tekan {colors.YELLOW}Enter{colors.RESET} untuk melanjutkan...")

    def lihatKehadiran(self, nama_karyawan):
        if nama_karyawan in self.kehadiran_karyawan["nama_karyawan"]:
            print("\nDaftar Hadir:")
            print("Nama Karyawan: ", nama_karyawan)
            print("Waktu: ", tanggal)
            input(f"Tekan {colors.YELLOW}Enter{colors.RESET} untuk melanjutkan...")
        else:
            print(f"{colors.RED}Karyawan tidak ditemukan dalam data kehadiran.{colors.RESET}")
            input(f"Tekan {colors.YELLOW}Enter{colors.RESET} untuk mencoba lagi...")

    def perbaruiKehadiran(self, nama_karyawan, tanggal):
        if nama_karyawan in self.kehadiran_karyawan["nama_karyawan"]:
            tanggal = datetime.now().strftime("%d-%m-%Y, %H:%M")
            print(f"\n{colors.GREEN}Absensi berhasil diperbarui!{colors.RESET}, berikut deskripsi absensi :")
            print("Nama Karyawan: ",nama_karyawan)
            print("Tanggal & Jam: ",tanggal)
            self.kehadiran_karyawan["waktu"] = ({"waktu":tanggal})
            input(f"Tekan {colors.YELLOW}Enter{colors.RESET} untuk melanjutkan...")
        else:
            print("Karyawan tidak ditemukan dalam data kehadiran.")
            input(f"Tekan {colors.YELLOW}Enter{colors.RESET} untuk mencoba lagi...")

    def hapusDataKehadiran(self, nama_karyawan):
        if nama_karyawan in self.kehadiran_karyawan["nama_karyawan"]:
            del self.kehadiran_karyawan["nama_karyawan"]
            print("Data kehadiran karyawan berhasil dihapus!")
            input(f"Tekan {colors.YELLOW}Enter{colors.RESET} untuk melanjutkan...")
        else:
            print("Karyawan tidak ditemukan dalam data kehadiran.")

pendataan = PendataanKehadiran()

def ambil_input():
    nama_karyawan = input("Masukkan Nama: ")
    tanggal = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    print(f"\n{colors.GREEN}Absensi berhasil!{colors.RESET}, berikut deskripsi waktu absensi :")
    print("Nama: ",nama_karyawan)
    print("Tanggal & Jam: ",tanggal)
    return nama_karyawan, tanggal

while True:
    bersihkan_layar()
    print(f"{'-'*40:^40}")
    print(f"{'Program Pendataan Kehadiran Karyawan':^40}")
    print(f"{'-'*40:^40}")
    print("Pilihan Menu:")
    print("1. Isi Absensi")
    print("2. Lihat Absensi")
    print("3. Perbarui Data Absensi")
    print("4. Hapus Absensi")
    print("5. Keluar")

    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == '1':
        nama_karyawan, tanggal = ambil_input()
        pendataan.catat_kehadiran(nama_karyawan, tanggal)
    elif pilihan == '2':
        pendataan.lihatKehadiran(nama_karyawan)
    elif pilihan == '3':
        pendataan.perbaruiKehadiran(nama_karyawan, tanggal)
    elif pilihan == '4':
        nama_karyawan = input("Masukkan Nama Karyawan: ")
        pendataan.hapusDataKehadiran(nama_karyawan)
    elif pilihan == '5':
        print("Terima kasih!.")
        break
    else:
        print("Input tidak valid. Silakan pilih menu yang sesuai.")