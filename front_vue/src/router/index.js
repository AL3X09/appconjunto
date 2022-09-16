import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '../views/IndexView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
//import TableroView from '../views/RegisterView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index',
      component: IndexView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/registar',
      name: 'registrar',
      component: RegisterView,
    },
   ]
    /*{
      path: '/tablero',
      name: 'tablero',
      component: TebleroView,
      children: [
        { path: "", name: "Index", component: () => import("./views/Home") },
        { path: "financiera", name: "Index", component: () => import("./views/Home") },
        { path: "parquedero", name: "Index", component: () => import("./views/Home") },
        { path: "paquete", name: "Index", component: () => import("./views/Home") },
        { path: "portafolio", name: "Index", component: () => import("./views/Home") },
        { path: "arriendopropiedad", name: "Index", component: () => import("./views/Home") },
        { path: "ventaspropiedad", name: "Index", component: () => import("./views/Home") },
        { path: "quejas", name: "Index", component: () => import("./views/Home") },
        { path: "saloncomunal", name: "Index", component: () => import("./views/Home") },
        { path: "salabbq", name: "Index", component: () => import("./views/Home") },
        { path: "visitante", name: "Index", component: () => import("./views/Home") },
        { path: "camaras", name: "Index", component: () => import("./views/Home") },
        { path: "administrar", name: "Index", component: () => import("./views/Home") },
      ]
    },
    {
      path: '/noticia/id',
      component: NoticiaView,
    },
  ]*/
})

export default router
