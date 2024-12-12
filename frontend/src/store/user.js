import { defineStore } from "pinia";
export const userStore = defineStore("userStore", {
  state: () => ({
    responseData: JSON.parse(localStorage.getItem("responseData")) || {},
  }),
  getters: {
    // Getter to access myData
    getResponseData: (state) => state.responseData,
  },
  actions: {
    setResponseData(data) {
      this.responseData = data;
      localStorage.setItem("responseData", JSON.stringify(data)); // Save to localStorage
    },
    logout() {
      this.responseData = {}; // Reset state
      localStorage.removeItem("responseData"); // Clear from localStorage
    },
  },
});
