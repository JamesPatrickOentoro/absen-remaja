<template>
    <div>
        <h2>All Students</h2>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Date of Birth</th>
                    <th>Class</th>
                    <th>Phone Number</th>
                    <th>Gender</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(student, index) in students" :key="index">
                    <td>{{ student.nama }}</td>
                    <td>{{ formatDate(student.tgl_lahir) }}</td>
                    <td>{{ student.kelas }}</td>
                    <td>{{ student.no_telp }}</td>
                    <td>{{ student.gender }}</td>
                    <td>
                        <button @click="editStudent(student)">
                            <i class="bi bi-pencil-square"></i> <!-- Edit icon -->
                        </button>
                        <button @click="deleteStudent">
                            <i class="bi bi-trash"></i><!-- Delete icon -->
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
        <div v-if="showEditModal" class="modalform">
            <div class="modal-content-section">
                <span class="close" @click="closeEditModal">&times;</span>
                <h2>Edit Student</h2>
                <!-- Edit form -->
                <form @submit.prevent="submitEditForm">
                    <label for="edit-name">Name:</label>
                    <input type="text" id="edit-name" v-model="editedStudent.nama" placeholder="Enter name">
                    <label for="edit-birth">Date of Birth:</label>
                    <input type="text" id="edit-birth" v-model="editedStudent.tgl_lahir"
                        placeholder="Enter date of birth">
                    <label for="edit-email">email:</label>
                    <input type="email" id="email" v-model="editedStudent.email"
                        placeholder="Enter email">
                    <label for="edit-hobby">hobby:</label>
                    <input type="text" id="hobby" v-model="editedStudent.hobi"
                        placeholder="Enter hobby">
                    <!-- Repeat similar structure for other fields -->
                    <button type="submit">Save</button>
                </form>
            </div>
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
            email:'',
            school: '',
            birth_place:'',
            no_telp_ortu:'',
            daerah:'',
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
        },
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
</style>