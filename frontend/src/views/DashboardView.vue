<template>
  <v-container fluid>
    <v-row class="pt-8">
      <v-col cols="12" md="4">
        <v-card class="pa-4" outlined>
          <v-card-title>Number of Companies</v-card-title>
          <v-card-text class="text-h4 text-center">
            {{ analyticsData.number_of_companies }}
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="4">
        <v-card class="pa-4" outlined>
          <v-card-title>Number of Departments</v-card-title>
          <v-card-text class="text-h4 text-center">
            {{ analyticsData.number_of_departments }}
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="4">
        <v-card class="pa-4" outlined>
          <v-card-title>Number of Employees</v-card-title>
          <v-card-text class="text-h4 text-center">
            {{ analyticsData.number_of_employees }}
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-row class="pt-8">
      <v-col cols="12">
        <v-card class="pa-4" outlined>
          <v-card-title>Employee Status</v-card-title>
          <v-card-text style="height: 400px">
            <BarChart
              :key="chartKey"
              :chart-data="employeeStatusData"
              :options="chartOptions"
            />
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-row class="pt-8">
      <v-col cols="12">
        <v-card class="pa-4" outlined>
          <v-card-title>Top Companies by Employee Count</v-card-title>
          <v-card-text style="height: 400px">
            <PieChart
              :key="pieChartKey"
              :chart-data="topCompaniesData"
              :options="chartOptions"
            />
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-row class="pt-8">
      <v-col cols="12">
        <v-card class="pa-4" outlined>
          <v-card-title>Average Employees per Company</v-card-title>
          <v-card-text class="text-h4 text-center">
            {{ analyticsData.avg_employees_per_company }}
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script setup>
import { ref, onMounted } from "vue";
import { useApiStore } from "@/store/api";
import BarChart from "@/components/BarChart.vue";
import PieChart from "@/components/PieChart.vue";

const chartKey = ref(0);
const pieChartKey = ref(0);

// Analytics Data
const analyticsData = ref({});
const employeeStatusData = ref({
  labels: ["Active Employees", "Inactive Employees", "Onboarding Employees"],
  datasets: [
    {
      label: "Employee Status",
      backgroundColor: ["#4caf50", "#f44336", "#ff9800"],
      data: [],
    },
  ],
});
const topCompaniesData = ref({
  labels: [],
  datasets: [
    {
      label: "Employee Count",
      data: [],
      backgroundColor: ["#2196f3", "#3f51b5", "#ff5722"],
    },
  ],
});

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: "top",
    },
    title: {
      display: false,
    },
  },
};

const apiRequest = useApiStore();

onMounted(() => {
  apiRequest
    .makeApiCall("/accounts/analytics/summary/", "GET")
    .then((response) => response.json())
    .then((data) => {
      analyticsData.value = data;
      employeeStatusData.value.datasets[0].data = [
        data.active_employees,
        data.inactive_employees,
        data.onboarding_employees,
      ];
      chartKey.value++;
      topCompaniesData.value = {
        labels: data.top_companies_data.map((company) => company.name),
        datasets: [
          {
            label: "Employee Count",
            data: data.top_companies_data.map(
              (company) => company.employee_count
            ),
            backgroundColor: ["#2196f3", "#3f51b5", "#ff5722"],
          },
        ],
      };
      pieChartKey.value++;
    })
    .catch((error) => console.error("Failed to fetch analytics data:", error));
});
</script>
<style scoped>
v-container {
  padding: 16px;
  background-color: #f9f9f9;
}

v-row {
  margin-bottom: 32px;
}

v-card {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  background-color: #ffffff;
}

v-card-title {
  font-size: 18px;
  font-weight: bold;
  color: #333333;
}

v-card-text {
  color: #555555;
}

v-card-text[style*="height"] {
  display: flex;
  justify-content: center;
  align-items: center;
}

.text-h4 {
  font-size: 24px;
  font-weight: bold;
  color: #333333;
}

.text-center {
  text-align: center;
}

.chart-container {
  padding: 16px;
}

@media (max-width: 768px) {
  v-col {
    margin-bottom: 16px;
  }

  v-card-title {
    font-size: 16px;
  }

  v-card-text {
    font-size: 14px;
  }
}
</style>
