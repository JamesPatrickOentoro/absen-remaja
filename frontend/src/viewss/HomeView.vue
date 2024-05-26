<template>
    <HeaderBefore></HeaderBefore>
    <div class="container">
        <div class="row content justify-content-md-center">
            <div class="col-md-6">
                <img src="@/assets/Hari reformasi_.png" />
            </div>
            <div class="col-md-5" id="cards">
                <h2>Absensi</h2>
                <br>
                <form v-on:submit.prevent="loginStudent">
                    <div class="form-group">
                        <h5>Nama Lengkap</h5>
                        <SearchAutocomplete :items=recommendations @itemselected="onItemSelected" />
                    </div>

                    <div class="row" id="terdaftar">
                        <div class="col-md-8 col-sm-9">
                            Belum terdaftar? <router-link to="/login">Daftar di sini</router-link> 
                        </div>
                        <div class="col-sm-2 justify-content-sm-right">
                          <button id='' class="btn btn-class">
                                Submit</button>
                        </div>
                    </div>
                </form>
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
                axios.post('absen/student/login', {id_jemaat: this.selectedId })
                    .then(response => {
                        // Handle the response as needed
                        console.log(this.selectedId)
                        console.log(response.data)
                        alert(response.data.status)
                    })
                    .catch(error => {
                        console.error('Error submitting form', error);
                    });
                this.selectedId = null;
            }  else {
                alert('not selected!')
            }    
        },
        onItemSelected(id) {
            this.selectedId = id;
            console.log('update')
        },
        navigateToAdmin(){
            this.$router.push('/admin-view')
        }
    },
};

</script>
<style>
@media (max-width: 768px) {
  .content {
    display: flex;
    flex-direction: row;
    /* text-align: center; */
  }
}
</style>