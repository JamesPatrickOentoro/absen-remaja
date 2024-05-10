<template>
    <div class="card">
        <div class="card-content">
            <select v-model="selectedYear" class="select">
                <option disabled selected value="">Year</option>
                <option v-for="year in years" :key="year">{{ year }}</option>
            </select>
            <select v-model="selectedMonth" class="select" >
                <option disabled selected value=""> Month</option>
                <option v-for="(month, index) in months" :key="month" :value="index + 1">{{ month }}</option>
            </select>
            <button @click="fetchMonthlyAbsentData" class="button">generate</button>
        </div>
        <div class="card-chart">
            <canvas id="barChart" width="400" height="300"></canvas>
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
            years: ['2022', '2023', '2024'], // Add years as needed
            months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            chart: null,
            chartData: {
                type: 'bar',
                labels: [],
                datasets: [{
                    label: 'Jumlah',
                    data: [],
                    // backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    // borderColor: 'rgba(54, 162, 235, 1)',
                    // borderWidth: 1
                }]
            } // Variable to store the chart instance
        };
    },
    mounted() {
        // Render an empty chart on component mount
        this.renderChart([], []);
    },
    methods: {
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
                const day = String(date.getDate()).padStart(2, '0');
                const month = String(date.getMonth() + 1).padStart(2, '0');
                const year = String(date.getFullYear()).slice(-2);
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
        }
    }
};
</script>
<style>
.card {
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
    background-color: #fff;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}

.card-content {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
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
}
</style>