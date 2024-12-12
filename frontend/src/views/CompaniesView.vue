<template>
  <v-container fluid class="bg-grey-lighten-3">
    <v-row v-if="isLoaded" class="pt-16 justify-center">
      <v-col
        v-for="(company, key) in companies"
        :key="key"
        cols="12"
        md="2"
        style="height: 100%"
      >
        <services-card
          :title="company.name"
          :id="company.id"
          image-src="company.jpeg"
          :numOfDep="company.number_of_departments"
          :numOfEmp="company.number_of_employees"
          :role="userApi.responseData.role"
        />
      </v-col>
    </v-row>
    <v-row v-else justify-center>
      <v-col cols="12" class="text-center">
        <v-progress-circular
          indeterminate
          color="primary"
        ></v-progress-circular>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import ServicesCard from "@/components/ServicesCard.vue";
import { onBeforeMount, ref } from "vue";
import { useApiStore } from "@/store/api";
import { userStore } from "@/store/user";
const userApi = userStore();
const apiRequest = useApiStore();
const companies = ref({});

let isLoaded = ref(false);
const companiesData = () => {
  apiRequest
    .makeApiCall(`/companies/companies/`, "GET")
    .then((response) => response.json())
    .then((data) => {
      companies.value = data;
      isLoaded.value = true;
    })
    .catch((error) => {
      console.log(error);
      isLoaded.value = false;
    });
};

const userData = () => {
  apiRequest
    .makeApiCall(`/accounts/users/me/`, "GET")
    .then((response) => response.json())
    .then((data) => {
      // console.log(data);
      userApi.setResponseData(data);
      console.log("userapi", userApi.responseData);
    })
    .catch((error) => {
      console.log(error);
    });
};
onBeforeMount(async () => {
  userData();
  companiesData();
});
</script>

<style>
#donation .v-img__img--contain {
  padding: 10px;
}
</style>
