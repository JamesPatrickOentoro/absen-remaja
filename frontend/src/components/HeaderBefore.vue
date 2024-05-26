<template>
  <nav class="navbar navbar-expand-lg" id="header-nav" style="box-shadow: rgba(0, 0, 0, .06) 0 0 6px 2px;">
    <div class="container-fluid">
      <a class="navbar-brand">Dashboard</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarContent">
        <div class="ms-auto">
          <button @click.prevent="showAdminLoginForm" class="btn btn-outline-success" type="button">Admin Login</button>
          <div v-if="showForm" class="modal" tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title">Admin Login</h5>
                  <button type="button" class="close" @click="closeAdminLoginForm" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
                <div class="modal-body">
                  <div v-if="error" class="alert alert-danger" role="alert">
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
                  <button @click.prevent="adminLogin" class="btn btn-primary">Login</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
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

<style scoped>
.modal {
  display: block;
  position: fixed;
  z-index: 1050;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0,0,0,0.4);
}

.header-nav {
  width: 100%;
  height: 20%;
}

.modal-content {
  background-color: #fefefe;
  margin: 10% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 90%;
  max-width: 500px;
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
</style>
