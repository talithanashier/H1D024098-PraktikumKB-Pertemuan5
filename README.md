Talitha Maharani Nashier
H1D024098
Shift C

# Sistem Pakar Diagnosa Penyakit THT

## Deskripsi
Program ini merupakan aplikasi berbasis GUI yang dibuat menggunakan Python dan library Tkinter. Sistem ini digunakan untuk membantu pengguna dalam mengidentifikasi kemungkinan penyakit THT (Telinga, Hidung, Tenggorokan) berdasarkan gejala yang dialami.

Pengguna akan menjawab beberapa pertanyaan dengan pilihan "Ya" atau "Tidak", kemudian sistem akan memproses jawaban tersebut untuk menampilkan hasil diagnosa.

## Fitur Utama
Diagnosa penyakit THT berbasis gejala  
Tampilan GUI sederhana dan interaktif  
Input menggunakan tombol "Ya" dan "Tidak"  
Menampilkan hasil diagnosa dalam bentuk popup  
Dapat mengulang proses diagnosa  

## Struktur Program
Program terdiri dari beberapa bagian utama:

Data Gejala → daftar pertanyaan yang diberikan ke pengguna  
Knowledge Base → data penyakit dan gejalanya  
Fungsi Diagnosa → proses pencocokan gejala  
Antarmuka GUI → tampilan interaksi pengguna  

## Mekanisme Kerja
Sistem bekerja dengan metode rule-based menggunakan pendekatan forward chaining:

Pengguna menjawab pertanyaan gejala  
Sistem menyimpan jawaban "Ya"  
Sistem mencocokkan dengan knowledge base  
Sistem menghitung kecocokan  
Sistem menampilkan hasil diagnosa  

## Cara Menjalankan Program
Pastikan Python sudah terinstall  
Jalankan file:
sistem_pakar_tht_gui.py
