import { createRouter, createWebHistory } from "vue-router";
import Cookies from "js-cookie";

const routes = [
  {
    path: "/",
    name: "home",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/HomeView.vue"),
  },
  {
    path: "/about",
    name: "about",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/profile",
    name: "profile",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/ProfileView.vue"),
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/DashboardView.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/companies",
    name: "companies",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/CompaniesView.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/companies/recharge/:name",
    name: "recharge",
    props: true,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/DepartmentsView.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/companies/recharge/employees/:name",
    name: "utilities",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/EmployeesView.vue"),
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});
router.beforeEach((to, from, next) => {
  let isAuthenticated = null;
  const auth = Cookies.get("token");
  if (auth != undefined) {
    isAuthenticated = true;
  }

  if (to.meta.requiresAuth && !isAuthenticated) {
    // If the route requires authentication and the user is not authenticated, redirect to the login page
    next("/");
  } else {
    // Continue with the navigation
    next();
  }
});
export default router;
