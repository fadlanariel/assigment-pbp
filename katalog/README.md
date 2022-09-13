Link heroku : [https://tugasduapbp.herokuapp.com/katalog/](https://tugasduapbp.herokuapp.com/katalog/)

1. Chart client request django
   ![Chart client request django](https://github.com/fadlanariel/assignment-pbp/blob/main/katalog/django-client-request-chart.jpg?raw=true)

    Request dari client yang masuk ke server Django akan diproses melalui `urls` yang akan diteruskan ke `views` untuk memproses request tersebut. Jika request memerlukan data dari database, `views` akan memanggil query ke `models` dan data akan diberikan oleh database ke `views`. hasil request yang telah diproses akan diarahkan ke dalam Template HTML yang sudah dibuat dan akan dikembalikan ke user sebagai respons.

2. Virtual environment digunakan untuk menghindari bentrokan versi dari dependencies yang digunakan jika aplikasi digunakan di device lain yang memiliki versi dependencies yang berbeda. Kita bisa membuat aplikasi tanpa menggunakan virtual environment tetapi ada resiko bentrokan versi dependencies jika dibuka di device lain.

3. Pertama buat fungsi pada `views.py` yang menerima `request` dan mengembailkan `render(request, "<namafile>.html", context)`, dengan context berisi data yang diambil dari `models.py` yang mendapatkan data dari `inital_catalog_data.json` dan juga data yang kita tambahkan secara langsung yang akan dimasukan ke HTML. Setelah itu buat routings di `urls.py` ke `views.py` sehingga HTML yang telah kita buat dapat ditambilkan di browser. Untuk men-deploy ke Heroku pertama buat secrets di repositori github bernama HEROKU_APP_NAME yang berisi nama aplikasi yang sudah dibuat dan HEROKU_API_KEY yang berisi API key dari pembuat aplikasi. 