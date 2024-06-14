<!-- <template>
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
</template> -->

<!-- <script>
export default {
    name: 'SideNavAdmin',
}
</script>
<style></style>
<link rel="stylesheet" href="@/assets/adminview.css"> -->
<template>
    <div>
      <!-- Hamburger icon visible on smaller screens -->
      <button class="navbar-toggler" type="button" @click="toggleMenu">
        <span class="navbar-toggler-icon"></span>
      </button>
      <!-- Sidebar -->
      <div :class="['sidebar', { 'open': isOpen }]" id="card">
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
    </div>
  </template>
  
  <script>
  export default {
    name: 'SideNavAdmin',
    data() {
      return {
        isOpen: false
      };
    },
    methods: {
      toggleMenu() {
        this.isOpen = !this.isOpen;
      }
    }
  }
  </script>
  
  <style scoped>
  .sidebar {
    /* Default sidebar styles */
    display: flex;
    flex-direction: column;
    height: 100vh;
    width: 250px;
    background-color: #f8f9fa;
    transition: transform 0.3s ease-in-out;
  }
  
  .sidebar.open {
    transform: translateX(0);
  }
  
  @media (max-width: 768px) {
    .sidebar {
      transform: translateX(-100%);
    }
    .navbar-toggler {
      display: inline-block;
    }
  }
  
  /* Hide the toggle button on larger screens */
  .navbar-toggler {
    display: none;
    border: none;
    background: none;
    font-size: 1.5rem;
  }
  
  /* Custom style for navbar-toggler-icon (hamburger icon) */
  .navbar-toggler-icon {
    display: inline-block;
    width: 24px;
    height: 24px;
    background-size: contain;
    background-image: url('data:image/svg+xml;charset=utf8,%3Csvg viewBox="0 0 30 30" xmlns="http://www.w3.org/2000/svg"%3E%3Cpath stroke="rgba%28150,150,150,0.7%29" stroke-width="2" linecap="round" linejoin="round" d="M4 7h22M4 15h22M4 23h22"/%3E%3C/svg%3E');
  }
  
  /* Ensuring the sidebar is above other content when toggled */
  .sidebar {
    z-index: 1000;
    position: fixed;
    top: 0;
    left: 0;
  }
  </style>
  
  <!-- <link rel="stylesheet" href="@/assets/adminview.css"> -->
  