# UAS-PBO
# Nama: Muhammad Rozagi
# NPM : G1A022008
# Kelompok : 5 
# ● Tugas Akhir Pemrograman Berorientasi Objek (Kelompok 5) 
Pemrograman berorientasi objek telah menjadi pendekatan yang dominan dalam pengembangan perangkat lunak modern. Dengan menggunakan paradigma ini, pengembang perangkat lunak dapat membagi program menjadi 
serangkaian objek yang saling berinteraksi, memungkinkan kode yang lebih terstruktur, modular, dan mudah diubah.Dalam rangka memperkuat pemahaman dan penerapan pemrograman berorientasi objek, kami memilih untuk mengembangkan proyek game 
Hangman. Hangman adalah permainan tebak kata sederhana yang sering dimainkan secara tradisional dengan kertas dan pena. Dalam permainan ini, pemain harus menebak kata dengan menebak huruf satu per satu. Setiap tebakan 
yang salah menggambar bagian tubuh manusia pada gantungan.

Proyek ini bertujuan untuk mengimplementasikan prinsip-prinsip pemrograman berorientasi objek dalam pengembangan game Hangman. Dengan membagi program menjadi kelas-kelas yang sesuai, kami akan memanfaatkan konsep seperti enkapsulasi, pewarisan, polimorfisme, dan abstraksi untuk membangun game Hangman yang interaktif dan menyenangkan.
Selain itu, proyek ini juga bertujuan untuk meningkatkan pemahaman kami tentang penggunaan struktur data dan algoritma dalam pengembangan permainan. Kami akan menggunakan struktur data yang sesuai untuk menyimpan kata-kata yang akan ditebak, serta mengimplementasikan algoritma yang efisien untuk memeriksa kebenaran tebakan pemain dan menggambar elemen-elemen visual pada layar.

# ● Penjelasan Singkat Kode yang dibuat 
Dalam program Game Hangman yang kami buat , terdapat beberapa metode yang saya gunakan yaitu sebagai berikut :
Berikut adalah penjelasan singkat untuk setiap fungsi/metode yang digunakan dalam kode permainan Hangman:

● ```ambil_kata_kunci()```
Fungsi ini menggunakan modul random untuk memilih secara acak sebuah kata kunci dari daftar kata yang sudah ditentukan. Daftar kata-kunci disimpan dalam variabel kata_kunci. Fungsi random.choice() digunakan untuk memilih satu kata secara acak dari daftar tersebut, kemudian kata tersebut dikembalikan.

● ```tampilkan_gantungan_hangman(kesalahan)```
Fungsi ini mengembalikan gambar gantungan hangman berdasarkan jumlah kesalahan yang terjadi. Gambar-gambar gantungan hangman disimpan dalam sebuah list dengan menggunakan notasi multiline string. Pada setiap indeks list, terdapat representasi gambar gantungan hangman yang sesuai dengan jumlah kesalahan. Indeks list yang digunakan ditentukan oleh parameter kesalahan.

● ```tampilkan_kata_tersembunyi(kata, tebakan)```
Fungsi ini menerima dua argumen, yaitu kata (kata kunci yang harus ditebak) dan tebakan (list huruf yang sudah ditebak). Fungsi ini mengembalikan sebuah string yang menampilkan kata yang sedang ditebak, dengan mengganti huruf-huruf yang belum ditebak dengan karakter garis bawah ("_"). Untuk setiap huruf dalam kata, fungsi ini memeriksa apakah huruf tersebut sudah ada dalam tebakan. Jika sudah ada, huruf tersebut ditampilkan. Jika belum, huruf tersebut diganti dengan karakter garis bawah.

● ```tampilkan_status(tebakan, kesalahan)```
Fungsi ini menerima dua argumen, yaitu tebakan (list huruf yang sudah ditebak) dan kesalahan (jumlah kesalahan yang terjadi). Fungsi ini menampilkan status tebakan yang sudah dilakukan, termasuk tebakan yang benar dan jumlah kesalahan yang telah terjadi. Status ini ditampilkan dalam bentuk teks di konsol.

● ```main()```
Fungsi utama permainan Hangman. Di dalamnya, permainan dimulai dengan menampilkan gambar gantungan hangman awal dan kata tersembunyi yang harus ditebak. Selanjutnya, pemain diminta untuk memasukkan tebakan huruf. Pada setiap langkah, fungsi ini memeriksa apakah tebakan sudah pernah dilakukan sebelumnya dengan memeriksa apakah huruf tersebut sudah ada dalam tebakan. Jika tebakan belum pernah dilakukan sebelumnya, fungsi memeriksa apakah huruf tersebut benar atau salah. Jika benar, huruf ditambahkan ke dalam tebakan dan kata tersembunyi yang ditampilkan diperbarui. Jika salah, jumlah kesalahan ditambah satu. Permainan berakhir ketika pemain berhasil menebak kata dengan benar atau ketika jumlah kesalahan mencapai batas maksimum. Pesan yang sesuai akan ditampilkan di konsol.

● ```if name == 'main```
Ini adalah blok yang mengeksekusi fungsi main() hanya jika file ini dijalankan secara langsung sebagai skrip, bukan diimpor sebagai modul.
Kode ini dapat digunakan untuk membuat permainan Hangman sederhana di lingkungan Python. Pemain akan diminta untuk menebak huruf-huruf dalam kata kunci yang tersembunyi dan akan melihat representasi visual dari gantungan Hangman saat mereka membuat kesalahan.

Sekian untuk penjelasan kode serta tugas akhir dari mata kuliah PBO ( Pemrograman Berorientasi Objek ) . 
Terimakasih atas bimbingan dari abang selama setengah semester ini . 

