# Tugas Praktek
# Di luar sudah menggelap. Gerobak nasi goreng yang biasanya menunggu di depan kantor tiap pukul tujuh sudah tampak. Aku masih saja larut dalam pekerjaan.

# “Masih di sini, Aksara? Belum pulang?” tegur Senja yang baru saja keluar dari ruangan.

# “Masih ngurusin proyek Tenaga Lepas. Ini baru dapat rikues lagi untuk nambahin class yang merepresentasikan masing-masing pekerjaan di divisi ini.”

# “Hmm, kamu pakai konsep inherintance saja, akan lebih mudah,” saran Senja sebelum pulang. Sejujurnya, aku juga mau pulang. Teringat kasur di rumah yang siap untuk rebahan. Kalau begitu, pekerjaan ini harus cepat diselesaikan.

# Di divisiku ada empat bidang pekerjaan, mulai dari analisis data, ilmuwan data, pembersih data, dan dokumenter teknis. Setiap peran punya sistem penerimaan fee yang berbeda. Ini yang bikin rumit. Misalnya, ilmuwan data akan mendapat insentif tambahan sebesar 10% dari proyek yang dikerjakan, dan dokumenter teknis adalah satu-satunya peran yang tidak menerima insentif dari proyek.

# Oke, tenang. Ini pasti bisa, tinggal masukkin saja variabelnya satu persatu. Semangat!, batinku sembari ditemani suara abang nasi goreng yang menjajakan makanannya.

# Aku kembali bekerja dengan data dan kode-kode ini di code editor.

# Definisikan class Karyawan sebagai parent class
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur 
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self,jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
# Definisikan class TenagaLepas sebagai child class dari
# class Karyawan
class TenagaLepas(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan, 0)
    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan += nilai_proyek * 0.01
# Definisikan class AnalisData sebagai child class dari
# class Karyawan
class AnalisData(Karyawan): 
    pass
# Definisikan class IlmuwanData sebagai child class dari
# class Karyawan
class IlmuwanData(Karyawan):
    def tambahan_proyek(self, nilai_proyek): 
        self.pendapatan_tambahan += 0.1 * nilai_proyek
# Definisikan class PembersihData sebagai child class dari
# class TenagaLepas
class PembersihData(TenagaLepas): 
    pass
# Definisikan class DokumenterTeknis sebagai child class dari
# class TenagaLepas
class DokumenterTeknis(TenagaLepas):
    def tambahan_proyek(self, jumlah_tambahan): 
        return