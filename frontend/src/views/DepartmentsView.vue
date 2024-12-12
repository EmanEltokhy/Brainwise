<template>
  <v-breadcrumbs :items="items" class="pl-16">
    <template v-slot:prepend>
      <v-icon size="small" icon="$vuetify" class="pl-16"></v-icon>
    </template>
  </v-breadcrumbs>
  <v-container fluid class="bg-grey-lighten-3">
    <div class="text-left mb-6 text-teal text-h4">
      {{ selectedCompany.name }} Company
    </div>
    <v-row>
      <v-img :src="getImgUrl()" class="mx-5" height="30%" conatin></v-img>
      <v-card class="align-start pa-6" rounded="lg" width="40%" justify-center>
        <div class="text-left mb-6 text-teal text-h6">Basic information</div>
        <v-item-group mandatory>
          <v-column class="justify-center">
            <v-card-text class="pl-1 text-start ml-3">
              <div class="text-h7">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy
                text ever since the 1500s, when an unknown printer took a galley
                of type and scrambled it to make a type specimen book. It has
                survived not only five centuries, but also the leap into
                electronic typesetting, remaining essentially unchanged. It was
                popularised in the 1960s with the release of Letraset sheets
                containing Lorem Ipsum passages, and more recently with desktop
                publishing software like Aldus PageMaker including versions of
                Lorem Ipsum.[as description for company]
              </div>
            </v-card-text>
            <v-card-text class="pl-1 text-start ml-3">
              <div class="text-h7 font-weight-bold">
                No. of departments: {{ selectedCompany.number_of_departments }}
              </div>
              <div class="text-h7 font-weight-bold">
                No. of employees: {{ selectedCompany.number_of_employees }}
              </div>
            </v-card-text>
          </v-column>
        </v-item-group>
      </v-card>
    </v-row>

    <v-row class="pt-10 justify-start">
      <v-col cols="12">
        <v-card class="mx-auto align-start pa-6" rounded="lg" height="100%">
          <div class="text-left mb-6 text-teal text-h5">Departments</div>

          <v-row class="justify-start">
            <v-col
              v-for="department in departments"
              :key="department.id"
              cols="12"
              md="4"
            >
              <departments-card
                :name="department.name"
                :id="department.id"
                :numOfEmp="department.number_of_employees"
                :company="department.company"
              />
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onBeforeMount } from "vue";
import router from "@/router";
import { useApiStore } from "@/store/api";
import DepartmentsCard from "@/components/DepartmentsCard.vue";
const apiRequest = useApiStore();
const selectedCompany = ref({});
const selectedId = ref(null);
const departments = ref([]);

const items = ref([
  { title: "Dashboard", disabled: false, href: "/dashboard" },
  { title: "Companies", disabled: false, href: "/Companies" },
  { title: "Departments", disabled: true, href: "breadcrumbs_link_2" },
]);

const getImgUrl = () => {
  var images = require.context("../assets/", false);
  return images("./company.jpeg");
};
const getCompanyById = () => {
  apiRequest
    .makeApiCall(`/companies/companies/${selectedId.value}/`, "GET")
    .then((response) => response.json())
    .then((data) => {
      selectedCompany.value = data;
    })
    .catch((error) => {
      console.log(error);
    });
};
const departmentsData = () => {
  apiRequest
    .makeApiCall(`/departments/departments/byId/?id=${selectedId.value}`, "GET")
    .then((response) => response.json())
    .then((data) => {
      departments.value = data;
      console.log("departments", departments.value);
    })
    .catch((error) => {
      console.log(error);
    });
};
onBeforeMount(async () => {
  const id = router.currentRoute.value.params.name;
  console.log("company eman", router.currentRoute.value.params.company);
  console.log("company eman", router.currentRoute.value.params);

  selectedId.value = id;
  if (id != "none") {
    getCompanyById(parseInt(id));
    departmentsData();
  }
});
</script>
