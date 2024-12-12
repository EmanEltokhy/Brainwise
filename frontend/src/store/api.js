// // stores/apiStore.js
// import { defineStore } from "pinia";
// import Cookies from "js-cookie";

// export const useApiStore = defineStore({
//   id: "api",
//   state: () => ({
//     baseUrl: "http://127.0.0.1:8000",
//     BillBaseUrl: "http://127.0.0.1:4000",
//     auth: Cookies.get("token"),
//   }),

//   actions: {
//     async makeApiCall(endpoint, method) {
//       //   try {
//       const url = this.baseUrl + endpoint;
//       console.log("token", this.auth);
//       await this.waitForAuthToken();
//       return await fetch(url, {
//         method: method,
//         headers: {
//           Authorization: `Bearer ${this.auth}`,
//         },
//         credentials: "same-origin",
//         // body: data,
//       });
//     },
//     async waitForAuthToken() {
//       if (!this.auth) {
//         // If auth is not available, try fetching it from cookies
//         this.auth = Cookies.get("token");

//         // Wait until the token is set
//         await new Promise((resolve) => {
//           const interval = setInterval(() => {
//             if (this.auth) {
//               clearInterval(interval); // Stop checking once the token is available
//               resolve();
//             }
//           }, 100); // Check every 100ms
//         });
//       }
//     },
//     async makePostApiCall(endpoint, data) {
//       const url = this.baseUrl + endpoint;
//       return await fetch(url, {
//         method: "Post",
//         headers: {
//           Authorization: `Bearer ${this.auth}`,
//           "Content-Type": "application/json",
//         },
//         credentials: "same-origin",
//         body: JSON.stringify(data),
//       });
//     },
//     async makePostApiCallHome(endpoint, data) {
//       const url = this.baseUrl + endpoint;
//       return await fetch(url, {
//         method: "Post",
//         headers: {
//           "Content-Type": "application/json",
//         },
//         credentials: "same-origin",
//         body: JSON.stringify(data),
//       });
//     },
//     async BillApi(endpoint) {
//       console.log("bill api");
//       const url = this.BillBaseUrl + endpoint;
//       console.log(url);
//       return await fetch(url, {
//         method: "GET",
//         headers: {
//           "Content-Type": "application/json",
//         },
//       });
//     },
//   },
// });
// stores/apiStore.js
import { defineStore } from "pinia";
import Cookies from "js-cookie";

export const useApiStore = defineStore({
  id: "api",
  state: () => ({
    baseUrl: "http://127.0.0.1:8000",
    BillBaseUrl: "http://127.0.0.1:4000",
    auth: Cookies.get("token"),
    refreshToken: Cookies.get("refresh"), // Assuming the refresh token is also stored in cookies
  }),

  actions: {
    async makeApiCall(endpoint, method) {
      // Wait for the auth token if it's not available
      await this.waitForAuthToken();

      const url = this.baseUrl + endpoint;
      console.log("token", this.auth);

      const response = await fetch(url, {
        method: method,
        headers: {
          Authorization: `Bearer ${this.auth}`,
        },
        credentials: "same-origin",
      });

      // If the token has expired (401), attempt to refresh it
      if (response.status === 401) {
        const refreshed = await this.refreshToken();
        if (refreshed) {
          // Retry the original request with the new token
          return await fetch(url, {
            method: method,
            headers: {
              Authorization: `Bearer ${this.auth}`,
            },
            credentials: "same-origin",
          });
        } else {
          // If refreshing the token fails, return an error or redirect to login
          console.log("Failed to refresh the token");
          return response;
        }
      }

      return response;
    },

    async waitForAuthToken() {
      if (!this.auth) {
        // If auth is not available, try fetching it from cookies
        this.auth = Cookies.get("token");

        // Wait until the token is set
        await new Promise((resolve) => {
          const interval = setInterval(() => {
            if (this.auth) {
              clearInterval(interval); // Stop checking once the token is available
              resolve();
            }
          }, 100); // Check every 100ms
        });
      }
    },

    async refreshToken() {
      const url = `${this.baseUrl}/api/token/refresh/`; // Your API endpoint for refreshing the token
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ refresh_token: this.refreshToken }),
      });

      if (response.ok) {
        const data = await response.json();
        this.auth = data.access_token; // Update the auth token with the new one
        Cookies.set("token", this.auth); // Store the new token in cookies
        return true;
      } else {
        // If refresh fails, log out the user or take necessary action
        console.log("Token refresh failed");
        return false;
      }
    },

    async makePostApiCall(endpoint, data) {
      await this.waitForAuthToken(); // Ensure the auth token is available before making the request

      const url = this.baseUrl + endpoint;
      return await fetch(url, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${this.auth}`,
          "Content-Type": "application/json",
        },
        credentials: "same-origin",
        body: JSON.stringify(data),
      });
    },

    async makePostApiCallHome(endpoint, data) {
      const url = this.baseUrl + endpoint;
      return await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "same-origin",
        body: JSON.stringify(data),
      });
    },
  },
});
