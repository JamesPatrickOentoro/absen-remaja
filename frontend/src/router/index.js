import{createRouter, createWebHistory} from 'vue-router';
import HomeView from '@/viewss/HomeView.vue'
import AdminView from '@/viewss/AdminView.vue'
import StudentSignUp from '@/components/StudentSignUp.vue'
// import StudentsEdit from '@/components/StudentEdit.vue'

const routes = [{
    path: '/',
    name:'home',
    component: HomeView
},{
    path:'/admin-view',
    name:'adminView',
    component: AdminView
},{
    path:'/login',
    name:'StudentSignUp',
    component: StudentSignUp
},
// {
//     path:'/studentsedit',
//     name:'StudentsEdit',
//     component:StudentsEdit
// }
]
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

export default router