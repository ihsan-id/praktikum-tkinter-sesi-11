import tkinter as tk
from tkinter import ttk, messagebox

# Aplikasi Pendaftaran Kegiatan Mahasiswa
# Praktikum Python Tkinter - Sesi 11

DAFTAR_KEGIATAN = [
    "Seminar Nasional",
    "Workshop Kewirausahaan",
    "Pelatihan Desain Grafis",
    "Lomba Karya Tulis Ilmiah",
    "Bakti Sosial"
]

def tampilkan_about():
    """Membuka jendela informasi aplikasi."""
    jendela_about = tk.Toplevel(root)
    jendela_about.title("Tentang Aplikasi")
    jendela_about.geometry("350x210")
    jendela_about.resizable(False, False)
    jendela_about.transient(root)

    ttk.Label(
        jendela_about,
        text="Pendaftaran Kegiatan Mahasiswa",
        font=("Arial", 13, "bold")
    ).pack(pady=(22, 10))
    ttk.Label(
        jendela_about,
        text="Aplikasi ini dibuat menggunakan Python Tkinter\\n"
             "untuk memenuhi Praktikum Sesi 11.\\n\\n"
             "Materi: Advanced Widgets dan Event Handling",
        justify="center"
    ).pack(padx=15, pady=5)
    ttk.Button(jendela_about, text="Tutup", command=jendela_about.destroy).pack(pady=10)


def submit_pendaftaran(event=None):
    """Memvalidasi input dan menampilkan ringkasan pendaftaran."""
    nama = entry_nama.get().strip()
    prodi = combo_prodi.get()
    jenis_kelamin = var_gender.get()
    alasan = text_alasan.get("1.0", tk.END).strip()
    kegiatan = [item for item, var in pilihan_kegiatan.items() if var.get()]

    if not nama:
        messagebox.showwarning("Validasi", "Nama tidak boleh kosong!")
        entry_nama.focus_set()
        return

    if not prodi:
        messagebox.showwarning("Validasi", "Silakan pilih program studi!")
        combo_prodi.focus_set()
        return

    if not jenis_kelamin:
        messagebox.showwarning("Validasi", "Silakan pilih jenis kelamin!")
        return

    if not kegiatan:
        messagebox.showwarning("Validasi", "Pilih minimal satu kegiatan!")
        return

    ringkasan = (
        "PENDAFTARAN BERHASIL\\n"
        "================================\\n"
        f"Nama: {nama}\\n"
        f"Program Studi: {prodi}\\n"
        f"Jenis Kelamin: {jenis_kelamin}\\n"
        f"Kegiatan: {', '.join(kegiatan)}\\n"
        f"Alasan: {alasan if alasan else '-'}\\n"
    )

    area_ringkasan.config(state="normal")
    area_ringkasan.delete("1.0", tk.END)
    area_ringkasan.insert(tk.END, ringkasan)
    area_ringkasan.config(state="disabled")

    messagebox.showinfo("Berhasil", f"Pendaftaran atas nama {nama} berhasil disimpan.")


def reset_form():
    """Mengosongkan seluruh isian formulir dan ringkasan."""
    entry_nama.delete(0, tk.END)
    combo_prodi.set("")
    var_gender.set("")
    for var in pilihan_kegiatan.values():
        var.set(False)
    text_alasan.delete("1.0", tk.END)
    listbox_kegiatan.selection_clear(0, tk.END)

    area_ringkasan.config(state="normal")
    area_ringkasan.delete("1.0", tk.END)
    area_ringkasan.config(state="disabled")
    entry_nama.focus_set()


def sinkronkan_listbox(event=None):
    """Memperbarui Checkbutton sesuai pilihan pada Listbox."""
    pilihan = {listbox_kegiatan.get(i) for i in listbox_kegiatan.curselection()}
    for nama_kegiatan, var in pilihan_kegiatan.items():
        var.set(nama_kegiatan in pilihan)


# Jendela utama
root = tk.Tk()
root.title("Pendaftaran Kegiatan Mahasiswa")
root.geometry("850x760")
root.minsize(760, 650)

# Menu aplikasi
menu_bar = tk.Menu(root)
menu_file = tk.Menu(menu_bar, tearoff=0)
menu_file.add_command(label="Reset Form", command=reset_form)
menu_file.add_separator()
menu_file.add_command(label="Exit / Keluar", command=root.destroy)
menu_bar.add_cascade(label="File", menu=menu_file)

menu_bantuan = tk.Menu(menu_bar, tearoff=0)
menu_bantuan.add_command(label="About", command=tampilkan_about)
menu_bar.add_cascade(label="Bantuan", menu=menu_bantuan)
root.config(menu=menu_bar)

# Header
header = ttk.Frame(root, padding=(18, 15))
header.pack(fill="x")
ttk.Label(
    header,
    text="FORMULIR PENDAFTARAN KEGIATAN MAHASISWA",
    font=("Arial", 16, "bold")
).pack(anchor="w")
ttk.Label(
    header,
    text="Silakan lengkapi data diri dan pilih kegiatan yang ingin diikuti.",
    font=("Arial", 9)
).pack(anchor="w", pady=(5, 0))

# Kontainer utama
container = ttk.Frame(root, padding=(18, 5, 18, 15))
container.pack(fill="both", expand=True)
container.columnconfigure(0, weight=1)
container.columnconfigure(1, weight=1)
container.rowconfigure(2, weight=1)

# Data diri
frame_data = ttk.LabelFrame(container, text=" Data Diri ", padding=12)
frame_data.grid(row=0, column=0, sticky="nsew", padx=(0, 8), pady=6)
frame_data.columnconfigure(1, weight=1)

ttk.Label(frame_data, text="Nama Lengkap").grid(row=0, column=0, sticky="w", padx=5, pady=7)
entry_nama = ttk.Entry(frame_data, width=32)
entry_nama.grid(row=0, column=1, sticky="ew", padx=5, pady=7)

ttk.Label(frame_data, text="Program Studi").grid(row=1, column=0, sticky="w", padx=5, pady=7)
combo_prodi = ttk.Combobox(
    frame_data,
    values=[
        "Teknik Informatika",
        "Sistem Informasi",
        "Agrobisnis Perikanan",
        "Manajemen",
        "Akuntansi",
        "Ilmu Komunikasi",
        "Pendidikan"
    ],
    state="readonly"
)
combo_prodi.grid(row=1, column=1, sticky="ew", padx=5, pady=7)

ttk.Label(frame_data, text="Jenis Kelamin").grid(row=2, column=0, sticky="nw", padx=5, pady=7)
var_gender = tk.StringVar(value="")
frame_gender = ttk.Frame(frame_data)
frame_gender.grid(row=2, column=1, sticky="w", padx=5, pady=5)
ttk.Radiobutton(frame_gender, text="Laki-laki", variable=var_gender, value="Laki-laki").pack(anchor="w")
ttk.Radiobutton(frame_gender, text="Perempuan", variable=var_gender, value="Perempuan").pack(anchor="w")

# Pilihan kegiatan dengan Checkbutton dan Listbox
frame_kegiatan = ttk.LabelFrame(container, text=" Pilihan Kegiatan ", padding=12)
frame_kegiatan.grid(row=0, column=1, sticky="nsew", padx=(8, 0), pady=6)
ttk.Label(frame_kegiatan, text="Centang kegiatan yang ingin diikuti:").pack(anchor="w", pady=(0, 5))

frame_check = ttk.Frame(frame_kegiatan)
frame_check.pack(fill="x")
pilihan_kegiatan = {}
for kegiatan in DAFTAR_KEGIATAN:
    var = tk.BooleanVar(value=False)
    pilihan_kegiatan[kegiatan] = var
    ttk.Checkbutton(frame_check, text=kegiatan, variable=var).pack(anchor="w", pady=1)

ttk.Label(frame_kegiatan, text="Daftar kegiatan (bisa pilih lebih dari satu):").pack(anchor="w", pady=(10, 4))
listbox_kegiatan = tk.Listbox(frame_kegiatan, height=5, selectmode=tk.MULTIPLE, exportselection=False)
for kegiatan in DAFTAR_KEGIATAN:
    listbox_kegiatan.insert(tk.END, kegiatan)
listbox_kegiatan.pack(fill="both", expand=True)
listbox_kegiatan.bind("<<ListboxSelect>>", sinkronkan_listbox)

# Alasan mengikuti kegiatan
frame_alasan = ttk.LabelFrame(container, text=" Alasan Mengikuti Kegiatan ", padding=12)
frame_alasan.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=6)
text_alasan = tk.Text(frame_alasan, height=4, wrap="word", font=("Arial", 10))
text_alasan.pack(fill="both", expand=True)

# Tombol aksi
frame_tombol = ttk.Frame(container)
frame_tombol.grid(row=2, column=0, columnspan=2, sticky="new", pady=8)
ttk.Button(frame_tombol, text="Submit", command=submit_pendaftaran).pack(side="left", padx=(0, 8))
ttk.Button(frame_tombol, text="Reset", command=reset_form).pack(side="left")

# Area informasi / ringkasan
frame_info = ttk.LabelFrame(container, text=" Area Informasi / Ringkasan Pendaftaran ", padding=10)
frame_info.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=6)
area_ringkasan = tk.Text(frame_info, height=7, wrap="word", state="disabled", font=("Consolas", 9))
area_ringkasan.pack(fill="both", expand=True)

# Event keyboard: Enter menjalankan Submit
entry_nama.bind("<Return>", submit_pendaftaran)

entry_nama.focus_set()
root.mainloop()
