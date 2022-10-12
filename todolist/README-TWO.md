# TUGAS 6
---
1. Perbedaan *asynchronous programming* dengan *synchronous programming* adalah *asynchronous programming* menjalankan task atau operasi secara bersamaan tanpa ada urutan tertentu sehingga tidak perlu menunggu operasi atau task lain selesai. Sedangkan *synchronous programming* mengerjakan task atau operasi secara terurut atau bergantian.
<br>

2. *Event-Driven Programming* adalah paradigma dimana alur atau *flow* dari program akan ditentukan oleh *event* seperti *action* dari user. Contoh penerapan dalam tugas ini adalah penambahan task dimana task akan ditambahkan apabila user mengisi form dan menekan *button* untuk menambahkan task. Contoh kedua adalah tombol delete task dimana data dan tampilan dari task akan dihapus apabila user menekan tombol *delete*.
<br>

3. AJAX merupakan singkatan dari *asynchronous JavaScript and XML*. AJAX memungkinkan halaman web diupdate secara *asynchronous*. AJAX hanya menyampaikan informasi yang berubah atau *updated* ke dan dari server.
<br>

4. Pertama adalah membuat view baru untuk menampilkan data json. Setelah itu dapatkan data untuk digunakan di `todolist.html` dengan menggunakan AJAX GET yaitu dengan mengambil data dari url yang terhubung ke view untuk data json yang telah dibuat. Jika berhasil mengambil data maka setiap ada update data kosongkan container yang digunakan untuk menyimpan `cards` lalu untuk tiap data yang didapatkan buat `card` dengan meng-*append* card yang ditulis sebagai string di script ke container yang digunakan untuk menyimpan `card`. Lalu buat `modal` untuk menampilkan `form` dengan menggunakan bootstrap. Masukkan `form` kedalam body dari `modal` dan hubungkan `button` kepada fungsi-fungsinya. Buat fungsi untuk meng-*handle* form di script menggunakan AJAX POST dengan menghubungkannya ke fungsi yang ada di `views` untuk mendapatkan value dari `form` dan menambahkannya ke database. Untuk 