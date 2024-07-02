<template>
    <HeaderBefore></HeaderBefore>
    <div class="absen-container">
        <div class="absen-contain">
            <div class="absen-catalogue" id="absen-cards">
                <h2>Absensi</h2>
                <br>
                <form v-on:submit.prevent="loginStudent">
                    <div class="absen-form-group">
                        <h5>Nama Lengkap</h5>
                        <SearchAutocomplete :items=recommendations @itemselected="onItemSelected" />
                    </div>

                    <div class="absen-content" id="terdaftar">
                        <div class="pendaftaran">
                            Belum terdaftar? <router-link to="/login">Daftar di sini</router-link>
                        </div>
                        <div class="absen-submit-button">
                            <button id='' class="btn-submit">
                                Submit
                            </button>
                        </div>
                    </div>
                </form>
            </div>
            <div class="pop-log" v-if="showPopLog">
                Login Berhasil
            </div>
        </div>
    </div>
</template>
<script>
import SearchAutocomplete from '@/components/SearchAutocomplete.vue'
import axios from 'axios';
import HeaderBefore from '@/components/HeaderBefore.vue';

export default {
    name: 'HomeView',
    components: {
        HeaderBefore, SearchAutocomplete,
    },
    data() {
        return {
            inpText: '',
            selectedId: null,
            recommendations: [], // Array of usernames from your JSON
            showAutocomplete: true,
            autocomplete: 'off',
            showPopLog: false, 
        };
    },
    mounted() {
        this.fetchRecommendations();
    },
    methods: {
        async fetchRecommendations() {
            try {
                const response = await axios.get('absen/student/recommendations');
                this.recommendations = response.data;
            } catch (error) {
                console.error('Error fetching data', error);
            }
        },
        loginStudent() {
            console.log(this.selectedId)
            if (this.selectedId !== null) {
                axios.post('absen/student/login', { id_jemaat: this.selectedId })
                    .then(response => {
                        // Handle the response as needed
                        this.showPopLog = true;
                        console.log(this.selectedId)
                        console.log(response.data)
                        // alert(response.data.status)
                    })
                    .catch(error => {
                        console.error('Error submitting form', error);
                    });
                this.selectedId = null;
            } else {
                alert('not selected!')
            }
        },
        onItemSelected(id) {
            this.selectedId = id;
            console.log('update')
        },
        navigateToAdmin() {
            this.$router.push('/admin-view')
        }
    },
};

</script>
<style>
.absen-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f5f5f5;
}

.absen-contain {
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    padding: 50px;
    width: 100%;
    max-width: 600px;
}

.absen-catalogue h2 {
    color: #333;
}

.absen-form-group h5 {
    color: #555;
}

.absen-content {
    margin-top: 20px;
}

.pendaftaran {
    margin-bottom: 15px;
    color: #777;
}

.pendaftaran a {
    color: #007bff;
    text-decoration: none;
}

.pendaftaran a:hover {
    text-decoration: underline;
}

.btn-submit {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
}

.btn-submit:hover {
    background-color: #0056b3;
}

.pop-log {
    position: fixed;
    top: 50%; /* Vertically center */
    left: 50%; /* Horizontally center */
    transform: translate(-100%); /* Center itself */
    background: white;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    padding: 20px;
    z-index: 1000; /* Ensure it's on top of other content */
    display: none; /* Initially hide */
}

.pop-log.show {
    display:block; 
}
</style>