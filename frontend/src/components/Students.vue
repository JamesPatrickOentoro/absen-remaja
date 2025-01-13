<template>
  <div class="header-attendance-container">
    <div class="attend">

      <div class="header-container">
        <h3>Students</h3>
        <div class="button-group">
          <button @click="generateSheet" class="btn btn-success export-button">Export to Excel</button>
          <button @click="confirmUpdateAcademicYear" class="btn btn-warning update-button">Update Academic Year</button>
        </div>
      </div>

      <div class="table-container-attendance">
        <table class="table-sticky">
          <thead style="position: sticky; top: 0; background: #ccc;">
            <tr>
              <th scope="col">Student Name</th>
              <th scope="col">Birthdate</th>
              <th scope="col">Class</th>
              <th scope="col">Phone</th>
              <th scope="col">Gender</th>
              <th scope="col">Status</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(student, index) in students" :key="index">
              <td>{{ student.nama }}</td>
              <td>{{ formatDate(student.tgl_lahir) }}</td>
              <td>{{ student.kelas }}</td>
              <td>{{ student.no_telp }}</td>
              <td>{{ student.gender }}</td>
              <td>{{ student.status }}</td>
              <td>
                <button @click="editStudent(student)" class="btn btn-primary">
                  <i class="bi bi-pencil-square"></i>
                </button>
                <button @click="deleteStudent(student.id_jemaat)" class="btn btn-danger">
                  <i class="bi bi-trash"></i>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-if="showEditModal" class="modalform">
        <div class="modal-content-section">
          <span class="close" @click="closeEditModal">&times;</span>
          <h2>Edit Student</h2>

          <form @submit.prevent="submitEditForm">
            <div class="form-group">
              <label for="edit-name">Name:</label>
              <input type="text" id="edit-name" v-model="editedStudent.nama" class="form-control"
                placeholder="Enter name">
            </div>
            <!-- <div class="form-group">
              <label for="edit-birth">Tanggal Lahir:</label>
              <input type="datetime-local" id="edit-birth" v-model="editedStudent.tgl_lahir" class="form-control"
                placeholder="Enter date of birth">
            </div> -->
            <div class="form-group">
              <label for="edit-birth">Tanggal Lahir:</label>
              <input type="date" id="edit-birth" v-model="editedStudent.tgl_lahir" class="form-control" />
            </div>

            <div class="form-group">
              <label for="edit-email">Email:</label>
              <input type="email" id="edit-email" v-model="editedStudent.email" class="form-control"
                placeholder="Enter email">
            </div>
            <div class="form-group">
              <label for="edit-alamat">Alamat:</label>
              <input type="text" id="edit-alamat" v-model="editedStudent.alamat" class="form-control"
                placeholder="Enter alamat">
            </div>
            <div class="form-group">
              <label for="edit-kelas">Kelas:</label>
              <input type="number" id="edit-kelas" v-model="editedStudent.kelas" class="form-control"
                placeholder="Enter kelas">
            </div>
            <div class="form-group">
              <label for="edit-notelp">Nomor Telpon:</label>
              <input type="number" id="edit-notelp" v-model="editedStudent.no_telp" class="form-control"
                placeholder="Enter nomor telpon">
            </div>
            <button type="submit" class="btn btn-success">Save</button>
          </form>
        </div>
      </div>
    </div>
    <!-- <div class="update-academic-year">
      <button @click="confirmUpdateAcademicYear" class="btn btn-warning">
        Update Academic Year
      </button>
    </div> -->
  </div>
</template>

<script>
import * as XLSX from 'xlsx';
import axios from 'axios';
import dayjs from 'dayjs';
import utc from 'dayjs/plugin/utc';
dayjs.extend(utc);

export default {
  name: 'StudentsList',
  data() {
    return {
      students: [],
      studentId: '',
      name: '',
      birth: '',
      phone: '',
      gender: '',
      class: '',
      email: '',
      school: '',
      birth_place: '',
      no_telp_ortu: '',
      daerah: '',
      kecamatan: '',
      foto: 'nanana',
      status: '',
      address: '',
      showEditModal: false,
      editedStudent: {
        nama: '',
        email: '',
        no_telp: '',
        gender: '',
        hobi: '',
        sekolah: '',
        tgl_lahir: '',
        temp_lahir: '',
        no_telp_ortu: '',
        kelas: null,
        daerah: '',
        kecamatan: '',
        alamat: '',
        foto: 'nanana',
        status: ''
      }
    };
  },
  created() {
    this.fetchStudents();
  },
  methods: {
    async fetchStudents() {
      try {
        const response = await axios.get('absen/all-students');
        console.log("Fetched Students Data:", response.data);
        this.students = response.data.map(student => ({
          ...student,
          tgl_lahir: this.formatDateToYMD(student.tgl_lahir) || '1970-01-01', // Gunakan default jika tidak valid
        }));
      } catch (error) {
        console.error('Error fetching students:', error);
      }
    },

    // formatDate(dateString) {
    //   const date = dayjs(dateString); // Parsing otomatis
    //   if (!date.isValid()) {
    //     console.error("Invalid date format:", dateString);
    //     return dateString; // Kembalikan nilai asli jika tidak valid
    //   }
    //   // Format ke format human-readable
    //   return date.format('ddd, DD MMM YYYY HH:mm:ss [UTC]');
    // },

    formatDateToYMD(dateString) {
      // Gunakan dayjs untuk parsing
      let date = dayjs(dateString, ['YYYY-MM-DD', 'ddd, DD MMM YYYY HH:mm:ss Z']);
      if (!date.isValid()) {
        console.error("Invalid date format:", dateString);
        return '1970-01-01'; // Nilai default jika parsing gagal
      }
      return date.format('YYYY-MM-DD'); // Format menjadi 'YYYY-MM-DD'
    },

    closeEditModal() {
      this.showEditModal = false;
    },

    confirmUpdateAcademicYear() {
      if (confirm("Are you sure you want to update the academic year? This action cannot be undone.")) {
        this.updateAcademicYear();
      }
    },


    updateAcademicYear() {

      axios.post('absen/academic-year')
        .then(response => {
          if (response.data.status === 'success') {
            alert("Academic year updated successfully.");
          } else {
            alert("Failed to update academic year.");
          }
        })
        .catch(error => {
          console.error("Error updating academic year:", error);
          alert("An error occurred while updating the academic year.");
        });
    },

    editStudent(student) {
      this.editedStudent = { ...student };
      this.showEditModal = true;
    },

    submitEditForm() {
      if (this.editedStudent.tgl_lahir) {
        this.editedStudent.tgl_lahir = this.formatDateToYMD(this.editedStudent.tgl_lahir);
      }

      if (this.editedStudent.tgl_lahir) {
    // Ubah ke format yang diharapkan server
    this.editedStudent.tgl_lahir = dayjs(this.editedStudent.tgl_lahir).format('ddd, DD MMM YYYY HH:mm:ss [GMT]');
  }

  axios.post('absen/edit-data-jemaat', this.editedStudent)
    .then(() => {
      const updatedStudentIndex = this.students.findIndex(student => student.id_jemaat === this.editedStudent.id_jemaat);
      if (updatedStudentIndex !== -1) {
        this.students[updatedStudentIndex] = { ...this.editedStudent };
      }
      this.showEditModal = false;
    })
    .catch(error => {
      console.error('Error updating student data:', error);
    });
    },

    deleteStudent(studentId) {
      axios.delete(`absen/delete-jemaat?id_jemaat=${studentId}`)
        .then(() => {
          this.students = this.students.filter(student => student.id_jemaat !== studentId);
        })
        .catch(error => {
          console.error('Error deleting student:', error);
        });
    },
    saveToExcel(data) {
      const ws = XLSX.utils.json_to_sheet(data);
      const wb = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(wb, ws, 'Students-Sheet');
      XLSX.writeFile(wb, 'data-remaja.xlsx');
    },
    generateSheet() {
      this.saveToExcel(this.students);
    },
  }
};
</script>

<style>
.header-attendance-container {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: auto;
  /* width: calc(100% - 40px); */
  min-width: 100%;
  max-width: 100%
}

.attend {
  margin: 0 auto;
}

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.button-group {
  display: flex;
  gap: 10px;
}

.table-container-attendance {
  max-height: 60vh;
  /* Set a fixed height */
  overflow-y: auto;
  /* Enable vertical scrolling */
}

.table-sticky {
  width: 100%;
  border: #444444 solid 1px;
}

.modalform {
  display: block !important;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1000;
}

.modal-content-section {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fefefe;
  padding: 20px;
}

/* Close button styles */
.close {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  font-size: 20px;
  color: #aaa;
}

.close:hover,
.close:focus {
  color: #000;
}

.table-sticky th,
.table-sticky td {
  padding: 12px 15px;
  border: 1px solid #ddd;
  text-align: left;
}

/* .table-sticky th {
  background-color: #f4f4f4;
  border: 1px solid #ddd;
}

.table-sticky tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}

.table-sticky tbody tr:hover {
  background-color: #f1f1f1;
} */
.table-container-attendance {
  max-height: 60vh;
  overflow-y: auto;
}

.table-sticky {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
}

.table-sticky th {
  position: sticky;
  top: 0;
  background-color: #f4f4f4;
  z-index: 1;
  text-align: left;
  padding: 12px 15px;
  border: 1px solid #ddd;
}

.table-sticky td {
  padding: 12px 15px;
  border: 1px solid #ddd;
}

.table-sticky tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}

.table-sticky tbody tr:hover {
  background-color: #f1f1f1;
}

/* Form input styles */
form label {
  display: block;
  margin-bottom: 5px;
}

form input[type="text"] {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

/* Submit button styles */
form button {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

form button:hover {
  background-color: #0056b3;
}

.update-academic-year {
  margin-top: 20px;
}

@media (max-width: 768px) {
  .header-attendance-container {
    padding: 5px;
    margin: 5px;
    width: calc(100% - 10px);
  }

  .table-sticky th,
  .table-sticky td {
    padding: 6px 8px;
    font-size: 14px;
  }

  .modal-content-section {
    width: 95%;
    padding: 5px;
  }
}
</style>
