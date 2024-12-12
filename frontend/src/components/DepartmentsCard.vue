<template>
  <message-display
    :show="snack.displayMessage"
    :message="snack.message"
    :color="snack.messageColor"
  ></message-display>
  <v-card
    class="mx-auto mb-3 d-flex flex-column position-relative pa-3"
    rounded="lg"
    style="background-color: #f4f1fa"
    @click="cardClick"
  >
    <!-- Icons Overlay -->
    <div
      v-if="!isEditing"
      class="position-absolute d-flex justify-end pa-2 w-100"
      style="z-index: 2"
    >
      <v-icon class="mr-2" style="cursor: pointer" @click.stop="editItem"
        >mdi-pencil</v-icon
      >
      <v-icon
        class="mr-2"
        style="cursor: pointer; color: red"
        @click.stop="confirmDelete"
        >mdi-delete</v-icon
      >
    </div>
    <div
      v-else
      class="position-absolute d-flex justify-end pa-2 w-100"
      style="z-index: 2"
    >
      <v-icon
        class="mr-2"
        style="cursor: pointer; color: green"
        @click.stop="Done"
        >mdi-check-circle</v-icon
      >
    </div>

    <div v-if="!isEditing">
      <div class="text-h5 mt-2 text-teal pt-8">{{ props.name }} Department</div>
    </div>
    <div v-else>
      <v-text-field
        v-model="editableTitle"
        label="Edit Name of Department"
        class="text-h5"
      ></v-text-field>
    </div>
    <v-card-text class="pl-1 text-start ml-3">
      <div class="text-h7">No. of employees: {{ props.numOfEmp }}</div>
    </v-card-text>
  </v-card>

  <!-- Confirmation Dialog -->
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
</template>

<script setup>
import { defineProps, ref } from "vue";
import { useApiStore } from "@/store/api";
import { userStore } from "@/store/user";
import router from "@/router";
import MessageDisplay from "@/components/MessageDisplay.vue";
const userApi = userStore();
const apiRequest = useApiStore();
const snack = ref({
  displayMessage: false,
  message: {},
  messageColor: "",
});
// Define props and methods in the setup function
const props = defineProps(["name", "id", "numOfEmp", "company"]);

const isEditing = ref(false); // Track if the title is being edited
const isClick = ref(false); // Track if the title is being edited

const editableTitle = ref(""); // Bind the editable title to this property
const canEditOrDelete = () => {
  return (
    userApi.responseData.role === "admin" ||
    userApi.responseData.role === "manager"
  );
};

// New reactive variable for the dialog visibility
const dialogVisible = ref(false); // Controls dialog visibility

const editItem = () => {
  if (!canEditOrDelete()) {
    showMessage("You do not have permission to do this", "error");
    return;
  } // Safety check
  isEditing.value = true;
  isClick.value = true;
};

// Trigger the confirmation dialog
const confirmDelete = () => {
  if (!canEditOrDelete()) {
    showMessage("You do not have permission to do this", "error");
    return;
  } // Safety check
  dialogVisible.value = true; // Show confirmation dialog
};
const cardClick = () => {
  if (isClick.value) {
    console.log("not press");
  } else {
    console.log("inside ekse");
    if (router) {
      router.push({ name: "utilities", params: { name: props.id } });
    }
  }
};
const deleteItem = () => {
  console.log("Deleting item...");
  isClick.value = true;
  apiRequest
    .makeApiCall(`/departments/departments/${props.id}/`, "DELETE")
    .then(() => {
      window.location.reload(); // Reload companies list after delete
      isClick.value = false;
    })
    .catch((error) => {
      console.log(error);
    });
};
const Done = () => {
  console.log("Editing item...");
  isClick.value = true;
  console.log(editableTitle.value);
  const body = {
    name: editableTitle.value,
    company: props.company,
  };
  apiRequest
    .makePostorPutApiCall(`/departments/departments/${props.id}/`, body, "PUT")
    .then((response) => response.json())
    .then(() => {
      isEditing.value = false;
      isClick.value = false;
      window.location.reload(); // Reload companies list after delete
    })
    .catch((error) => {
      console.log(error);
    });
};
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
