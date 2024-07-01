# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
print("Before importing pandas")
from pytz import timezone
from datetime import datetime, timedelta
import pandas as pd
# from werkzeug.security import check_password_hash
from . import db
from .models import Admin,Jemaat,Absen
import calendar
import pytz
# from .main import app

# app = Flask(__name__)
# CORS(app, resources={r"*": {"origins": "*"}})
# app.secret_key = "rmj_db"
# # # userpass = 'mysql://root:@'
# # # basedir  = '127.0.0.1'
# # # dbname   = '/rmj_db'
# # # socket   = '?unix_socket=/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'
# # # dbname   = dbname + socket
# # # app.config['SQLALCHEMY_DATABASE_URI'] = userpass + basedir + dbname
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost:3306/rmj_db'
# # # app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://jmspa:127.0.0.1/rmj_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# db = SQLAlchemy(app)

# class Jemaat(db.Model):
#     id_jemaat = db.Column('id_jemaat',db.Integer,primary_key=True)
#     nama = db.Column('nama_jemaat',db.String(100))
#     no_telp = db.Column('no_telp',db.String(100))
#     email = db.Column('email',db.String(100))
#     gender = db.Column('gender',db.String(1))
#     hobi = db.Column('hobi',db.String(100))
#     sekolah = db.Column('nama_sekolah',db.String(100))
#     temp_lahir = db.Column('tempat_lahir',db.String(100))
#     tgl_lahir = db.Column('tanggal_lahir',db.DateTime)
#     no_telp_ortu = db.Column('no_telp_ortu',db.String(100))
#     kelas = db.Column('kelas',db.Integer)
#     daerah = db.Column('daerah',db.String(100))
#     kecamatan = db.Column('kecamatan',db.String(100))
#     alamat = db.Column('alamat_lengkap',db.String(100))
#     foto = db.Column('foto_jemaat',db.String(100))
#     status = db.Column('status',db.String(100))
#     def __init__(self, nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status):
#         self.nama = nama
#         self.no_telp = no_telp
#         self.email = email
#         self.gender = gender
#         self.hobi = hobi
#         self.sekolah = sekolah
#         self.temp_lahir = temp_lahir
#         self.tgl_lahir = tgl_lahir
#         self.no_telp_ortu = no_telp_ortu
#         self.kelas = kelas
#         self.daerah = daerah
#         self.kecamatan = kecamatan
#         self.alamat = alamat
#         self.foto = foto
#         self.status = status

# class Absen(db.Model):
#     id_absen = db.Column('id_absen', db.Integer, primary_key=True)
#     id_jemaat = db.Column('id_jemaat', db.Integer)
#     waktu_absen = db.Column('waktu_absen', db.DateTime, default=datetime.now()) #, server_default=db.func.now()
#     def __init__(self,id_jemaat, waktu_absen):
#         self.id_jemaat = id_jemaat
#         self.waktu_absen = waktu_absen

# class Admin(db.Model):
#     id_admin = db.Column('id_admin', db.Integer, primary_key=True)
#     nama_admin = db.Column('nama_admin',db.String(100))
#     password = db.Column('password',db.String(10))
#     tanggal_terdaftar = db.Column('tanggal_terdaftar', db.DateTime, default=datetime.now())
#     last_login = db.Column('last_login', db.DateTime, default=datetime.now())
#     def __init__(self,nama_admin, password, last_login = datetime.now()):
#         self.nama_admin = nama_admin
#         self.password = password
#         self.last_login = last_login


#Dummy
def initiate_table():
    # with app.app_context():
    db.drop_all()
    db.create_all()
    adm1 = Admin('Patrick','123')
    adm2 = Admin('Feodor','111')
    db.session.add_all([adm1,adm2])
    db.session.commit()
    add_dummy_data()


def add_dummy_data():
    # with app.app_context():
    jemaat = [
        ["Au tu lei", "0812333333", "ajosephine49@students.calvin.ac.id", 'P', "tidur", "putus sekolah", "mars", datetime(2020, 5, 17), "08123555555", 10, "universe", "bima sakti", "jl. mars 56", "tidur.jpg", "Active"],
        ["Nicole", "08111111111", "dnicole50@students.calvin.ac.id", "P", "reading", "MIT", "Boston", datetime(2000, 5, 17), "0816666666", 12, "universe", "bima sakti", "jl. bumi 1", "nicole.jpg", "Active"]
        ]
    
    for nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status in jemaat:
        add_jemaat(nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status)

    absen = [
        [1, datetime(2023, 7, 11)],
        [1, datetime(2023, 7, 18)]
    ]

    for id_jemaat, waktu_absen in absen:
        add_absen(id_jemaat, waktu_absen)
        
def add_jemaat(nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status):
    # with app.app_context():
    wib = pytz.timezone('Asia/Jakarta')

    # Get the current time in UTC
    utc_now = datetime.now(pytz.utc)
    new_jemaat = Jemaat(nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status, utc_now.astimezone(wib))
    db.session.add(new_jemaat)
    db.session.commit()
    return {
        'status':'success'
    }

def add_admin(nama_admin, password, last_login):
    # with app.app_context():
    new_admin = Admin(nama_admin, password, last_login)
    db.session.add(new_admin)
    db.session.commit()
    return {
        'status':'success'
    }
    
def add_absen(id_jemaat, waktu_absen):
    # with app.app_context():
    new_absen = Absen(id_jemaat, waktu_absen)
    db.session.add(new_absen)
    db.session.commit() 
    # pengecekan row affected, kalo > 0 itu true (ada yang ke update) kalo ngga false
    return True


# Login Admin
def login_admin(input_nama_admin, input_password):
    # with app.app_context():
    wib = pytz.timezone('Asia/Jakarta')
    admins = db.session.query(Admin).filter_by(nama_admin=input_nama_admin).all()
    true_admin = None
    for admin in admins:
        if admin.password == input_password:
            true_admin = admin
            break
    if true_admin != None:
        utc_now = datetime.now(pytz.utc)
        true_admin.last_login = utc_now.astimezone(wib)
        db.session.commit()
        data = {
            'nama_admin':admin.nama_admin,
            'password':admin.password,
            'last_login':admin.last_login,
            'status':'success',
        }
        print("login berhasil")
        return data
        
    print("login gagal")
    return {'status':'failed',
    }

# 

# Ambil Semua Jemaat    
def get_all_jemaat():
    # with app.app_context():
    jemaat = []
    inv = db.session.query(Jemaat.id_jemaat, Jemaat.nama, Jemaat.no_telp, Jemaat.email, Jemaat.gender, Jemaat.hobi, Jemaat.sekolah, Jemaat.temp_lahir, Jemaat.tgl_lahir, Jemaat.no_telp_ortu, Jemaat.kelas, Jemaat.daerah, Jemaat.kecamatan, Jemaat.alamat, Jemaat.foto, Jemaat.status, Jemaat.tgl_daftar).all()
    for id_jemaat, nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status, tgl_daftar in inv:
        data = {
            'id_jemaat' : id_jemaat, 
            'nama' : nama, 
            'no_telp' : no_telp, 
            'email' : email, 
            'gender' : gender, 
            'hobi' : hobi, 
            'sekolah' : sekolah, 
            'temp_lahir' : temp_lahir, 
            'tgl_lahir' : tgl_lahir, 
            'no_telp_ortu' : no_telp_ortu, 
            'kelas' : kelas,
            'daerah' : daerah, 
            'kecamatan' : kecamatan, 
            'alamat' : alamat, 
            'foto' : foto,
            'status' : status,
            'tgl_daftar':tgl_daftar
        }
        jemaat.append(data)
    return jemaat
    
# Cari Jemaat Dengan ID
def get_jemaat_by_id(id):
    # with app.app_context():
    jmt = db.session.query(Jemaat.id_jemaat, Jemaat.nama, Jemaat.no_telp, Jemaat.email, Jemaat.gender, Jemaat.hobi, Jemaat.sekolah, Jemaat.temp_lahir, Jemaat.tgl_lahir, Jemaat.no_telp_ortu, Jemaat.kelas, Jemaat.daerah, Jemaat.kecamatan, Jemaat.alamat, Jemaat.foto, Jemaat.status, Jemaat.tgl_daftar).filter(Jemaat.id_jemaat == id)
    list_jemaat = []
    for id_jemaat, nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status, tgl_daftar in jmt:
        data = {
            'id_jemaat' : id_jemaat, 
            'nama' : nama, 
            'no_telp' : no_telp, 
            'email' : email, 
            'gender' : gender, 
            'hobi' : hobi, 
            'sekolah' : sekolah, 
            'temp_lahir' : temp_lahir, 
            'tgl_lahir' : tgl_lahir, 
            'no_telp_ortu' : no_telp_ortu, 
            'kelas' : kelas, 
            'daerah' : daerah, 
            'kecamatan' : kecamatan, 
            'alamat' : alamat, 
            'foto' : foto,
            'status' : status,
            'tgl_daftar':tgl_daftar
        }
        list_jemaat.append(data)
    return list_jemaat
    

def delete_jemaat_by_id(id_jemaat):
    try:
        # Query to delete the Jemaat record by id_jemaat
        db.session.query(Jemaat).filter_by(id_jemaat=id_jemaat).delete()
        
        # Commit the transaction
        db.session.commit()
        
        # Return success message or handle as needed
        return "Jemaat record deleted successfully."
    except Exception as e:
        # Rollback the transaction in case of error
        db.session.rollback()
        # Handle the error (e.g., log, return error message, etc.)
        return f"Error deleting Jemaat record: {str(e)}"
    
# Cari jemaat dengan huruf awal
def get_jemaat_by_name(name):
    list_jemaat = []
    jmt = db.session.query(Jemaat.id_jemaat, Jemaat.nama, Jemaat.no_telp, Jemaat.email, Jemaat.gender, Jemaat.hobi, Jemaat.sekolah, Jemaat.temp_lahir, Jemaat.tgl_lahir, Jemaat.no_telp_ortu, Jemaat.kelas, Jemaat.daerah, Jemaat.kecamatan, Jemaat.alamat, Jemaat.foto, Jemaat.status, Jemaat.tgl_daftar).filter(Jemaat.nama.startswith(name)).all()
    for id_jemaat, nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status, tgl_daftar in jmt:
        data = {
            'id_jemaat' : id_jemaat, 
            'nama' : nama, 
            'no_telp' : no_telp, 
            'email' : email, 
            'gender' : gender, 
            'hobi' : hobi, 
            'sekolah' : sekolah, 
            'temp_lahir' : temp_lahir, 
            'tgl_lahir' : tgl_lahir, 
            'no_telp_ortu' : no_telp_ortu, 
            'kelas' : kelas, 
            'daerah' : daerah, 
            'kecamatan' : kecamatan, 
            'alamat' : alamat, 
            'foto' : foto,
            'status' : status,
            'tgl_daftar': tgl_daftar
        }
        list_jemaat.append(data)
    return list_jemaat

# Cari jemaat dengan status
def get_absen_by_status(status):
    list_jemaat = []
    jmt = db.session.query(Jemaat.id_jemaat, Jemaat.nama, Jemaat.no_telp, Jemaat.email, Jemaat.gender, Jemaat.hobi, Jemaat.sekolah, Jemaat.temp_lahir, Jemaat.tgl_lahir, Jemaat.no_telp_ortu, Jemaat.kelas, Jemaat.daerah, Jemaat.kecamatan, Jemaat.alamat, Jemaat.foto, Jemaat.status, Jemaat.tgl_daftar).filter(Jemaat.status == status)
    for id_jemaat, nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status, tgl_daftar in jmt:
        data = {
            'id_jemaat' : id_jemaat, 
            'nama' : nama, 
            'no_telp' : no_telp, 
            'email' : email, 
            'gender' : gender, 
            'hobi' : hobi,
            'sekolah' : sekolah, 
            'temp_lahir' : temp_lahir, 
            'tgl_lahir' : tgl_lahir, 
            'no_telp_ortu' : no_telp_ortu, 
            'kelas' : kelas, 
            'daerah' : daerah, 
            'kecamatan' : kecamatan, 
            'alamat' : alamat, 
            'foto' : foto,
            'status' : status,
            'tgl_daftar':tgl_daftar
        }
        list_jemaat.append(data)
    return list_jemaat
        

# # Cari Absen Dengan Tanggal
# def get_absen_by_date(start_date, end_date):
#     # with app.app_context():
#     abs = db.session.query(Absen.id_jemaat, Jemaat.nama, Jemaat.status, Absen.waktu_absen).join(Absen,Absen.id_jemaat == Jemaat.id_jemaat).filter(Absen.waktu_absen.between(start_date,end_date)).all()
#     list_absen = []
#     for id_jemaat, nama, status, waktu_absen in abs:
#         data = {
#             "id_jemaat" : id_jemaat,
#             "nama":nama,
#             "status" : status,
#             "waktu_absen" : waktu_absen
#         }
#         list_absen.append(data)
#     return list_absen

# Cari absen dengan huruf awal
def get_absen_by_name(name):
    list_absen = []
    abs = db.session.query(Absen.id_jemaat, Jemaat.nama, Jemaat.status, Absen.waktu_absen).join(Jemaat, Jemaat.id_jemaat == Absen.id_jemaat).filter(Jemaat.nama.startswith(name)).all()
    for id_jemaat, nama, status, waktu_absen in abs:
        data = {
            "id_jemaat" : id_jemaat,
            "nama":nama,
            "status" : status,
            "waktu_absen" : waktu_absen
        }
        list_absen.append(data)

# Cari Absen Dengan ID Jemaat
# def get_absen_by_id(id_jmt):
#     # with app.app_context():
#     abs = db.session.query(Absen.id_jemaat, Jemaat.nama, Jemaat.status, Absen.waktu_absen).join(Absen,Absen.id_jemaat == Jemaat.id_jemaat).filter(Absen.id_jemaat == id_jmt).all()
#     list_absen = []
#     for id_jemaat, nama, status, waktu_absen in abs:
#         data = {
#             "id_jemaat" : id_jemaat,
#             "nama":nama,
#             "status" : status,
#             "waktu_absen" : waktu_absen
#         }
#         list_absen.append(data)
#     return list_absen
    
# Edit Data Jemaat #COBA
def edit_data_jemaat(id_jemaat, nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status):
    # with app.app_context():
    jemaat = db.session.query(Jemaat).filter(Jemaat.id_jemaat == id_jemaat).first()
    try:
        jemaat.nama = nama
        jemaat.no_telp = no_telp
        jemaat.email = email
        jemaat.gender = gender
        jemaat.hobi = hobi
        jemaat.sekolah = sekolah
        jemaat.temp_lahir = temp_lahir
        jemaat.tgl_lahir = tgl_lahir
        jemaat.no_telp_ortu = no_telp_ortu
        jemaat.kelas = kelas
        jemaat.daerah = daerah
        jemaat.kecamatan = kecamatan
        jemaat.alamat = alamat
        jemaat.foto = foto
        jemaat.status = status
        db.session.commit()

        return {
            'status':'success'
        }
    except:
        return {
            'status':'failed'
        }

#Migrate Data
def migrate_data(file_name):
    # with app.app_context():
    try:
        df = pd.read_csv(file_name)
        df = df.where(pd.notna(df), None)
        for index, row in df.iterrows():
            add_jemaat(row['NAMA LENGKAP (NAMA + NAMA BELAKANG/MARGA)'], 
                    row['NOMOR HP / WHATSAPP'], 
                    row['ALAMAT EMAIL'], 
                    row['GENDER'], 
                    row['Hobby'] if row['Hobby (Updated)']==None else row['Hobby (Updated)'], 
                    row['Nama Sekolah'], 
                    row['Tempat Lahir'], 
                    row['Tanggal Lahir'], 
                    row['NOMOR HP / WHATSAPP'], 
                    row['Kelas'], 
                    row['Tempat tinggal'], 
                    row['Kecamatan'], 
                    row['Alamat Lengkap'], 
                    None, 
                    "Active")
        return {'status':'success'}
    except:
        return {
            'status':'failed'
        }


# Cari jemaat dengan status
def get_jemaat_by_status(status):
    list_jemaat = []
    jmt = db.session.query(Jemaat.id_jemaat, Jemaat.nama, Jemaat.no_telp, Jemaat.email, Jemaat.gender, Jemaat.hobi, Jemaat.sekolah, Jemaat.temp_lahir, Jemaat.tgl_lahir, Jemaat.no_telp_ortu, Jemaat.kelas, Jemaat.daerah, Jemaat.kecamatan, Jemaat.alamat, Jemaat.foto, Jemaat.status, Jemaat.tgl_daftar).filter(Jemaat.status == status).all()
    for id_jemaat, nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status, tgl_daftar in jmt:
        data = {
            'id_jemaat' : id_jemaat, 
            'nama' : nama, 
            'no_telp' : no_telp, 
            'email' : email, 
            'gender' : gender, 
            'hobi' : hobi, 
            'sekolah' : sekolah, 
            'temp_lahir' : temp_lahir, 
            'tgl_lahir' : tgl_lahir, 
            'no_telp_ortu' : no_telp_ortu, 
            'kelas' : kelas, 
            'daerah' : daerah, 
            'kecamatan' : kecamatan, 
            'alamat' : alamat, 
            'foto' : foto,
            'status' : status,
            'tgl_daftar' : tgl_daftar
        }
        list_jemaat.append(data)
    return list_jemaat

def get_all_absen(status=None, nama=None, tanggal=None):
    query = db.session.query(Absen.id_jemaat, Jemaat.nama, Jemaat.status, Absen.waktu_absen).join(Absen, Absen.id_jemaat == Jemaat.id_jemaat)

    if status:
        # query = query.filter(Jemaat.status == status)
        if status.lower() == 'inactive':
            # Memfilter status yang tidak aktif
            query = query.filter(Jemaat.status == '-')
        else:
            query = query.filter(Jemaat.status == status)

    if nama:
        nama = nama.upper()
        query = query.filter(Jemaat.nama.ilike(f'%{nama}%'))

    if tanggal:
        wib = pytz.timezone('Asia/Jakarta')
        naive_wib_datetime = datetime.strptime(tanggal, '%Y-%m-%d').date()
        tanggal_obj = wib.localize(naive_wib_datetime)
        # Mendapatkan tanggal, bulan, dan tahun dari objek datetime
        tahun = tanggal_obj.year
        bulan = tanggal_obj.month
        hari = tanggal_obj.day
        # Memfilter berdasarkan tanggal, bulan, dan tahun
        query = query.filter(db.extract('year', Absen.waktu_absen) == tahun,
                             db.extract('month', Absen.waktu_absen) == bulan,
                             db.extract('day', Absen.waktu_absen) == hari)

    abs = query.all()

    list_absen = []
    
    for id_jemaat, nama, status, waktu_absen in abs:
        data = {
            "id_jemaat": id_jemaat,
            "nama": nama,
            "status": status,
            "waktu_absen": waktu_absen
        }
        list_absen.append(data)
        if waktu_absen.tzinfo:
            if waktu_absen.tzinfo == timezone('Asia/Jakarta'):
                print("The timestamp is in WIB (Asia/Jakarta) timezone.")
            elif waktu_absen.tzinfo == timezone('UTC'):
                print("The timestamp is in GMT (UTC) timezone.")
            else:
                print("The timestamp is in another timezone.")
        else:
            print("The timezone information is not available.")

    return list_absen
        
# Cari Absen Dengan Tanggal
def get_absen_by_date(date):
    # with app.app_context():
    abs = db.session.query(Absen.id_jemaat, Absen.waktu_absen).filter(Absen.waktu_absen == date).all()
    list_absen = []
    for id_jemaat, waktu_absen in abs:
        data = {
            "id_jemaat" : id_jemaat,
            "waktu_absen" : waktu_absen
        }
        list_absen.append(data)
    return list_absen
    
# # Cari Absen Dengan ID Jemaat
# def get_absen_by_id(id_jmt):
#     # with app.app_context():
#     abs = db.session.query(Absen.id_jemaat, Absen.waktu_absen).filter(Absen.id_jemaat == id_jmt).all()
#     list_absen = []
#     for id_jemaat, waktu_absen in abs:
#         data = {
#             "id_jemaat" : id_jemaat,
#             "waktu_absen" : waktu_absen
#         }
#         list_absen.append(data)
#     return list_absen
    
# Cari absen dengan huruf awal
# def get_absen_by_name(name):
#     list_absen = []
#     jmt = db.session.query(Absen.id_absen, Absen.waktu_absen).join(Jemaat, Jemaat.id_jemaat == Absen.id_jemaat).filter(Jemaat.nama.startswith(name)).all()
#     for id_jemaat, nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status in jmt:
#         data = {
#             'id_jemaat' : id_jemaat, 
#             'nama' : nama, 
#             'no_telp' : no_telp, 
#             'email' : email, 
#             'gender' : gender, 
#             'hobi' : hobi, 
#             'sekolah' : sekolah, 
#             'temp_lahir' : temp_lahir, 
#             'tgl_lahir' : tgl_lahir, 
#             'no_telp_ortu' : no_telp_ortu, 
#             'kelas' : kelas, 
#             'daerah' : daerah, 
#             'kecamatan' : kecamatan, 
#             'alamat' : alamat, 
#             'foto' : foto,
#             'status' : status
#         }
#         list_absen.append(data)
#     return list_absen
    
def visualize_monthly_absen(year, month):
    # list_absen = []
    wib = pytz.timezone('Asia/Jakarta')
    naive_wib_datetime = datetime.strptime(f"{year}-{month}-01", "%Y-%m-%d")
    this_month = wib.localize(naive_wib_datetime)
    # print(this_month)
    abs = db.session.query(Absen.id_absen, Absen.waktu_absen).filter(Absen.waktu_absen >= this_month).all()
    # for id_jemaat, waktu_absen in abs:
    #     data = {
    #         "id_jemaat" : id_jemaat,
    #         "waktu_absen" : waktu_absen
    #     }
    #     list_absen.append(data)
    
    weekly = get_all_sundays(year, month)
    count = [0] * len(weekly)
    for id_jemaat, waktu_absen in abs:
        for i in range(len(weekly)):
            print(waktu_absen,weekly[i])
            if waktu_absen <= weekly[i]:
                count[i]+=1
                break
    print(count)
    data = {
            "jumlah" : count,
            "minggu" : weekly
        }
    return data

def get_all_sundays(year, month):
    year = int(year)
    month = int(month)
    weekday, days_in_month = calendar.monthrange(year, month)

    # Calculate offsets to reach all Sundays (considering wrapping)
    offsets = range((6 - weekday) % 7 + 1, days_in_month + 1, 7)

    # Create a list of datetime objects for all Sundays with time set to 23:59:59
    all_sundays = [datetime(year, month, day, 23, 59, 59) for day in offsets]

    return all_sundays

def get_birthday():
    list_jemaat = []
    wib = pytz.timezone('Asia/Jakarta')
    utc_now = datetime.now(pytz.utc)
    today = utc_now.astimezone(wib).replace(hour=23, minute=59, second=59, microsecond=999999)
    abs = db.session.query(Jemaat.id_jemaat, Jemaat.nama, Jemaat.tgl_lahir).filter(Jemaat.status == 'active').all()
    print(abs)
    if abs == None:
        # print('type after:',type(Jemaat.tgl_lahir))
        return {'status' : 'failed'}
    last_week = today - timedelta(days=7)
    try:
        for id,nama,tgl in abs:
            print(nama)
            print('Masuk 1')
            print(tgl)
            if tgl.month == today.month:
                print('Masuk 2')
                print(tgl.day, last_week.day, tgl.day, today.day)
                if tgl.day >= last_week.day and tgl.day <= today.day:
                    print('Masuk 3')
                    data = {
                        'id': id,
                        'nama': nama,
                        'tanggal': tgl,
                        'status' : 'success'
                    }
                    list_jemaat.append(data)
    except:
        pass
    return list_jemaat

def get_all_jemaat():
    list_jemaat = []
    jemaat = db.session.query(Jemaat.id_jemaat, Jemaat.nama, Jemaat.no_telp, Jemaat.email, Jemaat.gender, Jemaat.hobi, Jemaat.sekolah, Jemaat.temp_lahir, Jemaat.tgl_lahir, Jemaat.no_telp_ortu, Jemaat.kelas, Jemaat.daerah, Jemaat.kecamatan, Jemaat.alamat, Jemaat.foto, Jemaat.status, Jemaat.tgl_daftar).all()
    for id_jemaat, nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status, tgl_daftar in jemaat:
        data = {
            'id_jemaat' : id_jemaat, 
            'nama' : nama, 
            'no_telp' : no_telp, 
            'email' : email, 
            'gender' : gender, 
            'hobi' : hobi, 
            'sekolah' : sekolah, 
            'temp_lahir' : temp_lahir, 
            'tgl_lahir' : tgl_lahir, 
            'no_telp_ortu' : no_telp_ortu, 
            'kelas' : kelas, 
            'daerah' : daerah, 
            'kecamatan' : kecamatan, 
            'alamat' : alamat, 
            'foto' : foto,
            'status' : status,
            'tgl_daftar' : tgl_daftar
        }
        list_jemaat.append(data)
    return list_jemaat

# def get_all_active_jemaat():
#     all_active_jemaat = []
#     jemaat = db.session.query(Jemaat.id_jemaat, Jemaat.nama).filter(Jemaat.status == 'active').all()
#     for id,nama in jemaat:
#         data = {
#             'id':id,
#             'nama':nama
#         }
#         all_active_jemaat.append(data)
#     return all_active_jemaat

def get_all_absent_today():
    wib = pytz.timezone('Asia/Jakarta')
    absen_jemaat = []
    utc_now = datetime.now(pytz.utc)
    today = utc_now.astimezone(wib).replace(hour=0, minute=0, second=0, microsecond=0)
    abs = db.session.query(Jemaat.id_jemaat, Jemaat.nama, Absen.waktu_absen).join(Absen,Absen.id_jemaat == Jemaat.id_jemaat).filter(Jemaat.status == 'active').filter(Absen.waktu_absen >= today).all()
    for id, nama, waktu in abs:
        data = {
            'id':id,
            'nama':nama,
            'waktu_absen':waktu
        }
        absen_jemaat.append(data)
    return absen_jemaat

def get_attendance():
    count_active_jemaat = len(get_jemaat_by_status('active'))
    absen_jemaat_today = len(get_all_absent_today())
    absent = count_active_jemaat - absen_jemaat_today
    data = {
        'attended' : absen_jemaat_today,
        'absent' : absent
    }
    return data

def add_academic_year():
    jemaats = db.session.query(Jemaat).filter(Jemaat.status == 'active').all()
    for jemaat in jemaats:
        jemaat.kelas += 1
        if jemaat.kelas > 12:
            jemaat.status = 'inactive'
    db.session.commit()
    return {'status':'success'}

def get_new_commers():
    new_commers = []
    wib = pytz.timezone('Asia/Jakarta')
    utc_now = datetime.now(pytz.utc)
    today = utc_now.astimezone(wib).replace(hour=0, minute=0, second=0, microsecond=0)
    jemaats = db.session.query(Jemaat.id_jemaat,Jemaat.nama,Jemaat.tgl_daftar).filter(Jemaat.status == 'active').filter(Jemaat.tgl_daftar >= today).all()
    for id, nama, tanggal in jemaats:
        data = {
            'id':id,
            'nama':nama,
            'tanggal':tanggal
        }
        new_commers.append(data)
    return new_commers

def get_absent_more_three():
    absent = []
    wib = pytz.timezone('Asia/Jakarta')
    today_utc = datetime.today()
    today = wib.localize(today_utc)
    three_weeks_ago = today - timedelta(weeks=3)
    print(three_weeks_ago)
    three_weeks_ago_start_of_day = three_weeks_ago.replace(hour=0, minute=0, second=0, microsecond=0)
    jemaats = db.session.query(Jemaat.id_jemaat,Jemaat.nama,Absen.waktu_absen).join(Absen,Absen.id_jemaat == Jemaat.id_jemaat).filter(Absen.waktu_absen < three_weeks_ago_start_of_day).filter(Jemaat.status == 'active').all()
    latest_absen = {}

    # Iterate over the results and update the dictionary with the latest waktu_absen for each id_jemaat
    for id_jemaat, nama, waktu_absen in jemaats:
        if id_jemaat not in latest_absen or waktu_absen > latest_absen[id_jemaat]:
            latest_absen[id_jemaat] = waktu_absen

    # Filter the results to include only the rows with the latest waktu_absen for each id_jemaat
    filtered_jemaats = [(id_jemaat, nama, waktu_absen) for id_jemaat, nama, waktu_absen in jemaats if waktu_absen == latest_absen[id_jemaat]]

    # Print the filtered results
    for id_jemaat, nama, waktu_absen in filtered_jemaats:
        data = {
            'id':id_jemaat,
            'nama':nama,
            'waktu_absen':waktu_absen
        }
        absent.append(data)
    return absent
# Test
# print(get_all_jemaat())
# print(initiate_table()) #Success
# file_name = "Data_remaja_aug_2022.csv"
# print(migrate_data(file_name)) #Success
# print(get_all_jemaat())
# print(login_admin("Patrick","123")) #Success
# print(login_admin("Feodor","123")) #Success
# print(get_all_jemaat()) #Success
# print(get_jemaat_by_id(1)) #Success
# print(get_all_absen()) #Success
# print(get_absen_by_tanggal(datetime(2023, 7, 11))) #Success
# print(get_absen_by_id(1)) #Success
# edit_data_jemaat