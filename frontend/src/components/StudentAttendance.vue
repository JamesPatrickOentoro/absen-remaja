<template>
    <div class="container-fluid">
        <div class="attend">
            <h3>Attendance</h3>
            <div class="filterbar">
                <div class="row">
                    <div class="col-2 col-md-3">
                        <div class="row">
                            <label>Name</label>
                        </div>
                        <div class="row">
                            <input type="text" v-model="filterName">
                        </div>
                    </div>
                    <div class="col-4 col-md-2">
                        <input class='bottom' style="border-radius: 5px; border:1px solid #ccc; padding:5px" type="date"
                          v-model="filterDate" >
                    </div>
                    <div class="col-3 col-md-2">
                    <select class="form-select bottom" v-model="filterStatus" @change="filterData">
                        <option value="">All</option>
                        <option value="active">Active</option>
                        <option value="inactive">Inactive</option>
                    </select>
                </div>
                    <div class="col-5 col-md-3">
                        <button class="bottom" @click="search">Search</button>
                        <button class="bottom" @click="generateSheet">Generate Sheet</button>
                    </div>
                </div>
            </div>

            <div class="table-container">
                <div class="table-responsive">
                    <table class="table table-hover table-sticky">
                        <thead style="position: sticky;top:0;background: #ccc;">
                            <tr>
                                <th scope="col">Student Name</th>
                                <th scope="col">Student ID</th>
                                <th scope="col">Date/Time</th>
                                <th scope="col">Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(absent, i) in absents" :key="i">
                                <td>{{ absent.nama }}</td>
                                <td>{{ absent.id_jemaat }}</td>
                                <td>{{ absent.waktu_absen }}</td>
                                <td>{{ absent.status }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// import AttendanceTable from '@/components/AttendanceTable.vue';
import * as XLSX from 'xlsx';
import axios from 'axios';
export default {
    name: 'StudentAttendance',
    // components:{
    //     AttendanceTable
    // },
    props: {
        items: {
            type: Array,
            required: false,
            default: () => [],
        },
    },
    data() {
        return {
            absents: [],
            filterName: '', // Filter by name
            filterStatus: '', // Filter by status
            filterDate: '', // Filter by datetime
        };
    },
    mounted() {
        this.fetchAbsents();
    },
    methods: {
        async fetchAbsents() {
            try {
                const response = await axios.get('http://127.0.0.1:5000/filter-absent-data', {
                    params: {
                        status: this.filterStatus,
                        nama: this.filterName,
                        tanggal: this.filterDate
                    }
                });
                this.absents = response.data;
            } catch (error) {
                console.error('Error fetching absents:', error);
            }
        },
        search() {
            this.fetchAbsents(); // Call fetchAbsents() when search button is clicked
        },
        // Fungsi untuk menyimpan data ke file Excel
        saveToExcel(data) {
            const ws = XLSX.utils.json_to_sheet(data);
            const wb = XLSX.utils.book_new();
            XLSX.utils.book_append_sheet(wb, ws, 'Sheet1');
            XLSX.writeFile(wb, 'data-absensi.xlsx');
        },

        // Panggil fungsi ini dari generateSheet di komponen Vue
        generateSheet() {
            this.saveToExcel(this.absents);
        },
        
        
    }
}

</script>
<style>
.table-container {
    height: 280px;
    overflow: auto;
    min-height: 10em;
    max-height: 80em;
}
</style>