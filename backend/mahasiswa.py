from flask import Blueprint, render_template, redirect, url_for, jsonify, request

# Blueprint di gunakan untuk memisahkan file. sehingga seluruh syntax tidak tertumpuk pada app.py saja
# ini juga dapat merapikan kode jadi lebih mudah untuk di kembangkan
# Blueprint perlu di daftarkan di app.py
# pembuatan nama blueprint disarankan sesuai dengan nama file namun di tambahkan juga app di belakang variablenya
# contoh : mahasisswaapp


# Mirip dengan class Flask pada app.py namun ini berupa blueprint
mahasiswaapp = Blueprint('mahasiswaapp', __name__)

@mahasiswaapp.route('/mahasiswa')
def daftar_mahasiswa():
    return render_template('mahasiswa/index.html')

@mahasiswaapp.route('/mahasiswa/tambah')
def tambah_mahasiswa():
    return render_template('mahasiswa/tambah.html')

@mahasiswaapp.route('/mahasiswa/lihat/')
def lihat_mahasiswa():
    return render_template('mahasiswa/lihat.html')

@mahasiswaapp.route('/mahasiswa/edit/')
def edit_mahasiswa():
    return render_template('mahasiswa/edit.html')

@mahasiswaapp.route('/mahasiswa/hapus/')
def hapus_mahasiswa():
    return redirect(url_for('mahasiswaapp.daftar_mahasiswa'))