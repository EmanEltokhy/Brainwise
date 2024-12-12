<template>
  <v-breadcrumbs :items="items" class="pl-16">
    <template v-slot:prepend>
      <v-icon size="small" icon="$vuetify" class="pl-16"></v-icon>
    </template>
  </v-breadcrumbs>
  <v-container fluid class="bg-grey-lighten-3">
    <v-row class="pt-10 justify-start">
      <v-col cols="12">
        <v-card class="mx-auto align-start pa-6" rounded="lg" height="100%">
          <div class="text-left mb-6 text-teal text-h5">Employees</div>
          <div class="create-button" @click="toggleCreateForm">
            <i class="mdi mdi-plus-circle"></i> Create New Employee
          </div>
          <v-row class="justify-start">
            <v-col
              v-for="(employeeData, key) in employees"
              :key="key"
              cols="12"
              md="4"
            >
              <employees-card :employee="employeeData" />
            </v-col>
            <v-dialog v-model="isCreating" max-width="500px">
              <v-card>
                <v-card-title class="headline"
                  >Create New Employee</v-card-title
                >
                <v-card-text>
                  <!-- Create Employee Form -->
                  <v-form v-model="valid" ref="form">
                    <v-text-field
                      v-model="newEmployee.name"
                      label="Name"
                      :rules="[requiredRule, nameRules]"
                      required
                    ></v-text-field>

                    <v-text-field
                      v-model="newEmployee.email"
                      label="Email"
                      :rules="[requiredRule, emailRules]"
                      required
                    ></v-text-field>

                    <v-text-field
                      v-model="newEmployee.mobile_number"
                      label="Mobile"
                      :rules="[requiredRule, mobileRules]"
                      required
                    ></v-text-field>

                    <v-text-field
                      v-model="newEmployee.designation"
                      label="Designation"
                      :rules="[requiredRule]"
                      required
                    ></v-text-field>

                    <v-select
                      v-model="newEmployee.status"
                      :items="['onboarding', 'active', 'inactive']"
                      label="Status"
                      :rules="[requiredRule]"
                      required
                    ></v-select>

                    <v-text-field
                      v-model="newEmployee.address"
                      label="Address"
                      :rules="[requiredRule]"
                      required
                    ></v-text-field>

                    <v-text-field
                      v-model="newEmployee.hired_on"
                      label="Hiring Date"
                      :rules="[requiredRule, dateRules]"
                      required
                    ></v-text-field>
                  </v-form>
                </v-card-text>

                <v-card-actions>
                  <v-btn text @click="cancelCreate">Cancel</v-btn>
                  <v-btn
                    color="primary"
                    @click="createEmployee"
                    :disabled="!valid"
                    >Save</v-btn
                  >
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onBeforeMount, reactive } from "vue";
import router from "@/router";
import { useApiStore } from "@/store/api";
import EmployeesCard from "@/components/EmployeesCard.vue";
import { userStore } from "@/store/user";
const userApi = userStore();
const apiRequest = useApiStore();
const selectedId = ref(null);
const employees = ref([]);
const isCreating = ref(false);
const valid = ref(false);
const form = ref(null);

const newEmployee = reactive({
  company: "",
  department: "",
  name: "",
  status: "",
  address: "",
  mobile_number: "",
  email: "",
  designation: "",
  hired_on: "",
});
const items = ref([
  { title: "Dashboard", disabled: false, href: "/dashboard" },
  { title: "Companies", disabled: false, href: "/services" },
  {
    title: "Departments",
    disabled: false,
    href: "javascript:history.back()",
  },
  { title: "Employees", disabled: true, href: "breadcrumbs_link_2" },
]);
const requiredRule = (v) => !!v || "This field is required";

const emailRules = (v) => /.+@.+\..+/.test(v) || "E-mail must be valid";
const mobileRules = (v) =>
  /^\d{11}$/.test(v) || "Mobile number must be 10 digits";

const nameRules = (v) => v.length >= 3 || "Name must be at least 3 characters";
const dateRules = (v) =>
  /^\d{4}-\d{2}-\d{2}$/.test(v) || "Date must be in yyyy-mm-dd format";
const canEditOrDelete = () => {
  console.log(userApi.responseData.role);
  return (
    userApi.responseData.role === "admin" ||
    userApi.responseData.role === "manager"
  );
};
const employeesData = () => {
  apiRequest
    .makeApiCall(`/employees/users/byId/?id=${selectedId.value}`, "GET")
    .then((response) => response.json())
    .then((data) => {
      employees.value = data;
    })
    .catch((error) => {
      console.log(error);
    });
};
onBeforeMount(async () => {
  const id = router.currentRoute.value.params.name;

  selectedId.value = id;
  if (id != "none") {
    employeesData();
  }
});
const toggleCreateForm = () => {
  if (!canEditOrDelete()) {
    // showMessage("You do not have permission to create an employee", "error");
    return;
  }
  isCreating.value = !isCreating.value;
};
const cancelCreate = () => {
  Object.assign(newEmployee, {
    company: "",
    department: "",
    name: "",
    status: "",
    address: "",
    mobile_number: "",
    email: "",
    designation: "",
    hired_on: "",
  }); // Reset form
  isCreating.value = false;
};
const createEmployee = () => {
  form.value.validate();
  if (!valid.value) {
    return;
  }

  newEmployee.company = employees.value[0].company;
  newEmployee.department = employees.value[0].department;
  console.log("newemployee", newEmployee);
  apiRequest
    .makePostorPutApiCall("/employees/users/", newEmployee, "POST")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to create employee");
      }
      return response.json();
    })
    .then((createdEmployee) => {
      console.log("Employee created:", createdEmployee);
      isCreating.value = false;
      window.location.reload();
    })
    .catch((error) => {
      console.error(error);
      alert("Failed to create employee.");
    });
};
</script>
<style>
.create-button {
  cursor: pointer;
  background-color: teal;
  color: white;
  padding: 10px 15px;
  border-radius: 5px;
  position: absolute;
  right: 20px;
  top: 20px;
  width: auto;
}
.v-dialog__content {
  width: 500px;
  padding: 20px;
  border-radius: 8px;
  background-color: #ffffff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.v-dialog .v-card-title {
  font-size: 1.5rem;
  font-weight: bold;
  color: #333;
  margin-bottom: 20px;
}

.v-form {
  display: flex;
  flex-direction: column;
}

.v-text-field,
.v-select {
  margin-bottom: 15px;
}

.v-text-field .v-input__control,
.v-select .v-input__control {
  border-radius: 4px;
  border: 1px solid #ddd;
}

.v-text-field label,
.v-select label {
  font-weight: 500;
  color: #555;
}

.v-text-field .v-label,
.v-select .v-label {
  font-size: 1rem;
}

.v-text-field .v-input__control .v-input__slot {
  color: #444;
}

.v-btn {
  border-radius: 4px;
  padding: 8px 16px;
  font-weight: bold;
}

.v-btn--text {
  background-color: transparent;
  color: #00796b;
}

.v-btn--text:hover {
  background-color: #f1f1f1;
}

.v-btn--primary {
  background-color: #28a745;
  color: white;
}

.v-btn--primary:hover {
  background-color: #218838;
}

.v-btn--red {
  background-color: #dc3545;
  color: white;
}

.v-btn--red:hover {
  background-color: #c82333;
}

.v-card-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}
</style>
