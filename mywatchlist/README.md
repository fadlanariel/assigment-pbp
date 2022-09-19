Link heroku : [https://tugasduapbp.herokuapp.com/mywatchlist/](https://tugasduapbp.herokuapp.com/mywatchlist/)

1. JSON dan XML adalah penyajian data dalam bentuk raw data tanpa sedangkan HTML menyajikan dalam suatu susunan. XML hanyalah informasi yang dibungkus di dalam tag. JSON merupakan turunan dari Object JavaScript dan didesain menjadi self-describing sehingga mudah dipahami.
   
2. Dalam mengembangkan sebuah platform pastinya ada kala dimana kita memerlukan data dari suatu database. Untuk itu kita perlu data delivery agar kita bisa mengirim data dari suatu stack ke stack lain. Data yang dikirim memiliki bermacam bentuk dan contoh pengiriman data adalah melalui format HTML, JSON, dan XML.
   
3. Pertama buat dulu aplikasi bernama `mywatchlist` dalam project. setelah itu implementasikan routing agar aplikasi bisa ditampilkan dengan menambahkan `mywatchlist` ke INSTALLED_APPS di `settings.py`. Setelah itu buat fungsi di `views` untuk mengurus request dan implementasikan routing ke `urls`. Lalu buat `models` dan buat datanya dalam format JSON. Lalu tambahkan fungsi dan routing untuk menampilkan data dalam format XML dan JSON. Terakhir deploy ke heroku.

![Postman mywatchlist/html](https://github.com/fadlanariel/assignment-pbp/blob/main/mywatchlist/watchlist-html.jpg?raw=true)
![Postman mywatchlist/xml](https://github.com/fadlanariel/assignment-pbp/blob/main/mywatchlist/watchlist-xml.jpg?raw=true)
![Postman mywatchlist/json](https://github.com/fadlanariel/assignment-pbp/blob/main/mywatchlist/watchlist-json.jpg?raw=true)