<template>
        <div class="form-container">
            <h1 style="text-align: center;"> Registration</h1>
            <div class="form-group">
                <form @submit.prevent="registerStudent">
                    <div class="form-group">
                        <label for="nama">Nama</label>
                        <input type="text" id="nama" class="form-control" v-model="formData.nama" required>
                    </div>
                    <div class="form-group">
                        <label for="phone">Nomor Telepon</label>
                        <input type="text" id="phone" class="form-control" v-model="formData.no_telp" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" id="email" class="form-control" v-model="formData.email" required>
                    </div>
                    <div class="form-group">
                        <label for="hobby">Hobi</label>
                        <input type="text" class="form-control" v-model="formData.hobi" required>
                    </div>
                    <div class="form-group">
                        <label for="school">Nama Sekolah</label>
                        <input type="text" class="form-control" v-model="formData.sekolah" required>
                    </div>
                    <div class="form-group">
                        <label for="grades">Kelas</label>
                        <input type="number" class="form-control" v-model="formData.kelas" required>
                    </div>
                    <div class="form-group">
                        <label for="gender">Jenis Kelamin</label><br>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" id="laki-laki" value="laki-laki"
                                v-model="formData.gender" required>
                            <label class="form-check-label" for="male">Laki-laki</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" id="perempuan" value="perempuan"
                                v-model="formData.gender" required>
                            <label class="form-check-label" for="female">Perempuan</label>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="birthdate">Tanggal Lahir:</label>
                        <input type="date" id="birthdate" class="form-control" v-model="formData.tgl_lahir" required>
                    </div>
                    <div class="form-group">
                        <label for="nama">Tempat Lahir</label>
                        <input type="text" id="name" class="form-control" v-model="formData.temp_lahir" required>
                    </div>
                    <div class="form-group">
                        <label for="nama">Alamat Lahir</label>
                        <input type="text" id="name" class="form-control" v-model="formData.alamat" required>
                    </div>
                    <div class="form-group">
                        <label for="nama">Daerah</label>
                        <input type="text" id="name" class="form-control" v-model="formData.daerah" required>
                    </div>
                    <div class="form-group">
                        <label for="nama">Kecamaatan</label>
                        <input type="text" id="name" class="form-control" v-model="formData.kecamatan" required>
                    </div>
                    <div class="form-group">
                        <label for="nama">No.Telp Orangtua</label>
                        <input type="text" id="name" class="form-control" v-model="formData.no_telp_ortu" required>
                    </div>
                    <button type="submit" class="btn btn-class">Register</button>
                    <button type="button" class="btn btn-secondary" @click="closeForm">Tutup</button>
                    <!-- <button @click="closeForm">Tutup</button> -->
                </form>
            </div>
        </div>
    <!-- </div> -->
</template>

<script>
import axios from 'axios';
export default {
    name: 'StudentSignUp',
    props: {
        isVisible: {
            type: Boolean,
            required: true
        }
    },
    data() {
        return {
            formData: {
                nama: '',
                email: '',
                no_telp: '',
                gender: '',
                hobi: '',
                sekolah: '',
                tgl_lahir: '',
                temp_lahir: '',
                no_telp_ortu: '',
                kelas: null,
                daerah: '',
                kecamatan: '',
                alamat: '',
                foto: "nanana",
                status: "active"
            }
        };
    },
    methods: {
        async registerStudent() {
            try {
                const res = await axios.post('http://127.0.0.1:5000/student/create', {
                    nama: this.formData.nama,
                    no_telp: this.formData.no_telp,
                    email: this.formData.email,
                    gender: this.formData.gender,
                    hobi: this.formData.hobi,
                    sekolah: this.formData.sekolah,
                    temp_lahir: this.formData.temp_lahir,
                    tgl_lahir: this.formData.tgl_lahir,
                    no_telp_ortu: this.formData.no_telp_ortu,
                    kelas: this.formData.kelas,
                    daerah: this.formData.daerah,
                    kecamatan: this.formData.kecamatan,
                    alamat: this.formData.alamat,
                    foto: this.formData.foto,
                    status: this.formData.status// Set status to 'active' by default
                });
                console.log('Response:', res.data);
                console.log('success masuk')
                this.closeForm();

            } catch (error) {
                console.error('Error submitting form:', error);
            }
        },

        closeForm() {
            this.$router.push('/')
            this.formData = {
                nama: '',
                no_telp: '',
                email: '',
                gender: '',
                hobi: '',
                sekolah: '',
                temp_lahir: '',
                tgl_lahir: '',
                no_telp_ortu: '',
                kelas: '',
                daerah: '',
                kecamatan: '',
                alamat: '',
                foto: '',
                status: ''
            }
        },
    }
};
</script>
<style>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");


.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}


.form-container {
    background-color: white;
    max-height: 500px;
    max-width: 80%;
    padding: 50px;
    border-radius: 5px;
    overflow: auto;
    margin: auto;
    margin-top: 7%;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.form-group {
    margin-bottom: 50px;
}

/* Customize radio buttons */
.form-check-input {
    left: 20px;
}
</style>
