<template>
  <message-display
    :show="snack.displayMessage"
    :message="snack.message"
    :color="snack.messageColor"
  ></message-display>

  <div class="employee-card">
    <!-- Header -->
    <div class="employee-header">
      <i class="mdi mdi-account-circle employee-icon"></i>
      <h2 v-if="!isEditing" class="employee-name">{{ employee.name }}</h2>
      <input
        v-else
        class="employee-input"
        v-model="editableEmployee.name"
        placeholder="Name"
      />
      <i
        class="mdi mdi-pencil employee-edit-icon"
        @click="toggleEditMode"
        title="Edit"
      ></i>
      <i
        class="mdi mdi-delete employee-delete-icon"
        @click="confirmDelete"
        title="Delete"
      ></i>
    </div>

    <!-- Employee Details -->
    <div v-for="field in fields" :key="field.key" class="employee-detail">
      <i :class="field.icon + ' employee-icon'"></i>
      <p class="detail-label">{{ field.label }}</p>

      <template v-if="!isEditing">
        <p class="employee-info">{{ employee[field.key] }}</p>
      </template>

      <template v-else>
        <input
          class="employee-input"
          v-model="editableEmployee[field.key]"
          :placeholder="field.label"
        />
      </template>
    </div>

    <!-- Action Buttons -->
    <div v-if="isEditing" class="employee-actions">
      <button class="btn-save" @click="saveChanges">Save</button>
      <button class="btn-cancel" @click="cancelChanges">Cancel</button>
    </div>
    <v-dialog v-model="dialogVisible" max-width="400px">
      <v-card>
        <v-card-title class="headline">Are you sure?</v-card-title>
        <v-card-text>Do you really want to delete this company?</v-card-text>
        <v-card-actions>
          <v-btn text @click="dialogVisible = false">Cancel</v-btn>
          <v-btn color="red" @click="deleteItem">Delete</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup>
import { ref, watch, defineProps, reactive } from "vue";
import { useApiStore } from "@/store/api";
import { userStore } from "@/store/user";
import MessageDisplay from "@/components/MessageDisplay.vue";
const userApi = userStore();

const apiRequest = useApiStore();
const dialogVisible = ref(false);

// Props
const props = defineProps({
  employee: {
    type: Object,
    required: true,
  },
});
const snack = ref({
  displayMessage: false,
  message: {},
  messageColor: "",
});

// Reactive state
const isEditing = ref(false);

const editableEmployee = reactive({ ...props.employee });
const fields = [
  { key: "status", label: "Status:", icon: "mdi mdi-briefcase" },
  { key: "address", label: "Address:", icon: "mdi mdi-home-map-marker" },
  {
    key: "designation",
    label: "Designation:",
    icon: "mdi mdi-briefcase-check",
  },
  { key: "hired_on", label: "Hiring Date:", icon: "mdi mdi-calendar-check" },
  { key: "mobile_number", label: "Mobile:", icon: "mdi mdi-phone" },
  { key: "email", label: "Email:", icon: "mdi mdi-email" },
];
const canEditOrDelete = () => {
  console.log(userApi.responseData.role);
  return (
    userApi.responseData.role === "admin" ||
    userApi.responseData.role === "manager"
  );
};
// Methods
const toggleEditMode = () => {
  if (!canEditOrDelete()) {
    showMessage("You do not have permission to do this", "error");
    return;
  } // Safety check
  isEditing.value = !isEditing.value;
  if (!isEditing.value) cancelChanges(); // Reset on cancel
};
const confirmDelete = () => {
  console.log(canEditOrDelete());
  if (!canEditOrDelete()) {
    showMessage("You do not have permission to do this", "error");
    return;
  } // Safety check// Safety check
  dialogVisible.value = true; // Show confirmation dialog
  console.log(dialogVisible.value);
};
const deleteItem = () => {
  console.log("Deleting item...");
  apiRequest
    .makeApiCall(`/employees/users/${props.employee.id}/`, "DELETE")
    .then(() => {
      dialogVisible.value = false;
      window.location.reload();
    })
    .catch((error) => {
      console.log(error);
    });
};
const saveChanges = () => {
  apiRequest
    .makePostorPutApiCall(
      `/employees/users/${props.employee.id}/`,
      editableEmployee,
      "PUT"
    )
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to update employee");
      }
      return response.json();
    })
    .then((updatedEmployee) => {
      console.log(updatedEmployee);
      window.location.reload(); // Emit event to parent
      isEditing.value = false;
    })
    .catch((error) => {
      console.error(error);
      alert("Failed to save changes.");
    });
};

const cancelChanges = () => {
  Object.assign(editableEmployee, { ...props.employee }); // Reset to original data
  isEditing.value = false;
};

// Watch for prop changes
watch(
  () => props.employee,
  (newEmployee) => {
    Object.assign(editableEmployee, { ...newEmployee });
  },
  { immediate: true }
);

const showMessage = (message, color) => {
  console.log("inside show message");
  snack.value.displayMessage = true;
  snack.value.message = message;
  snack.value.messageColor = color;

  // Close the message after a certain duration
  setTimeout(() => {
    snack.value.displayMessage = false;
    snack.value.message = {};
    snack.value.messageColor = "";
  }, 3000);
};
</script>

<style scoped>
.employee-card {
  width: 400px;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  background-color: #ffffff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  font-family: "Roboto", sans-serif;
  color: #333;
}

.employee-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.employee-header .employee-icon {
  font-size: 28px;
  color: teal;
  margin-right: 15px;
}

.employee-name {
  font-size: 1.5rem;
  font-weight: 600;
  margin: 0;
  color: teal;
}

.employee-edit-icon {
  cursor: pointer;
  color: #6567fc;
  font-size: 20px;
}

.employee-delete-icon {
  cursor: pointer;
  color: red;
  font-size: 20px;
}

.employee-detail {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

.employee-detail .employee-icon {
  font-size: 24px;
  color: teal;
  margin-right: 15px;
}

.employee-detail .detail-label {
  font-weight: 500;
  color: #555;
  margin-right: 10px;
}
.detail-label {
  margin-right: 8px;
  font-weight: bold;
}

.employee-info {
  margin: 0;
  color: #444;
  font-weight: 400;
}

.employee-input {
  flex: 1;
  padding: 4px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.employee-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}
.employee-card .employee-detail p:last-child {
  color: teal; /* Highlighting the value in blue */
}
.btn-save {
  background-color: #28a745;
  color: #fff;
  border: none;
  padding: 8px 12px;
  border-radius: 4px;
  cursor: pointer;
}

.btn-cancel {
  background-color: #dc3545;
  color: #fff;
  border: none;
  padding: 8px 12px;
  border-radius: 4px;
  cursor: pointer;
}
</style>
