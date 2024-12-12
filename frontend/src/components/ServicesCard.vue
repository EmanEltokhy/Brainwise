<template>
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
    class="mx-auto mb-3 d-flex flex-column position-relative"
    rounded="lg"
    max-height="20%"
    height="100%"
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

    <!-- Image Section -->
    <v-img
      :src="getImgUrl()"
      class="w-100"
      max-height="150"
      height="auto"
      contain
      style="z-index: 1"
    ></v-img>

    <div v-if="!isEditing">
      <div class="text-h5 mt-2 text-teal">{{ props.title }} Company</div>
    </div>
    <div v-else>
      <v-text-field
        v-model="editableTitle"
        label="Edit Title of The Company"
        class="text-h5"
      ></v-text-field>
    </div>
    <v-card-text class="pl-1 text-start ml-3">
      <div class="text-h7">No. of departments: {{ props.numOfDep }}</div>
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
import MessageDisplay from "@/components/MessageDisplay.vue";
import router from "@/router";
const apiRequest = useApiStore();

// Define props and methods in the setup function
const props = defineProps([
  "title",
  "id",
  "numOfDep",
  "numOfEmp",
  "role",
  "imageSrc",
]);
const snack = ref({
  displayMessage: false,
  message: {},
  messageColor: "",
});
const isEditing = ref(false); // Track if the title is being edited
const isClick = ref(false); // Track if the title is being edited

const editableTitle = ref(""); // Bind the editable title to this property
const canEditOrDelete = () => {
  console.log("role", props.role);
  return props.role === "admin" || props.role === "manager";
};
const getImgUrl = () => {
  var images = require.context("../assets/", false);
  return images("./" + props.imageSrc);
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
      router.push({
        name: "recharge",
        params: {
          name: props.id,
        },
      });
    }
  }
};
const deleteItem = () => {
  console.log("Deleting item...");
  isClick.value = true;
  apiRequest
    .makeApiCall(`/companies/companies/${props.id}/`, "DELETE")
    .then((response) => {
      console.log("res", response);
      if (!response.ok) {
        // Assuming server returns a JSON error message
        return Promise.reject(
          new Error(
            response.status == 500
              ? "Please delete the associated data of the removed item"
              : `Error: ${response.status}`
          )
        );
      }

      isClick.value = false;
      window.location.reload();
    })
    .catch((error) => {
      console.log("error", error);
      dialogVisible.value = false;
      showMessage(error, "error");
    });
};
const Done = () => {
  console.log("Editing item...");
  isClick.value = true;
  console.log(editableTitle.value);
  const body = {
    name: editableTitle.value,
  };
  apiRequest
    .makePostorPutApiCall(`/companies/companies/${props.id}/`, body, "PUT")
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
