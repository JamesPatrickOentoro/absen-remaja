<template>
    <HeaderAfter></HeaderAfter>
    <div class="container-fluid d-flex align-items-start" >
    <SideNavAdmin></SideNavAdmin> 
    
    <StudentAttendance></StudentAttendance>
    </div>
   
   
</template>
<script>
import HeaderAfter from '@/components/HeaderAfter.vue';
import SideNavAdmin from '@/components/SideNavAdmin.vue';
import StudentAttendance from '@/components/StudentAttendance.vue'
export default {
    name: 'AdminView',
    components: {
        HeaderAfter,SideNavAdmin,StudentAttendance
    }
}
</script>
<style>
body{
    overflow-y: hidden;
}
</style>