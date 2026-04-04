from flask import Flask, request, render_template

app = Flask(__name__)

def hitung_biaya(harga, marketplace):
    if marketplace == "tokopedia":
        persen = 0.03
    elif marketplace == "shopee":
        persen = 0.04
    else:
        persen = 0.05

    biaya = harga * persen
    hasil = harga - biaya

    return biaya, hasil

@app.route("/", methods=["GET", "POST"])
def home():
    hasil = None
    biaya = None

    if request.method == "POST":
        harga = float(request.form["harga"])
        marketplace = request.form["marketplace"]

        biaya, hasil = hitung_biaya(harga, marketplace)

        biaya = f"Rp {biaya:,.0f}"
        hasil = f"Rp {hasil:,.0f}"

    return render_template("marketplace.html", hasil=hasil, biaya=biaya)


if __name__ == "__main__":
    app.run(debug=True, port=5050)