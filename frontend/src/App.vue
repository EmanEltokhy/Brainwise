<template>
  <v-app>
    <v-app-bar app color="teal" class="mb-10" v-if="$route.path != '/'">
      <!-- <v-container> -->
      <v-row>
        <v-col>
          <!-- <div> -->
          <v-icon size="x-large" class="px-4">mdi-home</v-icon>
          <router-link
            class="text-none text-white pb-5"
            style="text-decoration: none"
            to="/dashboard"
            >Go to Home</router-link
          >
          <!-- </div> -->
        </v-col>
        <v-col></v-col>
        <v-col></v-col>
        <v-col align="end" class="text-right">
          <v-menu open-on-hover>
            <template v-slot:activator="{ props }">
              <v-btn v-on="on" v-bind="props">
                <v-icon size="x-large" class="px-4">mdi-account-circle</v-icon>
                {{ userApi.responseData.username }}
                <v-icon size="x-large" class="px-4">mdi-menu-down</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item @click="navigateTo('/profile')">
                <v-list-item-content>
                  <v-icon>mdi-account</v-icon>
                  My Profile
                </v-list-item-content>
              </v-list-item>
              <v-list-item @click="navigateTo('/dashboard')">
                <v-list-item-content>
                  <v-icon>mdi-view-dashboard</v-icon>
                  My Dashboard
                </v-list-item-content>
              </v-list-item>
              <div class="item mx-2"></div>
              <v-list-item @click="logout">
                <v-list-item-content style="color: red">
                  <v-icon>mdi-logout</v-icon>
                  Logout
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-col>
      </v-row>
    </v-app-bar>
    <v-app-bar app color="teal" class="mb-10" v-else></v-app-bar>
    <v-main>
      <v-toolbar color="white" elevation="4">
        <v-img
          :src="require('@/assets/brainwise.png')"
          width="60px"
          height="60"
        ></v-img>
        <!-- Navigation links -->
        <v-spacer></v-spacer>
        <v-toolbar-items class="mr-16" v-if="$route.path != '/'">
          <v-container class="mr-8">
            <router-link class="text-none text-teal mx-5" to="/dashboard"
              >Home</router-link
            >
            <router-link class="text-none text-teal mr-5" to="/companies"
              >Companies</router-link
            >
            <router-link class="text-none text-teal mr-5" to="/about"
              >About</router-link
            >
          </v-container>
        </v-toolbar-items>
      </v-toolbar>
      <router-view />
    </v-main>
    <v-footer color="teal">
      <v-row justify="center" class="my-4 text-center">
        <v-col cols="12">
          <v-row align="center" justify="center">
            <router-link to="about" class="px-5 text-white text-decoration-none"
              >About</router-link
            >
            <v-divider
              class="border-opacity-100"
              color="white"
              vertical
            ></v-divider>
            <v-divider
              class="border-opacity-100"
              color="white"
              vertical
            ></v-divider>
            <v-divider
              class="border-opacity-100"
              color="white"
              vertical
            ></v-divider>
            <router-link to="about" class="px-5 text-white text-decoration-none"
              >Store Locator</router-link
            >
            <v-divider
              class="border-opacity-100"
              color="white"
              vertical
            ></v-divider>
            <v-divider
              class="border-opacity-100"
              color="white"
              vertical
            ></v-divider>
            <v-divider
              class="border-opacity-100"
              color="white"
              vertical
            ></v-divider>
            <router-link to="about" class="px-5 text-white text-decoration-none"
              >Help & Support</router-link
            >
          </v-row>
        </v-col>
        <v-col cols="12"
          >&copy; 2024 Management Website. All rights reserved.</v-col
        >
      </v-row>
    </v-footer>
  </v-app>
</template>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap");
#app {
  font-family: "Poppins", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30em;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
.item {
  border-bottom: 1px solid black;
}
</style>
<script setup>
import { userStore } from "@/store/user";
import router from "@/router";
const userApi = userStore();
const navigateTo = (route) => {
  router.push(route);
};
const logout = () => {
  document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
  userApi.logout();
  router.push("/");
};
</script>
