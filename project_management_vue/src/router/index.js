import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

import {store} from '../store'
import SignUpView from "@/views/SignUpView";
import LogInView from "@/views/LogInView";
import Dashboard from "@/views/dashboard/Dashboard";
import MyAccount from "@/views/dashboard/MyAccount";
import Projects from "@/views/dashboard/Project/Projects";
import AddProject from "@/views/dashboard/Project/AddProject";
import Project from "@/views/dashboard/Project/Project";
import EditProject from "@/views/dashboard/Project/EditProject";
import AddDepartment from "@/views/dashboard/Department/AddDepartment";
import Department from "@/views/dashboard/Department/Department";
import AddEmployee from "@/views/dashboard/Employee/AddEmployee";
import Clients from "@/views/dashboard/Client/Clients";
import AddClient from "@/views/dashboard/Client/AddClient";
import EditClient from "@/views/dashboard/Client/EditClient";
import AddTask from "@/views/dashboard/Task/AddTask";
import EditTask from "@/views/dashboard/Task/EditTask";
import Task from "@/views/dashboard/Task/Task";
import EditEmployee from "@/views/dashboard/Employee/EditEmployee";
import MyTasks from "@/views/dashboard/Task/MyTasks";
import testing_porjects from "@/views/dashboard/Project/testing_porjects";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUpView
    },

    {
        path: '/login',
        name: 'Login',
        component: LogInView
    },

    {
        path: '/dashboard',
        name: 'Dashboard',
        component: Dashboard,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/my-account',
        name: 'MyAccount',
        component: MyAccount,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/projects',
        name: 'Projects',
        component: Projects,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/test',
        name: 'testing_projects',
        component: testing_porjects,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/projects/add',
        name: 'AddProject',
        component: AddProject,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/projects/:id',
        name: 'Project',
        component: Project,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/projects/:id/edit',
        name: 'EditProject',
        component: EditProject,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/add-department',
        name: 'AddDepartment',
        component: AddDepartment,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/department',
        name: 'Department',
        component: Department,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/department/add-employee',
        name: 'AddEmployee',
        component: AddEmployee,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/clients/',
        name: 'Clients',
        component: Clients,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/clients/add',
        name: 'AddClient',
        component: AddClient,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/clients/:id/edit',
        name: 'EditClient',
        component: EditClient,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/projects/:id/add-task',
        name: 'AddTask',
        component: AddTask,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/projects/:id/edit-task/:task_id',
        name: 'EditTask',
        component: EditTask,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/projects/:id/task/:task_id',
        name: 'Task',
        component: Task,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/edit-employee/:id',
        name: 'EditEmployee',
        component: EditEmployee,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/my-tasks',
        name: 'MyTasks',
        component: MyTasks,
        meta: {
            requireLogin: true
        }
    },


    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

router.beforeEach((to, from, next) =>{
  if (to.matched.some(record =>record.meta.requireLogin) && !store.state.isAuthenticated){
    next("/login")
  }else{
    next()
  }
})


export default router
