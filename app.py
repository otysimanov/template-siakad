from flask import Flask, render_template
import datetime
# ===============================================

# Starter Template Flask
# By Makassar Coding

# ================================================
# static_folder digunakan untuk Menentukan Nama Folder Penyimpanan Asset
# static_url_path digunakan untuk URL static, sebaiknya dikosongkan
app = Flask(__name__, static_folder='static', static_url_path='')
# Untuk Menggunakan session pada flask perlu menambahkan secret_key pada app
# app.secret_key = 'iNiAdalahsecrEtKey'
# Untuk Mentukan Batas Waktu Session hanya 7 hari. bila tidak ingin menentukan waktu session bisa di hapus saja
app.permanent_session_lifetime = datetime.timedelta(days=7)


# Import mahasiswaapp yang ada pada folder backend
from backend.mahasiswa import mahasiswaapp

# Ini untuk mendaftarkan Blueprint yang ada pada folder backend
# dalam contoh kasus ini adalah mendaftarkan mahasiswa.py yang ada pada folder backend

app.register_blueprint(mahasiswaapp)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login')
def login():
    return render_template('login.html')


# Untuk Menjalankan Program Flask
# Silahkan ganti port untuk memilih port yang ingin digunakan
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)