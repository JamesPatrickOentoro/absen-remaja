<template>
    <div id="app" class="dashboard-container">
        <!-- Left side -->
        <div class="dashboard-column">
            <div class="contain">
                <!-- Dashboard card for Attended -->
                <div class="card-absent">
                    <div class="card-content-absent">
                        <h2> Attended</h2>
                        <p>{{ attended }}</p>
                    </div>
                </div>
            </div>

            <!-- New Comers -->
            <div class="new-comer-container">
                <h2>New Comers</h2>
                <div class="new-comer-content">
                    <div class="new-comer-elements">
                        <div v-for="newComer in newCommers" :key="newComer.id" class="new-comer-card">
                            <p>{{ newComer.nama }}</p>
                            <p>{{ formatDate(newComer.tanggal) }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Middle -->
        <div class="dashboard-column">
            <!-- Generate Monthly Absent Data -->
            <div class="other-contain">
                <div class="card">
                    <div class="card-content">
                        <select v-model="selectedYear" class="select">
                            <option disabled selected value="">Year</option>
                            <option v-for="year in years" :key="year">{{ year }}</option>
                        </select>
                        <select v-model="selectedMonth" class="select">
                            <option disabled selected value="">Month</option>
                            <option v-for="(month, index) in months" :key="month" :value="index + 1">{{ month }}
                            </option>
                        </select>
                        <button @click="fetchMonthlyAbsentData" class="button">Generate</button>
                    </div>
                    <div class="card-chart">
                        <canvas id="barChart" width="400" height="300"></canvas>
                    </div>
                </div>
            </div>
        </div>

        <!-- Right side -->
        <div class="dashboard-column">
            <!-- Absent Students -->
            <div class="new-comer-container">
                <h2>Absent Students</h2>
                <div class="new-comer-content">
                    <div class="new-comer-elements">
                        <div v-for="absentStudent in absentStudents" :key="absentStudent.id" class="new-comer-card">
                            <p>{{ absentStudent.nama }}</p>
                            <p>{{ formatDate(absentStudent.waktu_absen) }}</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Birthdays -->
            <div class="new-comer-container">
                <h2>Birthdays</h2>
                <div class="new-comer-content">
                    <div class="new-comer-elements">
                        <div v-for="birthday in studentBirthdays" :key="birthday.id" class="new-comer-card">
                            <p>{{ birthday.nama }}</p>
                            <p>{{ formatDate(birthday.tanggal) }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Chart from 'chart.js/auto';

export default {
    data() {
        return {
            selectedYear: '',
            selectedMonth: '',
            years: [], // Add years as needed
            months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            chart: null,
            absent: 0,
            attended: 0,
            chartData: {
                type: 'bar',
                labels: [],
                datasets: [{
                    label: 'Jumlah',
                    data: [],
                }]
            }, // Variable to store the chart instance
            newCommers: [],
            absentStudents: [],
            studentBirthdays: [],
        };
    },
    mounted() {
        // Render an empty chart on component mount
        this.generateYears();
        this.renderChart([], []);
        this.fetchTodayAttendance();
        this.fetchNewCommers();
        this.fetchAbsentStudents();
        this.fetchBirthdays();

        // Panggil metode setiap 5 menit
        this.interval = setInterval(() => {
            this.fetchMonthlyAbsentData();
            this.fetchTodayAttendance();
            this.fetchNewCommers();
        }, 300000); // 300000 milidetik = 5 menit
    },
    unmounted() {
        // Hapus interval saat komponen dihancurkan untuk mencegah kebocoran memori
        clearInterval(this.interval);
    },

    methods: {
        generateYears() {
            const currentYear = new Date().getFullYear();
            const startYear = currentYear - 10; // Adjust this to include more years if needed
            for (let year = startYear; year <= currentYear; year++) {
                this.years.push(year.toString());
            }
        },
        fetchMonthlyAbsentData() {
            const year = this.selectedYear;
            const monthIndex = this.selectedMonth - 1;
            const month = (monthIndex < 9 ? '0' : '') + (monthIndex + 1).toString();
            console.log(month)
            console.log(year)

            axios.post('/absen/monthly-absent', { year, month })
                .then(response => {
                    console.log('Data fetched:', response.data);

                    // Extract jumlah and minggu lists from the response data
                    const jumlah = response.data.jumlah;
                    const minggu = response.data.minggu;


                    // Use jumlah and minggu as needed
                    console.log('Jumlah:', jumlah);
                    console.log('Minggu:', minggu);

                    this.renderChart(jumlah, minggu);
                })
                .catch(error => {
                    console.error('Error fetching monthly absent data:', error);
                });
        },
        renderChart(jumlah, minggu) {
            const formattedMinggu = minggu.map(dateString => {
                const date = new Date(dateString);
                const day = String(date.getUTCDate()).padStart(2, '0');
                const month = String(date.getUTCMonth() + 1).padStart(2, '0');
                const year = String(date.getUTCFullYear()).slice(-2);
                return `${day}-${month}-${year}`;
            });
            // Update chart data
            this.chartData.labels = formattedMinggu;
            this.chartData.datasets[0].data = jumlah;

            // Destroy existing chart if it exists
            if (this.chart) {
                this.chart.destroy();
            }

            // Create a new chart instance
            this.chart = new Chart(document.getElementById('barChart'), {
                type: 'bar',
                data: this.chartData, // Use updated chart data
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        },
        fetchTodayAttendance() {
            axios.post('absen/today-attendance')
                .then(response => {
                    this.absent = response.data.absent;
                    this.attended = response.data.attended;
                })
                .catch(error => {
                    console.error('Error fetching today attendance:', error);
                });
        },
        fetchNewCommers() {
            axios.post('absen/new-commers')
                .then(response => {
                    this.newCommers = response.data;
                    console.log(this.newCommers);
                })
                .catch(error => {
                    console.error('Error fetching new commers:', error);
                });
        },
        fetchAbsentStudents() {
            axios.post('absen/long-absent').then(
                response => {
                    this.absentStudents = response.data;
                    console.log(this.absentStudents)
                })
                .catch(
                    error => {
                        console.error('Error fetching absents', error);
                    }
                )
        },
        formatDate(dateString) {
            const date = new Date(dateString);
            const day = date.getDate().toString().padStart(2, '0');
            const month = (date.getMonth() + 1).toString().padStart(2, '0');
            const year = date.getFullYear();
            return `${day}/${month}/${year}`;
        },
        fetchBirthdays() {
            axios.post('absen/weekly-birthday').then(
                response => {
                    this.studentBirthdays = response.data;
                    console.log(this.studentBirthdays)
                })
                .catch(
                    error => {
                        console.error('Error fetching birthdays', error);
                    }
                )
        }
    },
};
</script>

<style>
.dashboard-container {
    display: flex;
    flex-wrap: wrap;
    /* margin-left: 90px; */
    max-width: 100%;
    overflow-x: none;
    max-height: 80vh;
    scroll-behavior: smooth;
    overflow-y: auto;
}

.dashboard-column {
    flex: 1;
    min-width: 500px;
    margin-right: 20px;
}


@media (max-width: 768px) {
    .dashboard-column {
        flex: 100%;
        margin-right: 0;
        margin-bottom: 20px;
        overflow-x: hidden;
        max-width: 90%;
        /* transform: translateX(-120px); */
    }
}

.contain {
    gap: 6px;
}

.other-contain {
    margin-left: 20px;
}

/* new commer  */
.new-comer-container {
    margin-left: 20px;
    max-height: 350px;
    border: 1px solid #ccc;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
}

.new-comer-content {
    overflow-y: auto;
    max-height: 250px;
    padding: 20px;
}

.new-comer-elements {
    overflow-y: auto;
}

.new-comer-card {
    margin-top: 10px;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
}

.new-comer-card p {
    font-size: 18px;
    margin-bottom: 10px;
}

.card {
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
    background-color: #fff;
    height: 500px;
}

.card-content {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 20px;
    flex-wrap: wrap;
}

.select {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: #f9f9f9;
}

.button {
    padding: 8px 20px;
    border: none;
    border-radius: 4px;
    background-color: #007bff;
    color: #fff;
    cursor: pointer;
    transition: background-color 0.3s;
}

.button:hover {
    background-color: #0056b3;
}

.card-chart {
    flex-grow: 1;
    padding: 20px;
    width: 100%;
}

.card-absent {
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
    background-color: #fff;
    height: 50%;
    margin-left: 20px;
}

.card-content-absent {
    text-align: left;
}

.card-absent h2 {
    margin-bottom: 10px;
}

.card-absent p {
    font-size: 32px;
    font-weight: bold;
}
</style>
