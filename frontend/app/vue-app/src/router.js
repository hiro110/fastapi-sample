import { createRouter, createWebHistory } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue';
import AdminHome from './components/admin/Home.vue';

const routes = [
    { path: '/', component: HelloWorld },
    { path: '/admin', component: AdminHome },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router;
