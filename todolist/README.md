Link heroku : [https://tugasduapbp.herokuapp.com/todolist/](https://tugasduapbp.herokuapp.com/todolist/)

1. `{% csrf_token %}` adalah sebuah token random yang berfungsi untuk mencegah serangan bahaya. Saat page di generate semua request akan di check terhadap token tersebut. Bila `{% csrf_token %}` tidak ditambahkan pada `<form>` maka page tersebut akan memiliki sebuah celah bagi penyerang untuk memaksa user yang terotentifikasi yang logged-in untuk melakukan sebuah perubahan atau suatu aksi tanpa sepengetahuan dan izin user tersebut.

2. `<form>` dapat dibuat secara manual tanpa menggunakan `{{ form.as_table }}`. Hal ini dapat dilakukan dengan menggunakan tag `<input>` di template secara langsung.

3. Data yang diisi oleh pengguna disimpan sebagai object dan dikirim ke database melalui `models`, setelah itu data dari database dikirim ke views untuk di petakan ke template untuk ditunjukkan sebagai response

4. Pertama buat app todolist dengan `python manage.py startapp todolist`. Setelah itu menambahkan `todolist` ke `INSTALLED_APPS` dan urls untuk `todolist` ke settings.py. Lalu implementasikan routing di `urls` agar dapat menerima request dan juga implementasikan `views` dengan membuat fungsi untuk menunjukan halaman `todolist`, login, register, logout, serta pembuatan task. Buat models untuk menyimpan data dari task dan user. Buat form pembuatan task secara manual di `create_task.html`. Lalu setalh selesai data dari form tersebut akan disimpan dan ditampilkan kembali di `todolist.html`