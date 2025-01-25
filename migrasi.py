import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from pytz import timezone
from models import Jemaat
# Read data from the Excel file
excel_file_path = 'data_remaja.xlsx'  # replace with your file path
df = pd.read_excel(excel_file_path)

# Ensure the column names match your database model
df.columns = ['nama', 'no_telp', 'email', 'gender', 'hobi', 'sekolah',
              'temp_lahir', 'tgl_lahir', 'kelas','daerah', 'kecamatan', 'alamat']

# Convert date columns to datetime objects
df['tgl_lahir'] = pd.to_datetime(df['tgl_lahir'])

# Connect to your MySQL database using SQLAlchemy
DATABASE_URI = 'mysql://root@localhost:3306/rmj_db'  # replace with your credentials
engine = create_engine(DATABASE_URI)

# Define your Jemaat model
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

# class Jemaat(Base):
#     __tablename__ = 'jemaat'
#     id_jemaat = Column('id_jemaat', Integer, primary_key=True)
#     nama = Column('nama_jemaat', String(100))
#     no_telp = Column('no_telp', String(100))
#     email = Column('email', String(100), unique=True)
#     gender = Column('gender', String(1))
#     hobi = Column('hobi', String(100))
#     sekolah = Column('nama_sekolah', String(100))
#     temp_lahir = Column('tempat_lahir', String(100))
#     tgl_lahir = Column('tanggal_lahir', DateTime)
#     no_telp_ortu = Column('no_telp_ortu', String(100))
#     kelas = Column('kelas', Integer)
#     daerah = Column('daerah', String(100))
#     kecamatan = Column('kecamatan', String(100))
#     alamat = Column('alamat_lengkap', String(100))
#     foto = Column('foto_jemaat', String(100))
#     status = Column('status', String(100))
#     tgl_daftar = Column('tanggal_daftar', DateTime(timezone=True))

# Create the table in the database
Base.metadata.create_all(engine)

# Insert data into the database
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

for index, row in df.iterrows():
    jemaat = Jemaat(
        nama=row['nama'],
        no_telp=row['nomor'],
        email=row['email'],
        gender=row['gender'],
        hobi=row['hobi'],
        sekolah=row['sekolah'],
        temp_lahir=row['tempat_lahir'],
        tgl_lahir=row['tgl_lahir'],
        no_telp_ortu='',  # or replace with actual column if available
        kelas=row['kelas'],
        daerah=row['daerah'],
        kecamatan=row['kecamatan'],
        alamat=row['alamat'],
        foto='',  # replace with actual column if available
        status='',  # replace with actual column if available
        tgl_daftar=datetime.now(timezone('Asia/Jakarta'))
    )
    session.add(jemaat)

# Commit the session
session.commit()

# Close the session
session.close()