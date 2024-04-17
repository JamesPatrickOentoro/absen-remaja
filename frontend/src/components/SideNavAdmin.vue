<template>
    <!-- <h1>hello</h1> -->
    <div class="sidebar" id="card">
        <ul class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start" id="menu">
            <li class="nav-item">
                <a href="#" class="nav-link align-middle px-0">
                    <i class="bi bi-house"></i> <span class="ms-1 d-none d-sm-inline">Attendance</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#" class="nav-link align-middle px-0">
                    <i class="bi bi-house"></i> <span class="ms-1 d-none d-sm-inline">Dashboard</span>
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link align-middle px-0">
                    <i class="bi bi-house"></i> <span class="ms-1 d-none d-sm-inline">Student</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#" class="nav-link align-middle px-0">
                    <i class="bi bi-house"></i> <span class="ms-1 d-none d-sm-inline">Logout</span>
                </a>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'SideNavAdmin',
}
</script>
<style></style>
<link rel="stylesheet" href="@/assets/adminview.css">