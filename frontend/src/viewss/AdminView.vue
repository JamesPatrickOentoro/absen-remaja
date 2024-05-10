<template>
    <HeaderAfter></HeaderAfter>
    <div class="container-fluid d-flex align-items-start">
        <div class="sidebar" id="card">
            <ul class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start" id="menu">
                <li class="nav-item">
                    <a href="#" class="nav-link align-middle px-0" @click="switchComponent('StudentAttendance')">
                       <span class="ms-2 d-none d-sm-inline">Attendance</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link align-middle px-0" @click="switchComponent('AdminDashboard')">
                         <span class="ms-2 d-none d-sm-inline">Dashboard</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link align-middle px-0" @click="switchComponent('StudentsList')">
                         <span class="ms-2 d-none d-sm-inline">Students</span>
                    </a>
                </li>
                <!-- Add other menu items as needed -->
            </ul>
        </div>
        <component :is="component"></component>
    </div>
</template>

<script>
import HeaderAfter from '@/components/HeaderAfter.vue';
import StudentAttendance from '@/components/StudentAttendance.vue';
import AdminDashboard from '@/components/AdminDashboard.vue';
import StudentsList from '@/components/Students.vue';

export default {
    name: 'AdminView',
    components: {
        HeaderAfter,
        StudentAttendance,
        AdminDashboard,
        StudentsList,
    },
    data() {
        return {
            component: 'StudentAttendance' // Default component
        };
    },
    methods: {
        switchComponent(componentName) {
            this.component = componentName;
        }
    }
}
</script>

<style>
/* Add your styles here */
</style>
