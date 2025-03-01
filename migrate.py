from datetime import datetime
from pytz import timezone
from backend.models import Jemaat
from backend.rmj_db import *
from main import app 
import pandas as pd
# from backend.rmj_db import engine
from sqlalchemy import create_engine,inspect
from sqlalchemy.orm import sessionmaker
# Read data from the Excel file
csv_file_path = 'data-students.xlsx'  # replace with your file path
df = pd.read_excel(csv_file_path)
# df.columns = ['id_jemaat','nama', 'no_telp', 'email', 'gender', 'hobi', 'sekolah', 
#               'temp_lahir', 'tgl_lahir','foto','no_telp_ortu','kelas','daerah', 'kecamatan', 'alamat','status','terakhir_hadir']

print(df['tgl_lahir'])
print('INI NAMA', df['no_telp'])

DATABASE_URI = 'mysql://root@localhost:3306/rmj_db' 
engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()



def create_new_database(path):
    ordered_columns = [
    'nama', 'no_telp', 'email', 'gender', 'hobi', 'sekolah', 
    'temp_lahir', 'tgl_lahir', 'no_telp_ortu', 'kelas', 'daerah', 
    'kecamatan', 'alamat', 'foto', 'status','tgl_daftar','terakhir_hadir'
    ]

    df_file = pd.read_excel(path)
    for _, row in df_file.iterrows():
        data = {col: row[col] for col in ordered_columns}
        
    inspector = inspect(engine)
    if 'jemaat' in inspector.get_table_names():
        print("Tabel 'jemaat' ditemukan, akan dihapus...")
        Jemaat.__table__.drop(engine)
        print("Tabel 'jemaat' berhasil dihapus.")
        
        print("Membuat tabel 'jemaat'...")
        
    Jemaat.__table__.create(engine)
    print("Tabel 'jemaat' berhasil dibuat.")
    # print(df['tgl_lahir'])
    # Masukkan data dari DataFrame ke tabel
    print("Memasukkan data dari CSV ke tabel 'jemaat'...")
    records = df.to_dict(orient='records')  # Konversi DataFrame ke daftar dictionary
    session.bulk_insert_mappings(Jemaat, records)
    session.commit()
    print("Data berhasil dimasukkan ke tabel 'jemaat'.")
        
        
if __name__ == "__main__":
    with app.app_context():
        # csv_file_path = 'data-students.xlsx'  # Ganti sesuai dengan path file CSV Anda
        print(df['terakhir_hadir'].dtypes)
        create_new_database(csv_file_path)
        # for _, row in df.iterrows():
        #         # Konversi baris ke dictionary
        #         data = {col: row[col] for col in ordered_columns}
        #         # data['terakhir_hadir'] = data['terakhir_hadir'].dt.tz_convert('UTC')
        #         # if isinstance(data['terakhir_hadir']):
        #         #     data['terakhir_hadir'] = pd.to_datetime(data['terakhir_hadir'], errors='coerce').d
        #         if data['terakhir_hadir'].tz is None:
        #             data['terakhir_hadir'] = data['terakhir_hadir'].tz_localize('Asia/Jakarta')

        #         # Konversi ke UTC
        #         data['terakhir_hadir'] = data['terakhir_hadir'].tz_convert('UTC')
        #         print(data['terakhir_hadir'])
        #         add_jemaat(**data)
                
                
            
    # reset_and_populate_jemaat_table(csv_file_path)
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def reset_and_populate_jemaat_table(csv_file_path):
#     """
#     Fungsi untuk reset tabel jemaat (drop jika ada, buat ulang) 
#     dan mengisi data dari file CSV ke tabel di database rmj_db.
#     """
#     # Baca data dari file CSV
#     df = pd.read_excel(csv_file_path)
#     print(df)
#     # Ubah nama kolom agar sesuai dengan model Jemaat

#     df.columns = ['id_jemaat','nama', 'no_telp', 'email', 'gender', 'hobi', 'sekolah', 
#               'temp_lahir', 'tgl_lahir','foto','no_telp_ortu','kelas','daerah', 'kecamatan', 'alamat','status','terakhir_hadir']
    
#     # (nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status
#     print('ini isi tgl lahir')
#     print(df['tgl_lahir'])

#     invalid_tgl_lahir = df[df['tgl_lahir'].isna()]
#     print('invalid', invalid_tgl_lahir)

# # Tampilkan entri yang tidak valid
#     # Perbaiki data yang hilang atau salah
#     # df['foto'] = ''
#     # df['status'] = 'active'
#     # df['gender'] = df['gender'].replace({'Laki-laki': 'L', 'Perempuan': 'P'})
#     # df['nama'] = df['nama'].str.upper()
#     # df = df[df['email'] != '-']  # Hapus data dengan email tidak valid
#     # df = df[df['tgl_lahir'] != '-'] 
#     # df = df[df['kelas'] != '-'] 
#     # df['tgl_lahir'] = pd.to_datetime(df['tgl_lahir'], errors='coerce',dayfirst=True)
#     # print('ini isi tgl lahir2',df['tgl_lahir'])
    
#     # print("Baris dengan tgl_lahir yang tidak valid:")
#     # print(invalid_tgl_lahir)
     
#     # df['tgl_lahir'] = pd.to_datetime(df['tgl_lahir'], format='%a, %d %b %Y %H:%M:%S %Z', errors='coerce')

 
#     # Periksa apakah tabel sudah ada
#     inspector = inspect(engine)
#     if 'jemaat' in inspector.get_table_names():
#         print("Tabel 'jemaat' ditemukan, akan dihapus...")
#         Jemaat.__table__.drop(engine)
#         print("Tabel 'jemaat' berhasil dihapus.")

#     # Buat tabel baru
#     print("Membuat tabel 'jemaat'...")
#     Jemaat.__table__.create(engine)
#     print("Tabel 'jemaat' berhasil dibuat.")
#     # print(df['tgl_lahir'])
#     # Masukkan data dari DataFrame ke tabel
#     print("Memasukkan data dari CSV ke tabel 'jemaat'...")
#     records = df.to_dict(orient='records')  # Konversi DataFrame ke daftar dictionary
#     session.bulk_insert_mappings(Jemaat, records)
#     session.commit()
#     print("Data berhasil dimasukkan ke tabel 'jemaat'.")