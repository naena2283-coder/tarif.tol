Cuplikan layar 2026-04-09 203840.png
Cuplikan layar 2026-04-09 203902.png

dibagian hitung_biaya(harga, marketplace) yang berfungsi untuk menghitung biaya admin dan hasil akhir.
di sini harga bertipe float karena berupa angka, sedangkan marketplace bertipe string karena berupa teks 
seperti “tokopedia”, “shopee” dan "lazada. pada bagian percabangan if marketplace "tokopedia" dan seterusnya, program menentukan besar persentase biaya. 
variabel persen bertipe float karena berisi angka desimal seperti 0.03 atau 0.04. Percabangan ini penting agar tiap 
marketplace punya biaya berbeda. lalu pada bagian biaya = harga * persen dan hasil = harga - biaya, program melakukan perhitungan.
biaya adalah potongan, sedangkan hasil adalah uang bersih yang didapat. Keduanya bertipe float karena hasil perhitungan angka
masuk ke bagian @app.route("/", methods=["GET", "POST"]), ini berfungsi menentukan halaman utama web. 
method GET digunakan saat membuka halaman, sedangkan POST digunakan saat user mengirim data dari form
fungsi def home() adalah fungsi utama untuk mengatur logika halaman. Di dalamnya ada hasil = None dan biaya = None yang berarti nilai awal masih 
kosong. Tipe datanya adalah NoneTypes saat if request.method == "POST":, program mulai mengambil data dari form. request.form["harga"] awalnya bertipe string, lalu diubah menjadi
float supaya bisa dihitung. sedangkan marketplace tetap string. kemudian fungsi hitung_biaya dipanggil untuk menghitung hasilnya.
setelah itu nilai biaya dan hasil diubah menjadi string dengan format rupiah #menggunakan f"Rp {biaya:,.0f}", jadi tampilannya lebih rapi.
terakhir, return render_template("marketplace.html", hasil=hasil, biaya=biaya) berfungsi mengirim data ke file HTML agar bisa ditampilkan di web. 
di sini hasil dan biaya sudah bertipe string. pada bagian paling bawah, if _name_ == "_main_": digunakan agar program hanya berjalan saat file ini dijalankan langsung. 
app.run(debug=True, #port=5050) akan menjalankan server di port 5050, dan debug=True membantu menampilkan error jika ada masalah.


apa yang terjadi jika variabelnya saya tambah, jadi saya menambahkan persen ke kode saya
