<template>
  <Pie :data="chartData" />
</template>

<script>
import { Pie } from "vue-chartjs";
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement } from "chart.js";

// Register the required Chart.js components
ChartJS.register(Title, Tooltip, Legend, ArcElement);

export default {
  name: "PieChart",
  components: { Pie },
  props: {
    chartData: {
      type: Object,
      required: true,
    },
  },
};
</script>
