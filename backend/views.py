from flask import Blueprint, request, jsonify, flash
from .rmj_db import *
from sqlalchemy import delete
from sqlalchemy import extract

views = Blueprint('views', __name__)

@views.route('/',methods=['GET'])
def halo():
    return '<h1>halo</h1>'

@views.route('/all-absent',methods=['POST','GET'])
def all_absen():
    return jsonify(get_all_absen())

@views.route('/init_table',methods=['POST','GET'])
def init_table():
    return jsonify(initiate_table())

@views.route('/filter-date-absent',methods=['POST','GET'])
def get_date_absen():
    if request.method == 'POST':
        data = request.get_json()
        date  = data['date']
    return jsonify(get_absen_by_date(date))

@views.route('/filter-name-absent',methods=['POST','GET'])
def get_name_absen():
    if request.method == 'POST':
        data = request.get_json()
        name  = data['name']
    return jsonify(get_absen_by_name(name))

@views.route('/filter-status-absent',methods=['POST','GET'])
def get_status_absen():
    if request.method == 'POST':
        data = request.get_json()
        status  = data['status'] #String [Active,Inactive]
    return jsonify(get_absen_by_status(status))

@views.route('/filter-absent-data', methods=['GET'])
def filter_absent_data():
    status = request.args.get('status')
    nama = request.args.get('nama')
    tanggal = request.args.get('tanggal')
    return jsonify(get_all_absen(status, nama, tanggal))

@views.route('/edit-data-jemaat',methods=['POST','GET'])
def edit_status_jemaat():
    if request.method == 'POST':
        data = request.get_json()
        id_jemaat  = data['id_jemaat']
        nama  = data['nama']
        no_telp  = data['no_telp']
        email  = data['email']
        gender  = data['gender']
        hobi  = data['hobi']
        sekolah  = data['sekolah']
        temp_lahir  = data['temp_lahir']
        tgl_lahir  = data['tgl_lahir']
        no_telp_ortu  = data['no_telp_ortu']
        kelas  = data['kelas']
        daerah  = data['daerah']
        kecamatan  = data['kecamatan']
        alamat  = data['alamat']
        foto  = data['foto']
        status  = data['status'] #String [Active,Inactive]
    return jsonify(edit_data_jemaat(id_jemaat, nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status))

@views.route('/student/recommendations', methods=['GET'])
def get_recommendations():
    data = get_all_jemaat()
    print(data)
    selected_keys = ['nama', 'id_jemaat']
    result_list = [{key: user[key] for key in selected_keys} for user in data]
    return jsonify(result_list)

@views.route('/all-students', methods=['GET'])
def get_all_students():
    data = get_all_jemaat()
    print(data)
    selected_keys = ['id_jemaat' , 
            'nama', 
            'no_telp', 
            'email', 
            'gender', 
            'hobi', 
            'sekolah', 
            'temp_lahir', 
            'tgl_lahir', 
            'no_telp_ortu', 
            'kelas' ,
            'daerah' , 
            'kecamatan', 
            'alamat' , 
            'foto' ,
            'status']
    result_list = [{key: user[key] for key in selected_keys} for user in data]
    return jsonify(result_list)

@views.route('/delete-jemaat', methods=['DELETE'])
def delete_jemaat():
    try:
        # Get the id_jemaat from the request parameters
        id_jemaat = request.args.get('id_jemaat')
        if id_jemaat is None:
            return jsonify({'message': 'id_jemaat parameter is required'})

        # Call the delete_jemaat_by_id function to delete the Jemaat record
        message = delete_jemaat_by_id(id_jemaat)

        return jsonify({'message': message})
    except Exception as e:
        return jsonify({'message': str(e)})
    
@views.route('/monthly-absent', methods=['POST'])
def monthly_absent():
    if request.method == 'POST':
        data = request.get_json()
        year = data['year']
        month = data['month']
    # date = "2024-05-01"
    return jsonify(visualize_monthly_absen(year,month))

@views.route('/weekly-birthday', methods=['POST']) # aku ubah
def weekly_birthday():
    if request.method == 'POST':
        data = request.get_json()
        weeks_before = data['weeks_before']
    return jsonify(get_birthday(weeks_before))

@views.route('/today-attendance', methods=['POST'])
def today_attendance():
    return jsonify(get_attendance())

@views.route('/academic-year', methods=['POST'])
def academic_year():
    return jsonify(add_academic_year())

@views.route('/new-commers', methods=['POST']) # aku ubah
def new_commers():
    if request.method == 'POST':
        data = request.get_json()
        weeks_before = data['weeks_before']
    return jsonify(get_new_commers(weeks_before))

@views.route('/long-absent', methods=['POST']) # aku ubah
def long_absent():
    if request.method == 'POST': 
        data = request.get_json()
        weeks_before = data['weeks_before']
    return jsonify(get_long_absent(weeks_before))

@views.route('/student-migrate',methods=['POST','GET'])
def migrate_students():
    print('MASUK 1')
    return jsonify(migrate_student())