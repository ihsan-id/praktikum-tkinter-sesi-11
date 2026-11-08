# Praktikum Tkinter Sesi 11
## Aplikasi Pendaftaran Kegiatan Mahasiswa

### Tujuan
Membangun aplikasi GUI menggunakan Python Tkinter dengan memanfaatkan berbagai widget, event handling, validasi input, menu, dan dialog.

### Fitur
- Entry untuk memasukkan nama mahasiswa.
- Combobox untuk memilih program studi.
- Radiobutton untuk memilih jenis kelamin.
- Checkbutton untuk memilih kegiatan.
- Text untuk menuliskan alasan mengikuti kegiatan.
- Tombol Submit untuk memvalidasi dan menampilkan ringkasan pendaftaran.
- Tombol Reset untuk mengosongkan formulir.
- Messagebox untuk notifikasi dan validasi.
- Menu File dengan pilihan Reset Form dan Exit/Keluar.
- Menu Bantuan yang membuka jendela About menggunakan Toplevel.
- Listbox untuk menampilkan dan memilih daftar kegiatan (multi-select).
- Validasi agar nama tidak boleh kosong, serta validasi isian penting lainnya.
- Tombol Enter untuk menjalankan Submit.
- Frame dan geometry manager `grid()` serta `pack()` untuk mengatur tata letak.

### Persyaratan
- Python 3.x
- Tkinter (umumnya sudah tersedia pada instalasi Python standar).

### Cara Menjalankan
1. Pastikan Python 3 sudah terpasang.
2. Buka terminal atau Command Prompt pada folder proyek.
3. Jalankan perintah:

   ```bash
   python main.py
   ```

4. Isi formulir, pilih kegiatan, lalu tekan tombol **Submit** atau tombol **Enter**.
5. Tekan **Reset** untuk mengosongkan formulir.

### Struktur Folder
```text
praktikum-tkinter-sesi-11/
├── main.py
├── README.md
└── screenshot/
    └── aplikasi.png
```

### Screenshot
Jalankan aplikasi, lalu ambil screenshot jendela aplikasi yang sedang terbuka. Simpan dengan nama `aplikasi.png` di dalam folder `screenshot/`.

### Catatan
Nama program studi dan daftar kegiatan pada aplikasi merupakan contoh dan dapat disesuaikan dengan kebutuhan praktikum.
