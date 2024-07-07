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
                    <input type="tel" id="phone" class="form-control" v-model="formData.no_telp" pattern="[0-9]{10,15}"
                        required>
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
                        <input class="form-check-input" type="radio" id="laki-laki" value="L" v-model="formData.gender"
                            required>
                        <label class="form-check-label" for="male">Laki-laki</label>
                    </div>
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" id="perempuan" value="P" v-model="formData.gender"
                            required>
                        <label class="form-check-label" for="female">Perempuan</label>
                    </div>
                </div>
                <div class="form-group">
                    <label for="birthdate">Tanggal Lahir:</label>
                    <input type="date" id="birthdate" class="form-control" v-model="formData.tgl_lahir" required>
                </div>
                <div class="form-group">
                    <label for="nama">Alamat</label>
                    <input type="text" id="name" class="form-control" v-model="formData.alamat" required>
                </div>

                <div class="form-group">
                    <label for="daerah">Daerah</label>
                    <select id="daerah" class="form-control" v-model="formData.daerah" @change="handleDaerahChange">
                        <option v-for="option in daerahOptions" :key="option" :value="option">
                            {{ option }}
                        </option>
                        <option value="custom">Input Custom Daerah</option>
                    </select>
                    <input v-if="showCustomDaerahInput" type="text" class="form-control" v-model="customDaerah"
                        @input="handleCustomDaerahInput" placeholder="Enter custom daerah">
                </div>

                <div class="form-group">
        
                    <label for="kecamatan">Kecamatan</label>
                    <select id="kecamatan" class="form-control" v-model="formData.kecamatan"
                        @change="handleSearchKecamatan">
                        <option v-for="option in kecamatanOptions" :key="option" :value="option">
                            {{ option }}
                        </option>
                        <option value="custom">Input Custom Kecamatan</option>
                    </select>
                    <input v-if="showCustomKecamatan" type="text" class="form-control" v-model="customKecamatan"
                        @input="updateKecamatan" placeholder="Enter kecamatan">
                </div>


                <div class="form-group">
                    <label for="nama">No.Telp Orangtua</label>
                    <input type="tel" id="name" class="form-control" v-model="formData.no_telp_ortu"
                        pattern="[0-9]{10,15}" required>
                </div>
                <button type="submit" class="btn btn-class">Register</button>
                <button type="button" class="btn btn-secondary" @click="closeForm">Tutup</button>
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
                tgl_lahir: 'none',
                temp_lahir: '',
                no_telp_ortu: '',
                kelas: null,
                daerah: '',
                kecamatan: '',
                alamat: '',
                foto: "nanana",
                status: "active"
            },
            daerahOptions: [],
            customDaerah: '',
            showCustomDaerahInput: false,
            kecamatanOptions: [],
            customKecamatan: '',
            showCustomKecamatan: false
        };
    },
    mounted() {
        this.fetchDaerahOptions();
        this.fetchKecamatanOptions();
    },
    methods: {
        async fetchDaerahOptions() {
            try {
                const response = await axios.get('absen/get-daerah');
                this.daerahOptions = response.data;
            } catch (error) {
                console.error('Error fetching daerah options:', error);
            }
        },
        async fetchKecamatanOptions() {
            try {
                const response = await axios.get('absen/get-kecamatan');
                this.kecamatanOptions = response.data;
            } catch (error) {
                console.error('Error fetching kecamatan options:', error);
            }
        },
        updateKecamatan(selected) {
            // if (selected && selected.name) {
            //     this.formData.kecamatan = selected.name;
            //     this.isCustomKecamatan = false;
            // } else {
            //     this.formData.kecamatan = selected.toUpperCase();
            //     this.isCustomKecamatan = true;
            // }
            this.customKecamatan = selected.target.value.toUpperCase();
            this.formData.kecamatan= this.customKecamatan;
        },
        handleSearchKecamatan(search) {
            const selectedValue = search.target.value;
            if (selectedValue === 'custom') {
                this.showCustomKecamatan = true;
                this.formData.kecamatan = '';
            } else {
                this.showCustomKecamatan = false;
                this.formData.kecamatan = selectedValue;
            }
        },
        // toUpperCaseKecamatan() {
        //     this.formData.kecamatan = this.formData.kecamatan.toUpperCase();
        // },

        handleDaerahChange(event) {
            const selectedValue = event.target.value;
            if (selectedValue === 'custom') {
                this.showCustomDaerah = true;
                this.formData.daerah = '';
            } else {
                this.showCustomDaerah = false;
                this.formData.daerah = selectedValue;
            }
        },
        addCustomDaerah() {
            if (this.customDaerah && !this.daerahOptions.includes(this.customDaerah)) {
                this.daerahOptions.push(this.customDaerah);
                this.formData.daerah = this.customDaerah;
                this.showCustomDaerahInput = false;
            }
        },
        handleCustomDaerahInput(event) {
            this.customDaerah = event.target.value.toUpperCase();
            this.formData.daerah = this.customDaerah;
        },
        async registerStudent() {
            try {
                const res = await axios.post('absen/student/create', {
                    nama: this.formData.nama,
                    no_telp: String(this.formData.no_telp),
                    email: this.formData.email,
                    gender: this.formData.gender,
                    hobi: this.formData.hobi,
                    sekolah: this.formData.sekolah,
                    temp_lahir: this.formData.temp_lahir,
                    tgl_lahir: this.formData.tgl_lahir,
                    no_telp_ortu: String(this.formData.no_telp_ortu),
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
            },
                this.selectedDaerah = '';
            this.selectedKecamatan = '';
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
