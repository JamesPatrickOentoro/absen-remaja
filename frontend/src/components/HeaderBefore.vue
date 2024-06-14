<template>
  <nav class="navbar-before" id="header-nav" style="box-shadow: rgba(0, 0, 0, .06) 0 0 6px 2px;">
    <div class="container-nav">
      <ul class="navbar-content">
        <li class="nav-item">
          <a class="navbar-logo">Dashboard</a>
        </li>
        <li class="nav-item">
          <button @click.prevent="showAdminLoginForm" class="btn-adminlog" type="button">Admin Login</button>
        </li>
      </ul>
    </div>
  </nav>

  <div v-if="showForm" class="fade show" tabindex="-1" role="dialog" style="display: block;">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Admin Login</h5>
          <button type="button" class="btn-close" @click="closeAdminLoginForm" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div v-if="error" class="alert-danger" role="alert">
            Username atau password salah.
          </div>
          <div class="form-group">
            <input type="text" class="form-control" v-model="adminUsername" placeholder="Username">
          </div>
          <div class="form-group">
            <input type="password" class="form-control" v-model="adminPass" placeholder="Password">
          </div>
        </div>
        <div class="modal-footer">
          <button @click.prevent="adminLogin" class="btn-login">Login</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HeaderBefore',
  data() {
    return {
      showForm: false,
      adminUsername: "",
      adminPass: "",
      error: false
    };
  },
  methods: {
    showAdminLoginForm() {
      this.showForm = true;
    },
    closeAdminLoginForm() {
      this.showForm = false;
    },
    adminLogin() {
      const data = {
        nama_admin: this.adminUsername,
        password: this.adminPass
      };
      axios.post('absen/admin/login', data)
        .then(response => {
          if (response.data.status === 'success') {
            this.$router.push('/admin-view');
          } else {
            console.error('Login gagal');
            this.error = true;
          }
        })
        .catch(error => {
          console.error('ada error', error);
        });
    }
  }
};
</script>

<style>
    /* Basic styles for the header */
   .navbar-before {
  box-shadow: rgba(0, 0, 0, 0.06) 0 0 6px 2px;
  background-color: #fff;
  padding: 10px 20px;
}

.container-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 100%;
  margin: 0 auto;
}

.navbar-content {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
}

.nav-item {
  margin: 0;
}

.navbar-logo {
  text-decoration: none;
  font-size: 1.5em;
  font-weight: normal;
  color: #292929;
}

.btn-adminlog {
  background-color: #007BFF;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 1em;
  cursor: pointer;
  border-radius: 5px;
}

.btn-adminlog:hover {
  background-color: #0056b3;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-dialog {
  max-width: 500px;
  margin: 1.75rem auto;
}

.modal-content {
  padding: 1rem;
  background-color: white;
  border-radius: 8px;
}

.modal-header .btn-close {
  background: none;
  border: none;
  font-size: 1.5rem;
  line-height: 1;
}

.alert-danger {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
  padding: .75rem 1.25rem;
  margin-bottom: 1rem;
  border: 1px solid transparent;
  border-radius: .25rem;
}

.btn-login {
  background-color: #007bff;
  color: white;
  border: none;
  padding: .5rem 1rem;
  cursor: pointer;
}

.btn-login:hover {
  background-color: #0056b3;
}
    /* Responsive styles */
    @media (max-width: 768px) {
      .container-nav {
        flex-direction: row;
        justify-content: space-between;
      }
      .navbar-content {
        flex-direction: row;
        justify-content: space-between;
      }
      .nav-item {
        margin-bottom: 0;
      }
    }
</style>
