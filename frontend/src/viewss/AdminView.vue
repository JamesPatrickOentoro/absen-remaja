<template>
    <HeaderAfter></HeaderAfter>
    <div class="container-fluid d-flex align-items-start">
        <div class="sidebar" :class="{ open: isMenuOpen }" id="card">
            <ul class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start" id="menu">
                <li class="nav-item" v-for="(item, index) in menuItems" :key="index">
                    <a href="#" class="nav-link align-middle px-0" @click="switchComponent(item.component)">
                        <span class="ms-2 d-none d-sm-inline">{{ item.label }}</span>
                    </a>
                </li>
            </ul>
        </div>
        <div class="content">
            <component :is="component"></component>
        </div>
        <button class="hamburger" @click="toggleMenu">
            <span class="hamburger-icon"></span>
            <span class="hamburger-icon"></span>
            <span class="hamburger-icon"></span>
        </button>
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
            component: 'StudentAttendance', // Default component
            isMenuOpen: false,
            menuItems: [
                { label: 'Attendance', component: 'StudentAttendance' },
                { label: 'Dashboard', component: 'AdminDashboard' },
                { label: 'Students', component: 'StudentsList' },
                { label: 'Logout', component: 'handleLogout' },
            ]
        };
    },
    methods: {
        switchComponent(componentName) {
            if (componentName === 'handleLogout') {
                this.handleLogout();
            } else {
                this.component = componentName;
                this.isMenuOpen = false; // Close the menu after selecting an option
            }
        },
        toggleMenu() {
            this.isMenuOpen = !this.isMenuOpen; // Toggle the menu open/close state
        },
        handleLogout() {
            // Clear user data from local storage
            localStorage.removeItem('userToken');
            localStorage.removeItem('userData');
            // Redirect to the login page
            this.$router.push('/');
        }
    }
}
</script>


<style>
.container-fluid {
    position: relative;
}

.sidebar {
    width: 250px;
    transition: transform 0.3s ease-in-out;
}

.content {
    flex: 1;
    padding: 20px;
}

.hamburger {
    display: none;
    position: fixed;
    top: 15px;
    right: 15px;
    z-index: 1000;
    background: none;
    border: none;
    cursor: pointer;
}

.hamburger-icon {
    width: 30px;
    height: 3px;
    background-color: #333;
    display: block;
    margin: 6px 0;
    transition: 0.3s;
}

@media (max-width: 768px) {
    .sidebar {
        transform: translateX(-100%);
        position: fixed;
        top: 0;
        left: 0;
        height: 100%;
        z-index: 999;
        background-color: #fff;
        overflow-y: auto;
    }
    
    .sidebar.open {
        transform: translateX(0);
    }

    .hamburger {
        display: block;
    }

    .nav-item {
        width: 100%;
        text-align: center;
    }

    .nav-link {
        display: block;
        width: 100%;
        padding: 10px;
        text-align: center;
        background: #f8f9fa;
        border-bottom: 1px solid #dee2e6;
    }

    .nav-link:hover {
        background: #e9ecef;
    }

    .nav-link .ms-2 {
        display: inline !important;
    }
}
</style>
