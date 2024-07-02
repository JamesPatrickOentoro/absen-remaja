<template>
    <div class="header-attendance-container">
        <div class="attend">
            <h3>Attendance</h3>
            <div class="attendance-filterbar">
                <div class="attendance-item">
                    <div class="attend-items">
                        <div class="a-item">
                            <label>Name</label>
                            <input type="text" v-model="filterName">
                        </div>
                        <div class="a-item">
                            <label>Date</label>
                            <input class="button" type="date" v-model="filterDate">
                        </div>
                        <div class="a-item">
                            <label>Status</label>
                            <select class="form-select" v-model="filterStatus" @change="filterData">
                                <option value="">All</option>
                                <option value="active">Active</option>
                                <option value="inactive">Inactive</option>
                            </select>
                        </div>
                        <div class="a-item">
                            <button class="button" @click="search">Search</button>
                            <button class="button" @click="generateSheet">Generate Sheet</button>
                        </div>
                    </div>
                </div>
            </div>

            <div class="table-container-attendance">
                <table class="table-sticky">
                    <thead style="position: sticky; top: 0; background: #ccc;">
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
</template>

<script>
import * as XLSX from 'xlsx';
import axios from 'axios';

export default {
    name: 'StudentAttendance',
    data() {
        return {
            absents: [],
            filterName: '',
            filterStatus: '',
            filterDate: '',
        };
    },
    mounted() {
        this.fetchAbsents();
    },
    methods: {
        async fetchAbsents() {
            try {
                const response = await axios.get('absen/filter-absent-data', {
                    params: {
                        status: this.filterStatus,
                        nama: this.filterName,
                        tanggal: this.filterDate,
                    }
                });
                console.log(this.filteDate);
                this.absents = response.data;
            } catch (error) {
                console.error('Error fetching absents:', error);
            }
        },
        search() {
            this.fetchAbsents();
        },
        saveToExcel(data) {
            const ws = XLSX.utils.json_to_sheet(data);
            const wb = XLSX.utils.book_new();
            XLSX.utils.book_append_sheet(wb, ws, 'Sheet1');
            XLSX.writeFile(wb, 'data-absensi.xlsx');
        },
        generateSheet() {
            this.saveToExcel(this.absents);
        },
    },
}
</script>

<style scoped>
.header-attendance-container {
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin: auto;
    min-width: 80%;
}

.attend {
    margin: 0 auto;
}

.attendance-filterbar {
    margin-bottom: 20px;
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    justify-content: space-between;
    align-items: center;
}

.attendance-item {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
}

.attend-items {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
}

.a-item {
    flex: 1;
    min-width: 150px;
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.a-item label {
    font-weight: bold;
}

.button {
    border-radius: 5px;
    border: none;
    padding: 8px 15px;
    background-color: #007bff;
    color: white;
    cursor: pointer;
    transition: background-color 0.3s;
}

.button:hover {
    background-color: #0056b3;
}

.table-container-attendance {
    /* overflow-x: auto; */
    max-height: 60vh;
    overflow-y: auto;
}

.table-sticky {
    width: 100%;
    border-collapse: collapse;
}

.table-sticky th, .table-sticky td {
    padding: 12px 15px;
    border: 1px solid #ddd;
    text-align: left;
}
input{
    border-radius: 8px;
}
.table-sticky th {
    background-color: #f4f4f4;
}

.table-sticky tbody tr:nth-child(even) {
    background-color: #f9f9f9;
}

.table-sticky tbody tr:hover {
    background-color: #f1f1f1;
}

@media (max-width: 768px) {
    .header-attendance-container {
        padding: 12px;
        margin-top: 20px;
    }

    .attendance-filterbar {
        flex-direction: row;
        gap: 12px;
    }

    .attend-items {
        flex-direction: row;
        gap: 10px;
    }
    .attend h3 {
    margin-bottom: 25px;
}

    .a-item {
        width: 100%;
    }
    .table-container-attendance {
    /* overflow-x: auto; */
    max-height: 40vh;
    overflow-y: auto;
}
}
</style>
