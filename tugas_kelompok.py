from collections import deque

class Restoran:
    def __init__(self):
        self.antrian = deque()   # untuk queue & VIP
        self.stack_batal = []    # untuk undo

    def tambah_pelanggan(self, nama, tipe="biasa"):
        if tipe == "VIP":
            self.antrian.appendleft(nama)
            print(f"[VIP] {nama} masuk ke depan antrian.")
        else:
            self.antrian.append(nama)
            print(f"{nama} masuk ke antrian.")

    def batalkan_pesanan(self):
        if not self.antrian:
            print("Tidak ada pesanan untuk dibatalkan.")
            return
        
        pelanggan = self.antrian.pop()
        self.stack_batal.append(pelanggan)
        print(f"{pelanggan} membatalkan pesanan.")

    def undo_pembatalan(self):
        if not self.stack_batal:
            print("Tidak ada pembatalan untuk di-undo.")
            return
        
        pelanggan = self.stack_batal.pop()
        self.antrian.append(pelanggan)
        print(f"{pelanggan} dikembalikan ke antrian.")

    def proses_pesanan(self):
        if not self.antrian:
            print("Tidak ada pesanan.")
            return
        
        pelanggan = self.antrian.popleft()
        print(f"Pesanan {pelanggan} sedang diproses...")

    def tampilkan_antrian(self):
        print("\n=== ANTRIAN SAAT INI ===")
        if not self.antrian:
            print("Kosong")
        else:
            for i, p in enumerate(self.antrian, 1):
                print(f"{i}. {p}")
        print("========================\n")


# ===== SIMULASI =====
resto = Restoran()

resto.tambah_pelanggan("Asror")
resto.tambah_pelanggan("Rosihan")
resto.tambah_pelanggan("Zaki", "VIP")
resto.tampilkan_antrian()

resto.proses_pesanan()
resto.tampilkan_antrian()

resto.batalkan_pesanan()
resto.tampilkan_antrian()

resto.undo_pembatalan()
resto.tampilkan_antrian()
