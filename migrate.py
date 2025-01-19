from datetime import datetime
from pytz import timezone
from backend.models import Jemaat
from backend.rmj_db import *
import pandas as pd
# from backend.rmj_db import engine
from sqlalchemy import create_engine,inspect
from sqlalchemy.orm import sessionmaker
# Read data from the Excel file
csv_file_path = 'data_remaja_edited.csv'  # replace with your file path
df = pd.read_csv(csv_file_path)

# print(df)
# df.columns = ['nama', 'nomor', 'email', 'gender', 'hobi', 'sekolah', 'kelas', 
#               'tempat_lahir', 'tgl_lahir', 'daerah','no_telp_ortu', 'kecamatan', 'alamat']
# df = df[df['email'] != '-']
# df["tgl_lahir"] = pd.to_datetime(df["tgl_lahir"], errors="coerce", dayfirst=True)

DATABASE_URI = 'mysql://root@localhost:3306/rmj_db'  # replace with your credentials
engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()


# # Define your Jemaat model
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, DateTime

# Base = declarative_base()
# # Create the table in the database
# Base.metadata.create_all(engine)

def reset_and_populate_jemaat_table(csv_file_path):
    """
    Fungsi untuk reset tabel jemaat (drop jika ada, buat ulang) 
    dan mengisi data dari file CSV ke tabel di database rmj_db.
    """
    # Baca data dari file CSV
    df = pd.read_csv(csv_file_path)
    print(df)

    # Ubah nama kolom agar sesuai dengan model Jemaat
    df.columns = ['nama', 'no_telp', 'email', 'gender', 'hobi', 'sekolah', 'kelas', 
              'temp_lahir', 'tgl_lahir', 'daerah','no_telp_ortu', 'kecamatan', 'alamat']

    # Perbaiki data yang hilang atau salah
    df = df[df['email'] != '-']  # Hapus data dengan email tidak valid
    df['tgl_lahir'] = pd.to_datetime(df['tgl_lahir'], errors='coerce', dayfirst=True)


    # Periksa apakah tabel sudah ada
    inspector = inspect(engine)
    if 'jemaat' in inspector.get_table_names():
        print("Tabel 'jemaat' ditemukan, akan dihapus...")
        Jemaat.__table__.drop(engine)
        print("Tabel 'jemaat' berhasil dihapus.")

    # Buat tabel baru
    print("Membuat tabel 'jemaat'...")
    Jemaat.__table__.create(engine)
    print("Tabel 'jemaat' berhasil dibuat.")

    # Masukkan data dari DataFrame ke tabel
    print("Memasukkan data dari CSV ke tabel 'jemaat'...")
    records = df.to_dict(orient='records')  # Konversi DataFrame ke daftar dictionary
    session.bulk_insert_mappings(Jemaat, records)
    session.commit()
    print("Data berhasil dimasukkan ke tabel 'jemaat'.")


if __name__ == "__main__":
    csv_file_path = 'data_remaja_edited.csv'  # Ganti sesuai dengan path file CSV Anda
    reset_and_populate_jemaat_table(csv_file_path)