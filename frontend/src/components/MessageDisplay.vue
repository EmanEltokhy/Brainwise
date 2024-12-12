<template>
  <div v-if="show" :class="['messagee', color]">
    {{ message }}
  </div>
</template>

<script>
export default {
  props: {
    show: Boolean,
    message: Object,
    color: {
      type: String,
      default: "info", // You can set a default color
    },
  },
};
</script>

<style scoped>
.messagee {
  /* Add your desired styles for the message component */
  padding: 10px;
  border-radius: 4px;
  color: white;
}

.success {
  background-color: green;
}

.error {
  background-color: red;
}

.warning {
  background-color: orange;
}

.info {
  background-color: blue;
}
</style>
