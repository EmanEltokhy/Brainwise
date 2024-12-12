<template>
  <v-container fluid class="bg-grey-lighten-3 mt-10">
    <v-col>
      <v-container class="pa-16">
        <div class="text-h4 text-center text-teal font-weight-bold mb-5">
          Welcome to our Employee Management System
        </div>
        <div class="text-h6 text-center text-teal">
          Experience the convenience of digital Management.
        </div>
      </v-container>
      <v-card
        class="mx-auto mb-3"
        elevation="0"
        max-width="448"
        rounded="lg"
        color="white"
      >
        <message-display
          :show="snack.displayMessage"
          :message="snack.message"
          :color="snack.messageColor"
        ></message-display>
      </v-card>
      <v-card
        class="mx-auto pa-12 pb-8 mb-16"
        elevation="8"
        max-width="448"
        rounded="lg"
      >
        <div class="text-h3 text-left mb-12">Log In</div>

        <v-text-field
          placeholder="Enter Email"
          prepend-inner-icon="mdi-email"
          variant="outlined"
          label="Email"
          v-model="email"
          color="teal"
        ></v-text-field>
        <v-text-field
          :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
          :type="visible ? 'text' : 'password'"
          placeholder="Enter your password"
          prepend-inner-icon="mdi-lock-outline"
          variant="outlined"
          label="Password"
          v-model="password"
          color="teal"
          @click:append-inner="visible = !visible"
        ></v-text-field>
        <v-btn block class="mb-8" color="teal" size="large" @click="loginFun">
          Log In
        </v-btn>
      </v-card>
    </v-col>
  </v-container>
  <v-container fluid class="bg-grey-lighten-2 text-light text-center py-5">
    <v-col>
      <h2 class="mb-16 text-teal font-weight-regular">Key Features</h2>
      <v-row justify="center" class="my-4 text-center">
        <v-card
          class="mx-2 mb-16"
          max-width="344"
          v-for="(card, id) in cards"
          :key="id"
        >
          <v-img :src="card.img" height="200px" cover></v-img>

          <v-card-title> {{ card.title }} </v-card-title>
          <v-card-text>
            {{ card.body }}
          </v-card-text>
        </v-card>
      </v-row>
    </v-col>
  </v-container>
</template>

<script setup>
import Cookies from "js-cookie";
import MessageDisplay from "@/components/MessageDisplay.vue";
import { ref } from "vue";
import router from "@/router";
import { useApiStore } from "@/store/api";
import { userStore } from "@/store/user";
const userApi = userStore();

const apiRequest = useApiStore();
const email = ref("");
const password = ref("");
const visible = ref(false);
const snack = ref({
  displayMessage: false,
  message: {},
  messageColor: "",
});
const cards = ref([
  {
    title: "Employee Management",
    body: "Manage employee records, track performance, and monitor their progress across departments.",
    img: require("@/assets/employee-management.jpeg"),
  },
  {
    title: "Department Organization",
    body: "Easily manage department structures, assign roles, and track departmental performance.",
    img: require("@/assets/department-organization.jpeg"),
  },
  {
    title: "Company Overview",
    body: "Get a comprehensive overview of your company, track employee distribution, and monitor company-wide progress.",
    img: require("@/assets/company-overview.jpg"),
  },
]);

const loginFun = async () => {
  const data = {
    email: email.value,
    password: password.value,
  };
  apiRequest
    .makePostApiCallHome("/accounts/api/token/", data)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      Cookies.set("token", data.access, { secure: true });
      Cookies.set("refresh", data.access, { secure: true });

      console.log("here", Cookies.get("token"));
      if (Cookies.get("token") == undefined) {
        showMessage(data, "error");
      } else {
        showMessage("Succesfully Login", "success");
        userApi.islogin = true;
        router.push("dashboard");
      }
    })
    .catch((error) => {
      showMessage(error, "error");
    });
};

const showMessage = (message, color) => {
  snack.value.displayMessage = true;
  snack.value.message = message;
  snack.value.messageColor = color;

  setTimeout(() => {
    snack.value.displayMessage = false;
    snack.value.message = {};
    snack.value.messageColor = "";
  }, 3000);
};
</script>
