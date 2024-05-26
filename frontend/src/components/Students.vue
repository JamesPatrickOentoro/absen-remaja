<!-- <template>
    <div class="container-fluid">
        <div class="attend">
            <h3>Attendance</h3>

            <div class="table-container">
                <div class="table-responsive">
                    <table class="table table-hover table-sticky">
                        <thead style="position: sticky;top:0;background: #ccc;">
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
                            <div class="form-group">
                                <label for="edit-birth">Date of Birth:</label>
                                <input type="datetime-local" id="edit-birth" v-model="editedStudent.tgl_lahir"
                                    class="form-control" placeholder="Enter date of birth">
                            </div>
                            <div class="form-group">
                                <label for="edit-email">Email:</label>
                                <input type="email" id="email" v-model="editedStudent.email" class="form-control"
                                    placeholder="Enter email">
                            </div>
                            <div class="form-group">
                                <label for="edit-alamat">alamat</label>
                                <input type="text" id="alamat" v-model="editedStudent.alamat" class="form-control"
                                    placeholder="Enter alamat">
                            </div>
                            <div class="form-group">
                                <label for="edit-kelas">kelas</label>
                                <input type="number" id="kelas" v-model="editedStudent.kelas" class="form-control"
                                    placeholder="Enter kelas">
                                </div>
                                <div class="form-group">
                                    <label for="edit-notelp">nomor telpon</label>
                                    <input type="number" id="notelp" v-model="editedStudent.no_telp" class="form-control"
                                        placeholder="Enter nomor telpon">
                                </div>
                            <button type="submit" class="btn btn-success">Save</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <div class="update-academic-year" style="margin-top: 100px;">
            <button @click="confirmUpdateAcademicYear" class="btn btn-warning">
                Update Academic Year
            </button>
        </div>
    </div>
</template>


<script>
import axios from 'axios';
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
            },
        };
    },
    created() {
        this.fetchStudents();
    },
    methods: {
        async fetchStudents() {
            try {
                const response = await axios.get('absen/all-students', {
                    params: {
                        id_jemaat: this.studentId,
                        nama: this.name,
                        tgl_lahir: this.birth,
                        kelas: this.kelas,
                        no_telp: this.no_telp,
                        gender: this.gender,
                        email: this.email,
                        sekolah: this.school,
                        temp_lahir: this.birth_place,
                        no_telp_ortu: this.no_telp_ortu,
                        daerah: this.daerah,
                        kecamatan: this.kecamatan,
                        alamat: this.address,
                        status: this.status,
                        foto: this.foto
                    }
                });
                console.log(response)
                this.students = response.data;
            } catch (error) {
                console.error('Error fetching absents:', error);
            }
        },

        formatDate(dateString) {
            const date = new Date(dateString);
            const day = date.getDate().toString().padStart(2, '0');
            const month = (date.getMonth() + 1).toString().padStart(2, '0');
            const year = date.getFullYear();
            return `${day}-${month}-${year}`;
        },
        closeEditModal() {
            // Close edit modal
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
                        // Optionally refresh the students list or other relevant data
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
            // Set edited student data and show edit modal
            console.log('edit student msuk');
            console.log(student.id_jemaat);
            console.log('Editing student:', student);
            this.editedStudent = {
                id_jemaat: student.id_jemaat,
                nama: student.nama,
                email: student.email,
                no_telp: student.no_telp,
                gender: student.gender,
                hobi: student.hobi,
                sekolah: student.sekolah,
                tgl_lahir: student.tgl_lahir,
                temp_lahir: student.temp_lahir,
                no_telp_ortu: student.no_telp_ortu,
                kelas: student.kelas,
                daerah: student.daerah,
                kecamatan: student.kecamatan,
                alamat: student.alamat,
                foto: student.foto,
                status: student.status
            };
            this.showEditModal = true;
            console.log(this.showEditModal);
        },
        submitEditForm() {
            // Send a request to the server to update the student data
            axios.post('absen/edit-data-jemaat', this.editedStudent)
                .then(() => {
                    // Update the student data in the UI
                    const updatedStudentIndex = this.students.findIndex(student => student.id_jemaat === this.editedStudent.id_jemaat);
                    if (updatedStudentIndex !== -1) {
                        this.students[updatedStudentIndex] = { ...this.editedStudent };
                    }
                    // Close the edit modal
                    this.showEditModal = false;
                    // Reset the edited student data
                    this.editedStudent = {
                        nama: '',
                        email: '',
                        no_telp: '',
                        gender: '',
                        hobi: '',
                        sekolah: '',
                        tgl_lahir: '',
                        temp_lahir: '',
                        no_telp_ortu: '',
                        kelas: '',
                        daerah: '',
                        kecamatan: '',
                        alamat: '',
                        foto: 'nanana',
                        status: ''
                    };
                })
                .catch(error => {
                    console.error('Error updating student data:', error);
                    // Optionally, display an error message to the user
                });
        }, deleteStudent(studentId) {
            // Send a DELETE request to delete the student by id_jemaat
            axios.delete(`absen/delete-jemaat?id_jemaat=${studentId}`)
                .then(() => {
                    // If deletion is successful, remove the student from the UI
                    this.students = this.students.filter(student => student.id_jemaat !== studentId);
                })
                .catch(error => {
                    console.error('Error deleting student:', error);
                    // Optionally, display an error message to the user
                });
        }
    },
};
</script>

<style>
.modalform {
    display: block !important;
    /* Force modal to be visible */
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    /* Semi-transparent background */
    z-index: 1000;
    /* Ensure modal appears above other content */
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

/* Add your styles here */
</style> -->
<template>
    <div class="container-fluid">
      <div class="attend">
        <h3>Attendance</h3>
  
        <div class="table-container">
          <div class="table-responsive">
            <table class="table table-hover table-sticky">
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
        </div>
  
        <div v-if="showEditModal" class="modalform">
          <div class="modal-content-section">
            <span class="close" @click="closeEditModal">&times;</span>
            <h2>Edit Student</h2>
  
            <form @submit.prevent="submitEditForm">
              <div class="form-group">
                <label for="edit-name">Name:</label>
                <input type="text" id="edit-name" v-model="editedStudent.nama" class="form-control" placeholder="Enter name">
              </div>
              <div class="form-group">
                <label for="edit-birth">Date of Birth:</label>
                <input type="datetime-local" id="edit-birth" v-model="editedStudent.tgl_lahir" class="form-control" placeholder="Enter date of birth">
              </div>
              <div class="form-group">
                <label for="edit-email">Email:</label>
                <input type="email" id="edit-email" v-model="editedStudent.email" class="form-control" placeholder="Enter email">
              </div>
              <div class="form-group">
                <label for="edit-alamat">Alamat:</label>
                <input type="text" id="edit-alamat" v-model="editedStudent.alamat" class="form-control" placeholder="Enter alamat">
              </div>
              <div class="form-group">
                <label for="edit-kelas">Kelas:</label>
                <input type="number" id="edit-kelas" v-model="editedStudent.kelas" class="form-control" placeholder="Enter kelas">
              </div>
              <div class="form-group">
                <label for="edit-notelp">Nomor Telpon:</label>
                <input type="number" id="edit-notelp" v-model="editedStudent.no_telp" class="form-control" placeholder="Enter nomor telpon">
              </div>
              <button type="submit" class="btn btn-success">Save</button>
            </form>
          </div>
        </div>
      </div>
      <div class="update-academic-year">
        <button @click="confirmUpdateAcademicYear" class="btn btn-warning">
          Update Academic Year
        </button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
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
          console.log(response);
          this.students = response.data;
        } catch (error) {
          console.error('Error fetching absents:', error);
        }
      },
      formatDate(dateString) {
        const date = new Date(dateString);
        const day = date.getDate().toString().padStart(2, '0');
        const month = (date.getMonth() + 1).toString().padStart(2, '0');
        const year = date.getFullYear();
        return `${day}-${month}-${year}`;
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
        axios.post('absen/edit-data-jemaat', this.editedStudent)
          .then(() => {
            const updatedStudentIndex = this.students.findIndex(student => student.id_jemaat === this.editedStudent.id_jemaat);
            if (updatedStudentIndex !== -1) {
              this.students[updatedStudentIndex] = { ...this.editedStudent };
            }
            this.showEditModal = false;
            this.editedStudent = {
              nama: '',
              email: '',
              no_telp: '',
              gender: '',
              hobi: '',
              sekolah: '',
              tgl_lahir: '',
              temp_lahir: '',
              no_telp_ortu: '',
              kelas: '',
              daerah: '',
              kecamatan: '',
              alamat: '',
              foto: 'nanana',
              status: ''
            };
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
      }
    }
  };
  </script>
  
  <style scoped>
  .container-fluid {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px;
  }
  
  .attend {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .table-container {
    width: 100%;
    overflow-x: auto;
    margin-bottom: 20px;
  }
  
  .table-sticky thead {
    background: #ccc;
    position: sticky;
    top: 0;
  }
  
  .update-academic-year {
    margin-top: 20px;
    display: flex;
    justify-content: center;
  }
  
  .modalform {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1000;
  }
  
  .modal-content-section {
    background-color: #fefefe;
    padding: 20px;
    border-radius: 8px;
    max-width: 500px;
    width: 100%;
    margin: 0 10px;
  }
  
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
  
  form label {
    display: block;
    margin-bottom: 5px;
  }
  
  form input[type="text"],
form input[type="datetime-local"],
form input[type="email"],
form input[type="number"] {
  width: 100%;
  margin-bottom: 10px;
}

@media (max-width: 600px) {
  .table-responsive {
    overflow-x: auto;
  }

  .modal-content-section {
    width: 90%;
  }

  .table th, .table td {
    padding: 8px;
    font-size: 12px;
  }

  .table-container {
    margin-bottom: 15px;
  }

  .update-academic-year {
    margin-top: 15px;
  }

  h3 {
    font-size: 1.5em;
  }
}
</style>