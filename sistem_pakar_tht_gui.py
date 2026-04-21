import tkinter as tk
from tkinter import messagebox

# ================= DATA GEJALA =================
gejala = [
    ("G1", "Apakah mengalami nafas abnormal?"),
    ("G2", "Apakah suara menjadi serak?"),
    ("G3", "Apakah terdapat perubahan pada kulit?"),
    ("G4", "Apakah telinga terasa penuh?"),
    ("G5", "Apakah terasa nyeri saat bicara atau menelan?"),
    ("G6", "Apakah mengalami nyeri tenggorokan?"),
    ("G7", "Apakah mengalami nyeri leher?"),
    ("G8", "Apakah terjadi pendarahan hidung?"),
    ("G9", "Apakah telinga berdenging?"),
    ("G10", "Apakah air liur menetes?"),
    ("G11", "Apakah terjadi perubahan suara?"),
    ("G12", "Apakah mengalami sakit kepala?"),
    ("G13", "Apakah nyeri di pinggir hidung?"),
    ("G14", "Apakah mengalami serangan vertigo?"),
    ("G15", "Apakah getah bening membengkak?"),
    ("G16", "Apakah leher bengkak?"),
    ("G17", "Apakah hidung tersumbat?"),
    ("G18", "Apakah mengalami infeksi sinus?"),
    ("G19", "Apakah berat badan menurun?"),
    ("G20", "Apakah mengalami nyeri telinga?"),
    ("G21", "Apakah selaput lendir berwarna merah?"),
    ("G22", "Apakah ada benjolan di leher?"),
    ("G23", "Apakah tubuh terasa tidak seimbang?"),
    ("G24", "Apakah bola mata bergerak tidak normal?"),
    ("G25", "Apakah mengalami nyeri wajah?"),
    ("G26", "Apakah dahi terasa sakit?"),
    ("G27", "Apakah mengalami batuk?"),
    ("G28", "Apakah tumbuh sesuatu di mulut?"),
    ("G29", "Apakah ada benjolan di leher?"),
    ("G30", "Apakah nyeri di antara mata?"),
    ("G31", "Apakah terjadi radang gendang telinga?"),
    ("G32", "Apakah tenggorokan terasa gatal?"),
    ("G33", "Apakah hidung meler?"),
    ("G34", "Apakah mengalami tuli?"),
    ("G35", "Apakah mengalami mual atau muntah?"),
    ("G36", "Apakah tubuh terasa letih dan lesu?"),
    ("G37", "Apakah mengalami demam?")
]

# ================= KNOWLEDGE BASE =================
knowledge_base = {
    "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
    "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
    "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
    "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
    "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
    "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
    "Kanker Leher dan Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
    "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
    "Contact Ulcers": ["G5", "G2"],
    "Abses Parafaringeal": ["G5", "G16"],
    "Barotitis Media": ["G12", "G20"],
    "Kanker Nasofaring": ["G17", "G8"],
    "Kanker Tonsil": ["G6", "G29"],
    "Neuronitis Vestibularis": ["G35", "G24"],
    "Meniere": ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34", "G9"],
    "Vertigo Postular": ["G24"]
}

# ================= VAR GLOBAL =================
i = 0
gejala_user = []

# ================= FUNGSI =================
def tampil():
    if i < len(gejala):
        info.config(text=f"Pertanyaan {i + 1} dari {len(gejala)}")
        label.config(text=gejala[i][1])
    else:
        hasil()

def klik(pilih):
    global i
    if pilih:
        gejala_user.append(gejala[i][0])
    i += 1
    tampil()

def hasil():
    hasil_diagnosa = []

    for nama, daftar_gejala in knowledge_base.items():
        cocok = len(set(gejala_user) & set(daftar_gejala))
        total = len(daftar_gejala)

        if cocok >= 2:
            persen = cocok / total * 100
            hasil_diagnosa.append((nama, persen, cocok, total))

    hasil_diagnosa.sort(key=lambda x: x[1], reverse=True)

    if hasil_diagnosa:
        teks = "Berdasarkan gejala yang Anda masukkan:\n\n"
        for nama, persen, cocok, total in hasil_diagnosa[:5]:
            teks += f"• {nama} ({persen:.0f}%)\n"
            teks += f"  Kecocokan: {cocok} dari {total} gejala\n\n"
    else:
        teks = (
            "Tidak ditemukan penyakit yang cukup cocok berdasarkan gejala yang dipilih.\n\n"
            "Saran: Silakan konsultasi ke dokter atau tenaga medis."
        )

    messagebox.showinfo("Hasil Diagnosa", teks)

    btn_ya.pack_forget()
    btn_tidak.pack_forget()
    btn_mulai.pack(pady=8)

    info.config(text="Diagnosa selesai")
    label.config(text="Klik tombol di bawah ini jika ingin memulai diagnosa lagi.")

def mulai():
    global i, gejala_user
    i = 0
    gejala_user = []
    btn_mulai.pack_forget()
    btn_ya.pack(side="left", padx=8)
    btn_tidak.pack(side="left", padx=8)
    tampil()

# ================= GUI =================
root = tk.Tk()
root.title("Sistem Pakar Diagnosa Penyakit THT")
root.geometry("500x270")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

judul = tk.Label(
    root,
    text="Sistem Pakar Diagnosa Penyakit THT",
    font=("Arial", 13, "bold"),
    bg="#f2f2f2",
    fg="black"
)
judul.pack(pady=(18, 8))

info = tk.Label(
    root,
    text="Tekan tombol untuk memulai diagnosa",
    font=("Arial", 10),
    bg="#f2f2f2"
)
info.pack()

label = tk.Label(
    root,
    text="Klik 'Mulai Diagnosa' untuk mulai.",
    font=("Arial", 11),
    bg="white",
    width=44,
    height=5,
    wraplength=380,
    relief="groove",
    bd=1,
    justify="center"
)
label.pack(pady=15)

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack()

btn_ya = tk.Button(
    frame,
    text="Ya",
    width=10,
    bg="#d9d9d9",
    command=lambda: klik(True)
)

btn_tidak = tk.Button(
    frame,
    text="Tidak",
    width=10,
    bg="#d9d9d9",
    command=lambda: klik(False)
)

btn_mulai = tk.Button(
    root,
    text="Mulai Diagnosa",
    width=18,
    font=("Arial", 10, "bold"),
    bg="#d9d9d9",
    command=mulai
)
btn_mulai.pack(pady=8)

root.mainloop()